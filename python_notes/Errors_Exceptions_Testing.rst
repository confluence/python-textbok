******************************
Errors, exceptions and testing
******************************

Errors
======

Errors or mistakes in a program are often referred to as bugs. They are almost always the fault of the programmer. The process of finding and eliminating errors is called debugging. Errors can be classified into three major groups:

* Syntax errors
* Runtime errors
* Logical errors

Syntax errors
-------------

Python will find these kinds of errors when it tries to parse your program, and exit with an error message without running anything.  Syntax errors are mistakes in the use of the Python language, and are analogous to spelling or grammar mistakes in a language like English: for example, the sentence *Would you some tea?* does not make sense -- it is missing a verb.

Common Python syntax errors include:

* leaving out a keyword
* putting a keyword in the wrong place
* leaving out a symbol, such as a colon, comma or brackets
* misspelling a keyword
* incorrect indentation

Python will do its best to tell you where the error is located, but sometimes its messages can be misleading: for example, if you forget to escape a quotation mark inside a string you may get a syntax error referring to a place later in your code, even though that is not the real source of the problem.  If you can't see anything wrong on the line specified in the error message, try backtracking through the previous few lines.  As you program more, you will get better at identifying and fixing errors.

Here are some examples of syntax errors in Python::

    # missing 'def' keyword in function definition
    myfunction(x, y):
        return x + y

    # 'else' clause without an 'if'
    else:
        print("Hello!")

    # missing colon
    if mark >= 50
        print("You passed!")

    # spelling mistake
    if arriving:
        print("Hi!")
    esle:
        print("Bye!")

    # indentation mistake
    if flag:
    print("Flag is set!")

Runtime errors
--------------

If a program is syntactically correct -- that is, free of syntax errors -- it will be run by the Python interpreter.  However, the program may exit unexpectedly during execution if it encounters a *runtime error* -- a problem which was not detected when the program was parsed, but is only revealed when a particular line is executed.  When a program comes to a halt because of a runtime error, we say that it has crashed.

Consider the English instruction *flap your arms and fly to Australia.*  While the instruction is structurally correct and you can understand its meaning perfectly, it is impossible for you to follow it.

Some examples of Python runtime errors:

* division by zero
* performing an operation on incompatible types
* using an identifier which has not been defined
* accessing a list element, dictionary value or object attribute which doesn't exist
* trying to access a file which doesn't exist

Runtime errors often creep in if you don't consider all possible values that a variable could contain, especially when you are processing user input.  You should always try to add checks to your code to make sure that it can deal with bad input and edge cases gracefully.  We will look at this in more detail in the chapter about exception handling.

Logical errors
--------------

Logical errors are the most difficult to fix. They occur when the program runs without crashing, but produces an incorrect result.  The error is caused by a mistake in the program's logic.  You won't get an error message, because no syntax or runtime error has occurred.  You will have to find the problem on your own by reviewing all the relevant parts of your code -- although some tools can flag suspicious code which looks like it could cause unexpected behaviour.

Sometimes there can be absolutely nothing wrong with your Python implementation of an algorithm -- the algorithm itself can be incorrect.  However, more frequently these kinds of errors are caused by programmer carelessness.  Here are some examples of mistakes which lead to logical errors:

* using the wrong variable name
* indenting a block to the wrong level
* using integer division instead of floating point division
* getting operator precedence wrong
* making a mistake in a boolean expression
* off-by-one, and other numerical errors

If you misspell an identifier name, you may get a runtime error or a logical error, depending on whether the misspelled name is defined.

A common source of variable name mix-ups and incorrect indentation is frequent copying and pasting of large blocks of code.  If you have many duplicate lines with minor differences, it's very easy to miss a necessary change when you are editing your pasted lines.  You should always try to factor out excessive duplication using functions and loops -- we will look at this in more detail later.

Handling exceptions
===================

Testing and debugging programs
==============================

Testing
-------

* Something about unit tests
* Black box testing
* Glass box testing
* Add discussion of unit vs functional vs integrated tests

Debugging
---------

* follow error messages
* static error checking: pyflakes, pep8
* print statements
* pdb

.. Todo:: Exercise; exception hierarchy will go in chapter about extensions; [explain where Python fits in??]