import string

from buffer import Buffer
from headless import HeadlessApp
from util import ROW, COL

# [buffer]
class InsertDeleteBuffer(Buffer):
    def insert(self, pos, char):
        assert 0 <= pos[ROW] < self.nrow()
        assert 0 <= pos[COL] <= self.ncol(pos[ROW])
        line = self._lines[pos[ROW]]
        line = line[:pos[COL]] + char + line[pos[COL]:]
        self._lines[pos[ROW]] = line

    def newline(self, pos):
        assert 0 <= pos[ROW] < self.nrow()
        assert 0 <= pos[COL] <= self.ncol(pos[ROW])
        new_line = self._lines[pos[ROW]][pos[COL]:]
        self._lines[pos[ROW]] = self._lines[pos[ROW]][:pos[COL]]
        self._lines.insert(pos[ROW] + 1, new_line)

    def undoNewline(self, pos):
        assert 0 <= pos[ROW] < self.nrow()
        assert 0 <= pos[COL] <= self.ncol(pos[ROW])
        self._lines[pos[ROW]] += self._lines.pop(pos[ROW] + 1)

    def delete(self, pos):
        assert 0 <= pos[ROW] < self.nrow()
        assert 0 <= pos[COL] < self.ncol(pos[ROW])
        line = self._lines[pos[ROW]]
        line = line[:pos[COL]] + line[pos[COL] + 1:]
        self._lines[pos[ROW]] = line
# [/buffer]

# [app]
class InsertDeleteApp(HeadlessApp):
    INSERTABLE = set(string.ascii_letters + string.digits)

    def _make_buffer(self):
        self._buffer = InsertDeleteBuffer(self._lines)
# [/app]

    # [dispatch]
    def _get_key(self):
        key = self._screen.getkey()
        if key in self.INSERTABLE:
            return "INSERT", key
        else:
            return None, key

    def _interact(self):
        family, key = self._get_key()
        if family is None:
            name = f"_do_{key}"
            if hasattr(self, name):
                getattr(self, name)()
        else:
            name = f"_do_{family}"
            if hasattr(self, name):
                getattr(self, name)(key)
        self._add_log(key)
    # [/dispatch]

    # [action]
    def _do_DELETE(self):
        self._buffer.delete(self._cursor.pos())

    def _do_INSERT(self, key):
        self._buffer.insert(self._cursor.pos(), key)
    # [/action]
