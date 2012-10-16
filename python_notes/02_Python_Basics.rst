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

.. Note:: You should also be careful that you don't accidentally redefine variables that have already been defined elsewhere by reusing their names.  In particular, the names of common Python functions like ``len``, ``max`` or ``sort`` are not keywords: you will not get a syntax error if you try to use them.  Redefining variables (accidentally and on purpose) will be discussed in greater detail in the section about scope.

Flow of Control
---------------

In Python, statements are written as a list, in the way that a person would write a list of things to do. The computer starts off by following the first instruction, then the next, in the order that they appear in the program. It only stops executing the program after the last instruction is completed. We refer to the order in which the computer executes instructions as the flow of control. When the computer is executing a particular instruction, we can say that control is at that instruction.

``"__main__"``
--------------

A computer program may be spread across several files and consist of many different functions and classes. Somewhere in the program there must be a starting point -- an instruction which the computer will execute first.  In some languages this is a function with a special name (usually ``main``).  In Python, there is no name reserved for this purpose, and you don't even need to have a function at all -- you may simply write a list of statements, and they will be executed in order.

The second example shows a typical way of designating code to be a Python program's "main function": ``__name__`` is a special variable which is set to the value ``"__main__"`` when the file is executed by Python directly.  If you run the file containing this program, everything inside the ``if`` statement will be executed -- the function will be called, and the message will be printed.  However, if you were to import the function ``my_function`` from a different file, this statement would not be executed.

Indentation and (lack of) semicolons
------------------------------------

Many languages arrange code into blocks using curly braces (``{`` and ``}``) or ``BEGIN`` and ``END`` statements -- these languages encourage you to indent blocks to make code easier to read, but indentation is not compulsory.  Python uses indentation only to delimit blocks, so you *must* indent your code::

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
-----------

Unlike some languages (such as Pascal), Python is case-sensitive. This means that the interpreter treats upper- and lowercase letters as different from one another. For example, ``A`` is different from ``a`` and ``def main()`` is different from ``DEF MAIN()``. Also remember that all reserved words are in lowercase.

More on Comments
----------------

Recall that comments start with ``#`` and continue until the end of the line, for example::

    # This is a comment
    print("Hello!")    # tells the computer to print "Hello!"

Comments are ignored by the interpreter and should be used by a programmer to:

* describe what the program does
* describe (in higher-level terms than the code) how the program works

It is not necessary to comment each line. You should comment in appropriate places where it might not be clear what is going on. You can also put a short comment describing what is taking place in the next few instructions following the comment.

Some languages also have support for comments that span multiple lines, but Python does not.  If you want to type a very long comment in Python, you should split it into multiple shorter lines and put a ``#`` at the start of each line.

.. Note:: It is possible to insert a multi-line string literal into your code by enclosing it in triple quotes.  This is not normally used for comments, except in the special case of docstrings: strings which are inserted at the top of structures like functions and classes, and which document them according to a standard format.  It is good practice to annotate your code in this way because automated tools can then parse it to generate documentation automatically.  We will discuss docstrings further in a future chapter.

.. Note:: You can easily disable part of your program temporarily by commenting out some lines.  Adding or removing many hashes by hand can be time-consuming -- your editor should have a keyboard shortcut which allows you to comment or uncomment all the text you have selected.

Reading and Writing
-------------------

Many programs display text on the screen either to give some information or to ask for some information. For example, you might just want to tell the user what your program does::

    Welcome to John's Calculating Machine.

Perhaps you might want to ask the user for a number::

    Enter the first number:

