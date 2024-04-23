from headless import HeadlessScreen
from undoable import UndoableApp

LINES = ["ab", "cd"]

def make_fixture(keys, size=(2, 2), lines=LINES):
    screen = HeadlessScreen(size, keys)
    app = UndoableApp(size, lines)
    app(screen)
    return app

def get_screen(app):
    return app.get_log()[-1][-1]

# [example]
def test_insert_undo():
    app = make_fixture(["z", "UNDO"])
    assert get_screen(app) == ["ab", "cd"]
# [/example]

def test_no_undo_movement():
    for key in ["KEY_UP", "KEY_DOWN", "KEY_LEFT", "KEY_RIGHT"]:
        app = make_fixture(["z", key, "UNDO"])
        assert get_screen(app) == ["ab", "cd"]

def test_enter_undo():
    app = make_fixture(["KEY_RIGHT", "ENTER", "UNDO"])
    assert get_screen(app) == ["ab","cd"]

### Test runner
import time

def run_tests():
    results = {"pass": 0, "fail": 0, "error": 0}
    for (name, test) in globals().items():
        if not name.startswith("test_"):
            continue
        try:
            test()
            results["pass"] += 1
        except AssertionError:
            results["fail"] += 1
        except Exception:
            results["error"] += 1
    print(f"pass {results['pass']}")
    print(f"fail {results['fail']}")
    print(f"error {results['error']}")



if __name__ == '__main__':
    run_tests()
