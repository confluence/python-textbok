*************
Python Basics
*************

Introduction
============

In this unit, we introduce the basics of the Python programming language. At this point you should already have set up a development environment for writing and running your Python code. It will be assumed in the text that this is the case. If you are having trouble setting up Python, contact a teaching assistant or post a message to the course forum. Throughout this course, you are strongly encouraged to try what you have learnt by writing an actual program. You can only learn how to program by actually doing it yourself.

Learning Objectives
-------------------

At the end of this chapter, you should:

* be able to write short Python programs using variables, expressions, inputs and output statements.
* understand how programs execute sequentially.
* be able to identify parts of a Python program.
* understand the concept of variables, and be able to define a program variable using a meaningful name.
* understand and use the assignment operator.
* be able to explain the difference between implicit and explicit type conversions.
* understand and be able to use explicit type conversion.
* know how to run a Python program.

Python 2 vs Python 3
--------------------

Python recently underwent a major version change from 2 to 3.  For consistency with other courses in the department, we will be using Python 3.  Python 2 is still widely used, and although Python 3 is not fully backwards compatible the two versions are very similar -- so should you ever encounter Python 2 code you should find it quite familiar.  We will discuss some of the major differences later in this chapter.

Essentials of a Python Program
==============================

Simple programs
----------------

In most of today's written languages, words by themselves do not make sense unless they are in certain order and surrounded by correct punctuation symbols. This is also the case with the Python programming language. The Python interpreter is able to interpret and run correctly structured Python programs. For example, the following Python code is correctly structured and will run::

    print("Hello, world!")

Many other languages require a lot more structure in their simplest programs, but in Python this single line, which prints a short message, is sufficient.  It is not, however, a very good example of Python's syntax -- so here is a slightly more complex program which does (almost) exactly the same thing::

    # Here is the main function.
    def my_function():
        print("Hello, World!")

    if __name__ == "__main__":
        my_function()

This type of program is often referred to as a skeleton program, because one can build upon it to create a more complex program.