The easiest way to output information is to display a string literal using the built-in ``print`` function. A string literal is text enclosed in quotes. You can use either single quotes (``'``) or double quotes (``"``) -- but the start quote and the end quote have to match!

These are examples of string literals::

    "Welcome to John's Calculating Machine."
    'Enter the first number:'

.. Todo:: How much stuff about streams do we actually need to put here?

We can tell the computer to print "Hello!" on the console with the following instruction::

    print("Hello!")

As you can see the ``print`` function takes in a string literal as an argument.  It prints the string literal, and by default also prints a newline character at the end -- this is why the console's cursor appears on a new line after you have printed something.  If you want to print a message *without* a newline at the end, you can pass an optional ``end`` parameter into the ``print`` function::

    print("Hello!", end='')

Now ``print`` will print an empty string (i.e. nothing) instead of a newline -- you should see your cursor appear immediately after the message.

To query the user for information, use the ``input`` function::

    first_number = input('Enter the first number: ')

There are several things to note.  First, unlike the ``print`` function, the ``input function`` does *not* print a newline automatically -- the text will be entered directly after the prompt.  That is why we have added a trailing space after the colon.  Second, the function always returns a string -- we will have to convert it to a number ourselves.

The string prompt is optional -- we could just use the ``input`` function without a parameter::

    second_number = input()

String Formatting
-----------------

You will often need to print a message which is not a fixed string -- perhaps you want to include some numbers or other values which are stored in variables.  The recommended way to include these variables in your message is to use string formatting syntax::

    name = "Jane"
    age = 23
    print("Hello! My name is %s." % name)
    print("Hello! My name is %s and I am %d years old." % (name, age))

The symbols in the string which start with percent signs (``%``) are placeholders, and the variables which are to be inserted into those positions are given after the string formatting operator, ``%``, in the same order in which they appear in the string.  If there is only one variable, it doesn't require any kind of wrapper, but if you have more than one you need to put them in a tuple (between round brackets).  The placeholders symbols have different letters depending on the type of the variable -- ``name`` is a string, but ``age`` is an integer.  All the variables will be converted to strings before being combined with the rest of the message.  We will discuss types in more detail soon.

.. Todo:: this is technically deprecated in 3.1, so should we use .format() instead?

Files
-----

Although the ``print`` function prints to the console by default, you can also use it to write to a file.  Here is a simple example::

    with open('myfile.txt', 'w') as myfile:
        print("Hello!", file=myfile)

.. Todo:: do we need to mention flushing?

More on String Literals
-----------------------

Escape Sequences
^^^^^^^^^^^^^^^^

An escape sequence (of characters) can be used to denote a special character which cannot be typed easily on a keyboard or one which has been reserved for other purposes.  For example, you may want to insert a newline into your string::

    print('This is one line.\nThis is another line.')

If your string is enclosed in single quotes, you will have to escape apostrophes, and you need to do the same for double quotes in a string enclosed in double quotes.  An escape sequence starts with a backslash (``\``)::

    print('"Hi! I\'m Jane," she said.')
    print("\"Hi! I'm Jane,\" she said.")

If you did not escape one of these quotes, Python would treat it as the end quote of your string -- and shortly afterwards it would fail to parse the rest of the statement and give you a syntax error::

    >>> print('"Hi! I'm Jane," she said.')
      File "<stdin>", line 1
        print('"Hi! I'm Jane," she said.')
                      ^
    SyntaxError: invalid syntax

Some common escape sequences:

========  =================
Sequence  Meaning
========  =================
``\\``    literal backslash
``\'``    single quote
``\"``    double quote
``\n``    newline
``\t``    tab
========  =================

You can also use escape sequences to output unicode characters.

.. Todo:: argh, how do line endings work on Windows?


Triple quotes
^^^^^^^^^^^^^

In cases where you need to define a long literal spanning multiple lines, or containing many quotes, it may be simplest and most legible to enclose it in triple quotes (either single or double quotes, but of course they must match).  Inside the triple quotes, all whitespace is treated literally -- if you type a newline it will be reflected in your string.  You also don't have to escape any quotes.  Be careful that you don't include anything that you don't mean to -- any indentation will also go inside your string!

These string literals will be identical::

    string_one = '''"Hello," said Jane.
    "Hi," said Bob.'''

    string_two = '"Hello," said Jane.\n"Hi," said Bob.'

.. Todo:: Exercise 4

Built-in types
==============

There are many kinds of information that a computer can process, like numbers and characters. In Python (and other programming languages), the kinds of information the language is able to handle are known as types.  Many common types are built into Python -- for example integers, floating-point numbers and strings.  Users can also define their own types using classes.

In many languages a distinction is made between built-in types (which are often called "primitive types" for this reason) and classes, but in Python they are indistinguishable.  Everything in Python is an object (i.e. an instance of some class) -- that even includes lists and functions.

A type consists of two parts: a domain of possible values and a set of possible operations that can be performed on these values. For example, the domain of the integer type (``int``) contains all integers, while common integer operations are addition, subtraction, multiplication and division.

Python is a dynamically (and not statically) typed language.  That means that you don't have to specify a type for a variable when you create it -- you can use the same variable to store values of different types.  However, Python is also strongly (and not weakly) typed -- at any given time, a variable has a definite type.  If you try to perform operations on variables which have incompatible types (for example, if you try to add a number to a string), Python will exit with a type error instead of trying to guess what you mean.

Integers
--------

An integer (``int`` type) is a whole number such as ``1``, ``5``, ``1350`` or ``-34``. ``1.5`` is not an integer because it has a decimal point. Numbers with decimal points are floating-point numbers. Even ``1.0`` is a floating-point number and not an integer.

Integer operations
^^^^^^^^^^^^^^^^^^

Python can display an integer with the ``print`` function, but only if it is the only argument::

    print(3)
    # You can add two numbers together
    print(1 + 2)

You can't combine a string and an integer directly, because Python is strongly typed::

    >>> print("My number is " + 3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: Can't convert 'int' object to str implicitly

If you want to print a number and a string together, you will have to convert the number to a string somehow::

    # str function converts things to strings.
    # Then you can concatenate two strings with +.
    print("My number is " + str(3))

    # String formatting does the conversion for you.
    print("My number is %d" % 3)

Other integer operations:

===================  ======  ============  ========
Operation            Symbol  Example       Result
===================  ======  ============  ========
Addition             ``+``   ``28 + 10``   ``38``
Subtraction          ``-``   ``28 - 10``   ``18``
Multiplication       ``*``   ``28 * 10``   ``280``
Division             ``//``  ``28 // 10``  ``2``
Modulus (Remainder)  ``%``   ``28 % 10``   ``8``
===================  ======  ============  ========

Note that all these operations are integer operations. That is why the answer to ``28 // 10`` is not ``2.8``, but ``2``. An integer operation results in an integer solution.

.. Note:: In Python 2, the operator ``/`` performed integer division if both the dividend and the divisor were integers, and floating point division if at least one of them was a float.  In Python 3, ``/`` *always* performs floating-point division and ``//`` *always* performs integer division -- even if the dividend and divisor are floats!


Operator precedence
^^^^^^^^^^^^^^^^^^^

Another important thing to keep in mind is operator precedence. For example, ``1 + 2 // 3`` could mean ``(1 + 2) // 3`` or ``1 + (2 // 3)`` depending on where one puts the brackets. To solve this issue, Python has a specific and predictable way to determine the order in which it performs operations. For integer operations, the system will first handle brackets ``()``, followed by ``*``, ``//`` and ``%``, then ``+`` and ``-``. The operators ``*``, ``//`` and ``%`` are in the same level of precedence, so the system will handle them from left to right. ``+`` and ``-`` are handled the same way. Left to right handling is performed for left-associative operators (which all operators mentioned so far are). The following table shows some examples.

============   ====================  ======
Expression     How Python evaluates  Result
============   ====================  ======
20 + 10 // 2   20 + (10 // 2)        25
20 + 10 - 2    (20 + 10) - 2         28
20 - 10 + 2    (20 - 10) + 2         12
20 - 10 * 2    20 - (10 * 2)         0
20 // 10 * 2   (20 // 10) * 2        4
20 * 10 // 2   (20 * 10) // 2        100
============   ====================  ======

.. Todo:: Exercise 5

Floating-point numbers
----------------------

Floating-point numbers (``float`` type) are numbers with a decimal point or an exponent (or both). Examples are ``5.0``, ``10.24``, ``0.0``, ``12.`` and ``.3``. You can use scientific notation to denote very large or very small floating point numbers, e.g. 3.8 x 10\ :sup:`15`. The first part of the number, 3.8, is the mantissa and 15 is the exponent. You can think of the exponent as the number of times you have to move the decimal point to the right to get to the actual value of the number.

In Python, you can write the number 3.8 x 10\ :sup:`15` as ``3.8e15`` or ``3.8e+15``. You can also write it as ``38e14`` or ``.038e17``. They are all the same value. A negative exponent indicates smaller numbers, e.g. ``2.5e-3`` is the same as ``0.0025``. Negative exponents can be thought of as how many times you have to move the decimal point to the left. Negative mantissa indicates that the number itself is negative, e.g. ``-2.5e3`` equals ``-2500`` and ``-2.5e-3`` equals ``-0.0025``.

The ``print`` function will display floating-point numbers in decimal notation if they are greater than or equal to ``1e-4`` and less than ``1e16``, but for smaller and larger numbers it will use scientific notation::

    # This will print 10000000000.0
    print(1e10)

    # This will print 1e+100
    print(1e100)

    # This will print 1e-10
    print(0.0000000001)

When displaying floats, you will usually specify how you would like them to be displayed, using string formatting::

    # This will print 12.35
    print("%.2f" % 12.3456)

    # This will print 1.234560e+01
    print("%e" % 12.3456)

Note that any rounding only affects the display of the numbers. The precision of the number itself is not affected.

Floating-point operations and precedence
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Arithmetic operations for floating-point numbers are the same as those for integers: addition, subtraction, multiplication, division and modulus.  They also use the same operators, except for division -- the floating-point division operator is ``/``.  Floating-point operations always produce a floating-point solution. The order of precedence for these operators is the same as those for integer operators.

Often, you will have to decide which type of number to use in a program. Generally, you should use an integer for counting and measuring discrete whole numbers. Use floating-point numbers for measuring things that are continuous.

You can combine integers and numbers in arithmetic expressions without having to convert them -- this is something that Python will do for you automatically.  If you perform an arithmetic operation on an integer and a floating-point number, the result will always be a floating-point number.

You can use the integer division operator on floating-point numbers, and vice versa. The two division operators are at the same level in the order of precedence.

.. Todo:: Exercise 6

Using strings
-------------

A string is a sequence of characters. You should already be familiar with string literals from working with them in the last section.  In Python, strings (type ``str``) are a special kind of type which is similar to sequence types. In many ways, strings behave in similar ways to lists (type ``list``), which we will discuss in a later chapter, but they also have some functionality specific to text.

.. Note:: In Python 2, the ``str`` type used the ASCII encoding. If you wanted to use strings containing Unicode (for example, characters from other alphabets or special punctuation) you had to use the ``unicode`` type. In Python 3, the ``str`` type uses Unicode.

String Operations
-----------------

We have already introduced a string operation - concatenation (``+``). It can be used to join two strings. There are many built-in functions which perform operations on strings.  String objects also have many useful methods (i.e. functions which are attached to the objects, and accessed with the attribute reference operator, ``.``)::

    name = "Jane Smith"

    # Find the length of a string with the built-in len function
    print(len(name))

    # Print the string converted to lowercase
    print(name.lower())
    # Print the original string
    print(name)

Why does the last print statement output the original value of ``name``? It's because the ``lower`` method does not change the value of ``name``.  It returns a modified *copy* of the value.  If you wanted to change the value of ``name`` permanently, you would have to assign the new value to the variable, like this::

    # Convert the string to lowercase
    name = name.lower()
    print(name)

In Python, strings are *immutable* -- that means that you can't modify part of a string once it has been created.  You can only *replace* it with a modified version.

Variables
=========

Recall that a variable is a label for a location in memory.  It can be used to hold a value.  In statically typed languages, variables have predetermined types, and a variable can only be used to hold values of that type.  In Python, you may reuse the same variable to store values of any type.

A variable is similar to the memory functionality found in most calculators, in that it holds one value which can be retrieved many times, and that storing a new value erases the old. A variable differs from a calculator's memory in that one can have many variables storing different values, and that each variable is referred to by name.

Defining variables
------------------

To define a new variable in Python, you simply assign a value to a label.  For example, this is how you create a variable called ``count``, which contains an integer value of zero::

    count = 0

This is exactly the same syntax as assigning a new value to an existing variable called ``count``.  In the next section we will discuss under what circumstances this statement will cause a new variable will be created.


  If no variable with that name exists **IN THE SAME SCOPE?**, Python will create it for you automatically -- with some exceptions, which we will discuss in the next section.

If you try to access the value of a variable which hasn't been defined anywhere yet, the interpreter will exit with a name error.

We can define several variables in one line::

    # Define three variables at once:
    count, result, total = 0, 0, 0

    # This is equivalent to:
    count = 0
    result = 0
    total = 0

In keeping with good programming style, you should make use of meaningful names for variables.

.. Note:: in statically typed languages, in which variables have types, you must declare the type of a new variable before assigning any value to it -- you can do this in the same step as the value assignment, or in a separate step.  Because of this, it is possible for a variable to be defined, but never to have been assigned a value -- such a variable is said to be ``uninitialised``.  Trying to access the values of uninitialised variables can result in unpredictable errors!  Fortunately, you will never have this problem in Python, because it has no separate variable definition step.  When you create a new variable in Python, you define it and initialize it with a starting value at the same time.

Variable scope and lifetime
---------------------------

Not all variables are accessible from all parts of your program, and not all variables exist for the same amount of time.  Where a variable is accessible and how long it exists depend on how it is defined.  We call the part of a program where a variable is accessible its ''scope'', and the duration for which the variable exists its ''lifetime''.

A variable which is defined in the main body of a file is called a ''global'' variable.  It will be visible throughout the file, and also inside any file which imports that file.  Global variables can have unintended consequences because of their wide-ranging effects -- that is why you should almost never use them.  Only objects which are intended to be used globally, like functions and classes, should be put in the global namespace.

A variable which is defined inside a function is ''local'' to that function.  It is accessible from the point at which it is defined until the end of the function, and exists for as long as the function is executing.

Here is an example of variables in different scopes::

    # This is a global variable
    a = 0

    if (a == 0):
        # This is still a global variable
        b = 1

    def my_function():
        # this is a local variable
        c = 3
        print(c)

    # Now we call the function
    my_function()

    # a and b still exist
    print(a)
    print(b)

    # c doesn't exist anymore -- this will give you a name error!
    print(c)

This may not do what you expect::

    # This is a global variable
    a = 0

    def my_function():
        a = 3
        print(a)

    my_function()

    print(a)

Why does the last print statement also output ``0``?  Because the assignment inside the function does not modify the global ``a``.  It creates a new local variable called ``a``, and assigns the value ``3`` to that variable.  The first print statement prints out the value of the local variable -- because if a local variable has the same name as a global variable the local variable will always take precedence.  The last print statement prints out the global variable, which has remained unchanged.


.. Note:: Variables which are associated with a class are known as ''attributes''.  They can either be ''class'' variables (variables shared between all instances of a class) or ''instance'' variables (a separate variable for each instance) We will look at variable scope within classes in greater detail in a later chapter.





There are three kinds of variable in Java (Note that here we are not talking about the type of the value that is to be stored in that variable). These are local, instance and class variables. Local variables are those defined inside a method such as main(). Instance variables are those defined inside a class, but not in any method in this class. There is a different version of this variable for each object of the class. Class variables (also known as static variable) are defined in the same place as instance variables, but there is only one version per class. Class variables are defined with the keyword static at the beginning. The following example shows the three different kinds of variables.

﻿public class KindsOfVariables {
  int anInstanceVariable;
  static int aClassVariable;

  public static void main(String[] args) {
    int aLocalVariable;
  }
}

The scope of a variable is the part of the program that can make use of the variable i.e where the variable is accessible. A local variable is accessible from its definition to the end of the containing method. Instance and class variables are accessible throughout the class.

The lifetime of a variable is the time when the variable exists. Local variables exist as long as the containing method is running. Instance and class variables exist as long as an object of the class exists.

In the next few units, we will make use of local and instance variables. Static variables will be used in later units. Also remember that local variable's definition must appear earlier in the program than any use of that variable.

Exercise 7

Draw up a summary table comparing the three kinds of variables. It should contain the following columns: definition location, number of versions, scope and lifetime.



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
