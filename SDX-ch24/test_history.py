from headless import HeadlessScreen
from history import HistoryApp

LINES = ["ab", "cd"]

def make_fixture(keys, size=(2, 2), lines=LINES):
    screen = HeadlessScreen(size, keys)
    app = HistoryApp(size, lines)
    app(screen)
    return app

def get_screen(app):
    return app.get_log()[-1][-1]

def test_empty_history():
    app = make_fixture(["KEY_DOWN"])
    assert app.get_history() == []
    assert get_screen(app) == LINES

def test_history_after_insert():
    app = make_fixture(["z"])
    assert app.get_history() == [("insert", (0, 0), "z")]
    assert get_screen(app) == ["za", "cd"]

def test_history_after_delete():
    app = make_fixture(["KEY_RIGHT", "DELETE"])
    assert app.get_history() == [("delete", (0, 1), "b")]
    assert get_screen(app) == ["a_", "cd"]
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
