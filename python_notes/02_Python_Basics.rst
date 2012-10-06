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
    def main():
        print("Hello, World!")

    if __name__ == "__main__":
        main()

This type of program is often referred to as a skeleton program, because one can build upon it to create a more complex program.

The first line of the skeleton program is a comment.  A hash (``#``) denotes the start of a comment.  The interpreter will ignore everything that follows the hash until the end of the line.  Comments will be discussed further in the later part of this unit.

The words ``def`` and ``if`` are keywords or reserved words, i.e. they have been kept for specific purposes and may not be used for any other purposes in the program. The following are keywords in Python::

False      class      finally    is         return
None       continue   for        lambda     try
True       def        from       nonlocal   while
and        del        global     not        with
as         elif       if         or         yield
assert     else       import     pass
break      except     in         raise

Identifiers
-----------

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