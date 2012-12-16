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

Until now, the programs that we have written have generally ignored the fact that things can go wrong.  We have have tried to prevent runtime errors by checking data which may be incorrect before we used it, but we haven't yet seen how we can handle errors when they do occur -- our programs so far have just crashed suddenly whenever they have encountered one.

There are some situations in which runtime errors are likely to occur.  Whenever we try to read a file or get input from a user, there is a chance that something unexpected will happen -- the file may have been moved or deleted, and the user may enter data which is not in the right format.  Good programmers should add safeguards to their programs so that common situations like this can be handled gracefully -- a program which crashes whenever it encounters an easily forseeable problem is not very pleasant to use.  Most users expect programs to be robust enough to recover from these kinds of setbacks.

If we know that a particular section of our program is likely to cause an error, we can tell Python what to do if it does happen.  Instead of letting the error crash our program we can intercept it, do something about it, and allow the program to continue.

All the runtime (and syntax) errors that we have encountered are called *exceptions* in Python -- Python uses them to indicate that something *exceptional* has occurred, and that your program cannot continue unless it is *handled*.  All exceptions are subclasses of the ``Exception`` class -- we will learn more about classes, and how to write your own exception types, in later chapters.

The ``try`` and ``except`` statements
-------------------------------------

To handle possible exceptions, we use a *try-except* block::

    try:
        age = int(input("Please enter your age: "))
        print("I see that you are %d years old." % age)
    except ValueError:
        print("Hey, that wasn't a number!")

Python will *try* to process all the statements inside the ``try`` block.  If a ``ValueError`` occurs at any point as it is executing them, the flow of control will immediately pass to the ``except`` block, and any remaining statements in the ``try`` block will be skipped.

In this example, we know that the error is likely to occur when we try to convert the user's input to an integer.  If the input string is not a number, this line will trigger a ``ValueError`` -- that is why we specified it as the type of error that we are going to handle.

We could have specified a more general type of error -- or even left the type out entirely, which would have caused the ``except`` clause to match *any* kind of exception -- but that would have been a bad idea.  What if we got a completely different error that we hadn't predicted?  It would be handled as well, and we wouldn't even notice that anything unusual was going wrong.  We may also want to react in different ways to different kinds of errors.  We should always try pick specific rather than general error types for our ``except`` clauses.

It is possible for one ``except`` clause to handle more than one kind of error: we can provide a tuple of exception types instead of a single type::

    try:
        dividend = int(input("Please enter the dividend: "))
        divisor = int(input("Please enter the divisor: "))
        print("%d / %d = %f" % (dividend, divisor, dividend/divisor))
    except(ValueError, ZeroDivisionError):
        print("Oops, something went wrong!")

A *try-except* block can also have multiple ``except`` clauses.  If an exception occurs, Python will check each ``except`` clause from the top down to see if the exception type matches.  If none of the ``except`` clauses match, the exception will be considered *unhandled*, and your program will crash::

.. Todo:: I assume that Python searches the stack first to see if the exception is handled elsewhere. What has been mentioned about the stack already?  This section *really* needs to go after functions.

    try:
        dividend = int(input("Please enter the dividend: "))
        divisor = int(input("Please enter the divisor: "))
        print("%d / %d = %f" % (dividend, divisor, dividend/divisor))
    except ValueError:
        print("The divisor and dividend have to be numbers!")
    except ZeroDivisionError:
        print("The dividend may not be zero!")

Note that in the example above if a ``ValueError`` occurs we won't know whether it was caused by the dividend or the divisor not being an integer -- either one of the input lines could cause that error.  If we want to give the user more specific feedback about which input was wrong, we will have to wrap each input line in a separate *try-except* block::

    try:
        dividend = int(input("Please enter the dividend: "))
    except ValueError:
        print("The dividend has to be a number!")

    try:
        divisor = int(input("Please enter the divisor: "))
    except ValueError:
        print("The divisor has to be a number!")

    try:
        print("%d / %d = %f" % (dividend, divisor, dividend/divisor))
    except ZeroDivisionError:
        print("The dividend may not be zero!")

Exception handling gives us an alternative way to deal with error-prone situations in our code.  Instead of adding checks before doing something to make sure that an error doesn't occur, we just try to do it -- and if an error does occur we handle it.  This can allow us to write simpler and more readable code.  Let's look at a more complicated input example -- one in which we want to keep asking the user for input until the input is correct.  We will try to write this example using the two different approaches::

    # with checks

    n = None
    while n is None:
        s = input("Please enter an integer: ")
        if s.lstrip('-').isdigit():
            n = int(s)
        else:
            print("%s is not an integer." % s)

    # with exception handling

    n = None
    while n is None:
        try:
            s = input("Please enter an integer: ")
            n = int(s)
        except ValueError:
            print("%s is not an integer." % s)

In the first code snippet, we have to write quite a convoluted check to test whether the user's input is an integer -- first we strip off a minus sign if it exists, and then we check if the rest of the string consists only of digits.  But there's a very simple criterion which is also what we really want to know: will this string cause a ``ValueError`` if we try to convert it to an integer?  In the second snippet we can in effect check for exactly the right condition instead of trying to replicate it ourselves -- something which isn't always easy to do.  For example, we could easily have forgotten that integers can be negative, and written the check in the first snippet incorrectly.

The ``else`` and ``finally`` statements
---------------------------------------

* common exceptions
* raising exceptions
* note that writing exceptions will be discussed later

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