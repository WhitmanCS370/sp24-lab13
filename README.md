# sp24-lab13
Materials for week 13 lab in CS-370, which includes Ch. 24 "Undo and Redo" adapted from [Software Design by Example](https://third-bit.com/sdxpy/) by Greg Wilson.

_April 23, 2024_

Organization:
* SDX-ch24: The code files for the _SDX Ch. 24_ activity, as downloaded from the book website. The test scripts have been modified to include the test runner from chapter 6.

## Team Members for Part 1
Enter your names here

## Team Roles for Part 1
Who will start out as
* DRIVER: Terence 
* NAVIGATOR: Zurrain

You will switch halfway through this activity.

## Part 1 Documentation

Write your answers to the questions below.

* What were the main ideas from SDX chapter 24?
- I think the main idea in this chapter is using objects to simulate keyboard strokes, record file history and enable undo.

* What questions did you have about the material in the chapters? What did you find confusing?
- We both vaguely understand the chapter and agree that the lack of a visual of the actual program running makes it a bit harder to undertsand and follow along. 

## Exercise 0: Run the code

First, verify that you can run the test scripts, and that all tests pass.

Next, verify that you can run the base application from Chapter 23:

    python3 app.py 20

Use CTRL-X to quit.

Finally, note that Wilson didn't give us a way to run the new code from Chapter 24 as an interactive text editor.
Try running `undoable.py` and verify nothing happens.
We'll address this in a later exercise.

## Exercise 1: Forgetting moves

Most editors do not save cursor movements in their undo history. 
Modify the code in `action.py` so that movement operations are not saved.

Before you modify the code, here is a test case you can add to `test_undoable.py`. It should initially fail.

    def test_no_undo_movement():
        for key in ["KEY_UP", "KEY_DOWN", "KEY_LEFT", "KEY_RIGHT"]:
            app = make_fixture(["z", key, "UNDO"])
            assert get_screen(app) == ["ab", "cd"]

**How did you approach this exercise?**
- At first we tried to modify _interact by preventing move actions to be   added to histroy however that did not work so we tried to prevent the movement keys to be logged in _add_log which also didn't work and finally we added a method save in Move which returns False. This worked becuase now all the move actions were being ignored. 
**Considering the advice of Ousterhout and others, what do you think about the abstractions that Wilson chose?**
- The abstractions are a bit hard to figure out because there are too many classes which means multiple interfaces to try and remember which causes cognitive overload. 

## Exercise 2: Line breaks

Modify the code in `action.py` and `buffer.py` so that pressing the Enter key inserts a new line or breaks the current line in two.
What information do you have to store to make this operation undoable?

Here is a test case to add to `test_action.py`:

    def test_enter():
        app = make_fixture(["KEY_RIGHT", "ENTER"])
        assert get_screen(app) == ["a_","b_"]

And here is a test case to add to `test_undoable.py`:

    def test_enter_undo():
        app = make_fixture(["KEY_RIGHT", "ENTER", "UNDO"])
        assert get_screen(app) == ["ab","cd"]


**How did you approach this exercise?**
We tried to modify Insert methods undo and do to account for the "\n" character but that failed, we then tried to modify the insert method in buffer using the same approach and that too did pass the tests. We could not get our code to pass within the allocated time. 
**Considering the advice of Ousterhout and others, what do you think about the abstractions that Wilson chose?**

## Exercise 3: Redoing operations

Implement a “redo” command that re-executes an operation that has been undone. How does redo differ from undoing an undo? Does it make sense to redo an action that wasn’t done?

Here's an example test case:

    def test_undo_redo():
        app = make_fixture(["KEY_RIGHT", "z", "UNDO", "REDO"])
        assert get_screen(app) == ["az","cd"]

How did you approach this exercise? 
Considering the advice of Ousterhout and others, what do you think about the abstractions that Wilson chose?

## Exercise 4: A real text editor

Create a new main module `main.py`.  It should take the name of a file and open that file for editing using the `UndoableApp` class.

To run the app with a real screen in the terminal, you will need to make the `InsertDeleteApp` class inherit from `App` instead of `HeadlessApp`.
Do this now and resolve any resulting errors. 
Note that you will no longer be able to run the automated tests that use headless mode, which is why I put this exercise last.

Using your knowledge of design patterns and principles, propose a different approach for introducing headless mode
that would allow you to both use the app and run automated tests. What's your approach?

What else do you need to do to make this text editor work as a useful interactive application? 
