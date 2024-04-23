import string

from insert_delete import InsertDeleteApp


# [Action]
class Action:
    def __init__(self, app):
        self._app = app

    def do(self):
        raise NotImplementedError(f"{self.__class__.__name__}: do")

    def undo(self):
        raise NotImplementedError(f"{self.__class__.__name__}: undo")
# [/Action]

    def save(self):
        return True


# [Insert]
class Insert(Action):
    def __init__(self, app, pos, char):
        super().__init__(app)
        self._pos = pos
        self._char = char

    def do(self):
        # if self._char == '\n':  
        #     row, col = self._pos
        #     line = self._app._buffer.lines()[row]
        #     self._app._buffer.insert((row, col), '\n')
        #     self._app._cursor.move_to((row + 1, 0))
        # else:
        self._app._buffer.insert(self._pos, self._char)

    def undo(self):
        # if self._char == '\n':  
        #     row, col = self._pos
        #     line = self._app._buffer.lines()[row]
        #     self._app._buffer.insert((row, col), line[col:])
        #     self._app._buffer._lines[row + 1] = self._app._buffer._lines[row + 1][1:]
        #     self._app._cursor.move_to(self._pos)
        # else:
        self._app._buffer.delete(self._pos)
# [/Insert]

    def __str__(self):
        return f"Insert({self._pos}, '{self._char}')"


# [Delete]
class Delete(Action):
    def __init__(self, app, pos):
        super().__init__(app)
        self._pos = pos
        self._char = self._app._buffer.char(pos)

    def do(self):
        self._app._buffer.delete(self._pos)

    def undo(self):
        self._app._buffer.insert(self._pos, self._char)
# [/Delete]

    def __str__(self):
        return f"Delete({self._pos}, '{self._char}')"


# [Move]
class Move(Action):
    def __init__(self, app, direction):
        super().__init__(app)
        self._direction = direction
        self._old = self._app._cursor.pos()
        self._new = None

    def do(self):
        self._app._cursor.act(self._direction)
        self._new = self._app._cursor.pos()

    def undo(self):
        self._app._cursor.move_to(self._old)

    def save(self):
        return False
# [/Move]

    def __str__(self):
        return f"Move('{self._direction}', {self._old}, {self._new})"


class Exit(Action):
    def do(self):
        self._app._running = False

    def __str__(self):
        return f"Exit()"


class ActionApp(InsertDeleteApp):
    INSERTABLE = set(string.ascii_letters + string.digits)

    def __init__(self, size, keystrokes):
        super().__init__(size, keystrokes)
        self._history = []

    def get_history(self):
        return self._history

    def _get_key(self):
        key = self._screen.getkey()
        if key in self.INSERTABLE:
            return "INSERT", key
        else:
            return None, key

    # [interact]
    def _interact(self):
        family, key = self._get_key()
        name = f"_do_{family}" if family else f"_do_{key}"
        if not hasattr(self, name):
            return
        action = getattr(self, name)(key)
        # if isinstance(action, Move):
        #     return
        self._history.append(action)
        action.do()
        self._add_log(key)
    # [/interact]

    def _add_log(self, key):
        # if key not in ["KEY_UP", "KEY_DOWN", "KEY_LEFT", "KEY_RIGHT"]:
        self._log.append((key, self._cursor.pos(), self._screen.display()))

    # [actions]
    def _do_DELETE(self, key):
        return Delete(self, self._cursor.pos())

    def _do_INSERT(self, key):
        return Insert(self, self._cursor.pos(), key)

    def _do_KEY_UP(self, key):
        return Move(self, "up")
    # [/actions]

    def _do_KEY_DOWN(self, key):
        return Move(self, "down")

    def _do_KEY_LEFT(self, key):
        return Move(self, "left")

    def _do_KEY_RIGHT(self, key):
        return Move(self, "right")

    def _do_CONTROL_X(self, key):
        return Exit(self)

