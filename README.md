# sp24-lab13
Materials for week 13 lab in CS-370, which includes Ch. 24 "Undo and Redo" adapted from [Software Design by Example](https://third-bit.com/sdxpy/) by Greg Wilson.

_April 23, 2024_

Organization:
* SDX-ch24: The code files for the _SDX Ch. 24_ activity, as downloaded from the book website. The test scripts have been modified to include the test runner from chapter 6.

## Team Members for Part 1
Enter your names here

## Team Roles for Part 1
Who will start out as
* DRIVER: Driver's name
* NAVIGATOR: Navigator's name

You will switch halfway through this activity.

## Part 1 Documentation

Write your answers to the questions below.

* What were the main ideas from SDX chapter 24?
* What questions did you have about the material in the chapters? What did you find confusing?

## Exercise 0: Run the code

First, verify that you can run the test scripts, and that all tests pass.

Next, verify that you can run the base application from Chapter 23:

    python3 app.py 20

Use CTRL-X to quit.

Finally, note that Wilson didn't give us a way to run the new code from Chapter 24 as an interactive text editor.
Try running `undoable.py` and verify nothing happens.
We'll address this in the next exercise.

## Exercise 1: A real text editor

Create a new module `main.py`.  It should take the name of a file and open that file for editing using the `UndoableApp` class.

Verify that you can insert and delete characters, in addition to moving the cursor.

Add a new handler for CTRL-S to save the contents of the file. 
(You can test this with `history.py`, which is not part of the application, or with a new text file obtained elsewhere.)
