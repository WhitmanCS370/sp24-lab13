from headless import HeadlessScreen
from insert_delete import InsertDeleteApp

# [fixture]
def make_fixture(keys, size, lines):
    screen = HeadlessScreen(size, keys)
    app = InsertDeleteApp(size, lines)
    app(screen)
    return app
# [/fixture]

def test_insert_upper_left():
    app = make_fixture(["Z"], (2, 2), ["", ""])
    assert app.get_log()[-1] == ("CONTROL_X", (0, 0), ["Z_", "__"])

def test_delete_left_edge():
    app = make_fixture(["DELETE"], (1, 3), ["abc"])
    assert app.get_log()[-1] == ("CONTROL_X", (0, 0), ["bc_"])

# [example]
def test_delete_middle():
    app = make_fixture(["KEY_RIGHT", "DELETE"], (1, 3), ["abc"])
    assert app.get_log()[-1] == ("CONTROL_X", (0, 1), ["ac_"])
# [/example]

def test_delete_right():
    app = make_fixture(["KEY_RIGHT", "KEY_RIGHT", "DELETE"], (1, 3), ["abc"])
    assert app.get_log()[-1] == ("CONTROL_X", (0, 2), ["ab_"])

def test_delete_empty_line():
    app = make_fixture(["DELETE"], (1, 1), ["a"])
    assert app.get_log()[-1] == ("CONTROL_X", (0, 0), ["_"])

# [empty]
def test_delete_when_impossible():
    try:
        make_fixture(["DELETE"], (1, 1), [""])
    except AssertionError:
        pass
# [/empty]
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
