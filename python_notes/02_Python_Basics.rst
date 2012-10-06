*************
Python Basics
*************

Introduction
============

In this unit, we introduce the basics of the Python programming language. At this point you should have already set up a development environment for writing and running your Python code. It will be assumed in the text that this is the case. If you are having trouble setting up Python, contact a teaching assistant or post a message to the course forum. Throughout this course, you are strongly encouraged to try what you have learnt by writing an actual program. You can only learn how to program by actually doing it yourself.

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
    def my_function_name():
        print("Hello, World!")

    if __name__ == "__main__":
        my_function_name()

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

When you write a Python program, you will create many entities -- variables which store values like numbers or strings, as well as functions and classes.  These entities must given names by which they can be referred to uniquely -- these names are known as identifiers.  For example, in our skeleton code above, ``my_function_name`` is the name of the function.  This particular name has no special significance -- we could also have called the function ``main`` or ``print_hello_world``. What is important is that we use the same name to refer to the function when we call it at the bottom of the program.

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
* names of all other variables should be in lowercase_with_underscores.
* names of class attributes and methods which are intended to be "private" and not accessed from outside the class should start with an underscore.

Of course there are always exceptions -- for example, many common mathematical symbols have very short names which are nonetheless widely understood.

Here are a few examples of identifiers:

============  ============  =============
Syntax error  Bad practice  Good practice
============  ============  =============

============  ============  =============

.. Note:: A few special identifiers are automatically defined by Python: ``_`` (only in the interactive interpreter), variable names that start and end with two underscores, and class method names that start with two underscores.  You should not use these names for your own variables -- it may lead to unpredictable errors in your code.

.. Note:: You should also be careful that you don't accidentally redefine variables that have already been defined elsewhere by reusing their names.  In particular, the names of common Python functions like ``len``, ``max`` or ``sort`` are not keywords: nothing will stop you from defining new variables with those names, but you may get an unexpected result if you try to use the functions later.

``__main__``
------------

Flow of Control
---------------

Indentation
-----------

Letter Case

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