.. Note:: The first line of the skeleton program is a comment.  A hash (``#``) denotes the start of a comment.  The interpreter will ignore everything that follows the hash until the end of the line.  Comments will be discussed further in the later part of this unit.

Keywords
--------

In the code above, the words ``def`` and ``if`` are keywords or reserved words, i.e. they have been kept for specific purposes and may not be used for any other purposes in the program. The following are keywords in Python::

False      class      finally    is         return
None       continue   for        lambda     try
True       def        from       nonlocal   while
and        del        global     not        with
as         elif       if         or         yield
assert     else       import     pass
break      except     in         raise

Identifier names
----------------

When you write a Python program, you will create many entities -- variables which store values like numbers or strings, as well as functions and classes.  These entities must given names by which they can be referred to uniquely -- these names are known as identifiers.  For example, in our skeleton code above, ``my_function`` is the name of the function.  This particular name has no special significance -- we could also have called the function ``main`` or ``print_hello_world``. What is important is that we use the same name to refer to the function when we call it at the bottom of the program.

Python has some rules that you must follow when forming an identifier:

* it may only contain letters (uppercase or lowercase), numbers or the underscore character (``_``) (no spaces!).
* it may not start with a number.
* it may not be a keyword.

If you break any of these rules, your program will exit with a syntax error.  However, not all identifiers which are syntactically correct are meaningful to human readers.  There are a few guidelines that you should follow when naming your variables to make your code easier to understand (by other people, and by you!) -- this is an important part of following a good coding style:

* be descriptive -- a variable name should describe the contents of the variable; a function name should indicate what the function does; etc..
* don't use abbreviations unnecessarily -- they may be ambiguous and more difficult to read.

Pick a naming convention, and stick to it.  This is a commonly used naming convention in Python:

* names of classes should be in CamelCase (words capitalised and squashed together).
* names of variables which are intended to be constants should be in CAPITAL_LETTERS_WITH_UNDERSCORES.
* names of all other variables should be in lowercase_with_underscores. In some other languages, like Java, the standard is to use camelCase (with the initial letter lowercase), but this style is less popular in Python.
* names of class attributes and methods which are intended to be "private" and not accessed from outside the class should start with an underscore.

Of course there are always exceptions -- for example, many common mathematical symbols have very short names which are nonetheless widely understood.

Here are a few examples of identifiers:

==============  ============  ==============
Syntax error    Bad practice  Good practice
==============  ============  ==============
Person Record   PRcrd         PersonRecord
DEFAULT-HEIGHT  Default_Ht    DEFAULT_HEIGHT
2totalweight    num2          total_weight
==============  ============  ==============

.. Todo:: Exercise 1

.. Note:: A few special identifiers are automatically defined by Python: ``_`` (only in the interactive interpreter), variable names that start and end with two underscores, and class method names that start with two underscores.  You should not use these names for your own variables -- it may lead to unpredictable errors in your code.

.. Note:: You should also be careful that you don't accidentally redefine variables that have already been defined elsewhere by reusing their names.  In particular, the names of common Python functions like ``len``, ``max`` or ``sort`` are not keywords: you will not get a syntax error if you try to use them.  Redefining variables (accidentally and on purpose) will be discussed in greater detail in the section about scope.

Flow of Control
---------------

In Python, statements are written as a list, in the way that a person would write a list of things to do. Recall that this is what makes Python a procedural language. The computer starts off by following the first instruction, then the next, in the order that they appear in the program. It only stops executing the program after the last instruction is completed. We refer to the order in which the computer executes instructions as the flow of control. When the computer is executing a particular instruction, we can say that control is at that instruction.

``"__main__"``
------------

A computer program may be spread across several files and consist of many different functions and classes. Somewhere in the program there must be a starting point -- an instruction which the computer will execute first.  In some languages this is a function with a special name (usually ``main``).  In Python, there is no name reserved for this purpose, and you don't even need to have a function at all -- you may simply write a list of statements, and they will be executed in order.

The second example shows a typical way of designating code to be a Python program's "main function": ``__name__`` is a special variable which is set to the value ``"__main__"`` when the file is executed by Python directly.  If you run the file containing this program, everything inside the ``if`` statement will be executed -- the function will be called, and the message will be printed.  However, if you were to import the function ``my_function`` from a different file, this statement would not be executed.

Indentation and semicolons
--------------------------

Many languages arrange code into blocks using curly braces (``{`` and ``}``) or ``BEGIN`` and ``END`` statements -- these languages encourage you to indent blocks to make code easier to read, but indentation is not compulsory.  Python uses indentation only to delimit blocks::

    # this function definition starts a new block
    def add_numbers(a, b):
        # this instruction is inside the block, because it's indented
        c = a + b
        # so is this one
        return c

    # this if statement starts a new block
    if (it_is_tuesday):
        # this is inside the block
        print("It's Tuesday!")
    # this is outside the block!
    print("Print this no matter what.")

In many languages you need to use a special character to mark the end of each instruction -- usually a semicolon.  Python uses ends of lines to determine where instructions end (except in some special cases when the last symbol on the line lets Python know that the instruction will span multiple lines).  You may optionally use semicolons -- this is something you might want to do if you want to put more than one instruction on a line (but that is usually bad practice)::

    # These all individual instructions -- no semicolons required!
    print("Hello!")
    print("Here's a new instruction")
    a = 2

    # This instruction spans more than one line
    b = [1, 2, 3,
        4, 5, 6]

    # This is legal, but you shouldn't do it
    c = 1; d = 5

.. Todo: Exercise 2 and Exercise 3

Letter Case

Unlike some languages (such as Pascal), Python is case-sensitive. This means that the inerpreter treats upper and lower case letters as different from one another. For example, ``A`` is different to ``a`` and ``def main()`` is different to ``DEF MAIN()``. Also remember that all reserved words are in lower case.

More on Comments

Print
-----

* String Formatting
* Files

Primitive Types
===============

  * simple types -- integers, floats, boolean, strings
  * delay discussion of static and class variables until OO section

* Variables of Primitive Types and Strings
  * assignment is just labelling in Python

* Constants
  * replace with discussion of mutable vs immutable
  * mention constants in other languages.

* Input
  * input()
  * translate scanner example

* Type conversion
  * translate discussion to Python

* Compiling Java Programs
  * Running Python programs
  * Select appropriate Python IDE and translate wizard example

* Differences between Python 2 and 3
  * raw_input()
  * print
  * unicode vs bytes

* translate exercises