from headless import HeadlessScreen
from action import ActionApp

LINES = ["ab", "cd"]

def make_fixture(keys, size=(2, 2), lines=LINES):
    screen = HeadlessScreen(size, keys)
    app = ActionApp(size, lines)
    app(screen)
    return app

def get_screen(app):
    print(app.get_log())
    return app.get_log()[-1][-1]

def test_no_action():
    app = make_fixture(["KEY_DOWN"])
    assert get_screen(app) == LINES

def test_immediate_insert():
    app = make_fixture(["z"])
    assert get_screen(app) == ["za", "cd"]

def test_move_and_delete():
    app = make_fixture(["KEY_RIGHT", "DELETE"])
    assert get_screen(app) == ["a_", "cd"]

def test_enter():
    """ Inserting _ as a new line character doesn't move 'b' over, but it removes it completely.
    """
    app = make_fixture(["KEY_RIGHT", "ENTER"])
    print(get_screen(app))
    assert get_screen(app) == ["a_","b_"]

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
