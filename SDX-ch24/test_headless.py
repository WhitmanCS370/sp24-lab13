from headless import HeadlessApp, HeadlessScreen

def test_no_keystrokes():
    size = (2, 2)
    lines = []
    keys = []
    screen = HeadlessScreen(size, keys)
    app = HeadlessApp(size, lines)
    app(screen)
    assert app.get_log() == [
        ("CONTROL_X", (0, 0), ["__", "__"])
    ]

def test_move_right():
    size = (2, 2)
    lines = ["ab", "cd"]
    keys = ["KEY_RIGHT"]
    screen = HeadlessScreen(size, keys)
    app = HeadlessApp(size, lines)
    app(screen)
    assert app.get_log() == [
        ("KEY_RIGHT", (0, 1), lines),
        ("CONTROL_X", (0, 1), lines)
    ]

# [example]
def test_scroll_down():
    size = (2, 2)
    lines = ["abc", "def", "ghi"]
    keys = ["KEY_DOWN"] * 3
    screen = HeadlessScreen(size, keys)
    app = HeadlessApp(size, lines)
    app(screen)
    assert app.get_log()[-1] == ("CONTROL_X", (2, 0), ["de", "gh"])
# [/example]

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
