*************
Python basics
*************

Introduction
============

In this chapter, we introduce the basics of the Python programming
language. At this point you should already have set up a development
environment for writing and running your Python code. It will be
assumed in the text that this is the case. If you are having trouble
setting up Python, contact a teaching assistant or post a message to
the course forum. Throughout this course, you are strongly encouraged
to try what you have learnt by writing an actual program. You can only
learn how to program by actually doing it yourself.

Each chapter contains several exercises to help you
practice. Solutions are found at the end of the chapter.

.. Todo:: removed learning objectives; possibly they should be added
          to all the chapters.  Move the bit about being able to run
          code, etc. to end of next subsection.

Python 2 vs Python 3
--------------------

Python recently underwent a major version change from 2 to 3.  For
consistency with other courses in the department, we will be using
Python 3.  Python 2 is still widely used, and although Python 3 is not
fully backwards compatible the two versions are very similar -- so
should you ever encounter Python 2 code you should find it quite
familiar.  We will mention important differences between the two
versions throughout this course.  We will always refer to the *latest*
version of Python 2, which at the time of writing was *2.7*.

Getting started with Python
===========================

Using the interactive interpreter
---------------------------------

Running programs from files
---------------------------

.. Todo:: translate the section about compiling programs. Say
          something about how to use the interactive interpreter.
          Include something about an IDE (Wing?).

Installing new packages
-----------------------

* Mention pip, easy_install and system package managers.

Essentials of a Python program
==============================

In most of today's written languages, words by themselves do not make
sense unless they are in certain order and surrounded by correct
punctuation symbols. This is also the case with the Python programming
language. The Python interpreter is able to interpret and run
correctly structured Python programs. For example, the following
Python code is correctly structured and will run::

    print("Hello, world!")

Many other languages require a lot more structure in their simplest
programs, but in Python this single line, which prints a short
message, is sufficient.  It is not, however, a very informative
example of Python's syntax -- so here is a slightly more complex
program which does (almost) exactly the same thing::

    # Here is the main function.
    def my_function():
        print("Hello, World!")

    my_function()

This type of program is often referred to as a skeleton program,
because one can build upon it to create a more complex program.

.. Note:: The first line of the skeleton program is a comment.  A hash
          (``#``) denotes the start of a comment.  The interpreter
          will ignore everything that follows the hash until the end
          of the line.  Comments will be discussed further in the
          later part of this unit.

Keywords
--------

In the code above, the words ``def`` and ``if`` are keywords or
reserved words, i.e. they have been kept for specific purposes and may
not be used for any other purposes in the program. The following are
keywords in Python::

  False      class      finally    is         return
  None       continue   for        lambda     try
  True       def        from       nonlocal   while
  and        del        global     not        with
  as         elif       if         or         yield
  assert     else       import     pass
  break      except     in         raise

Identifier names
----------------

When you write a Python program, you will create many entities --
variables which store values like numbers or strings, as well as
functions and classes.  These entities must given names by which they
can be referred to uniquely -- these names are known as identifiers.
For example, in our skeleton code above, ``my_function`` is the name
of the function.  This particular name has no special significance --
we could also have called the function ``main`` or
``print_hello_world``. What is important is that we use the same name
to refer to the function when we call it at the bottom of the program.

Python has some rules that you must follow when forming an identifier:

* it may only contain letters (uppercase or lowercase), numbers or the
  underscore character (``_``) (no spaces!).
* it may not start with a number.
* it may not be a keyword.

If you break any of these rules, your program will exit with a syntax
error.  However, not all identifiers which are syntactically correct
are meaningful to human readers.  There are a few guidelines that you
should follow when naming your variables to make your code easier to
understand (by other people, and by you!) -- this is an important part
of following a good coding style:

* be descriptive -- a variable name should describe the contents of
  the variable; a function name should indicate what the function
  does; etc..
* don't use abbreviations unnecessarily -- they may be ambiguous and
  more difficult to read.

Pick a naming convention, and stick to it.  This is a commonly used
naming convention in Python:

* names of classes should be in CamelCase (words capitalised and
  squashed together).
* names of variables which are intended to be constants should be in
  CAPITAL_LETTERS_WITH_UNDERSCORES.
* names of all other variables should be in
  lowercase_with_underscores. In some other languages, like Java, the
  standard is to use camelCase (with the initial letter lowercase),
  but this style is less popular in Python.
* names of class attributes and methods which are intended to be
  "private" and not accessed from outside the class should start with
  an underscore.

Of course there are always exceptions -- for example, many common
mathematical symbols have very short names which are nonetheless
widely understood.

Here are a few examples of identifiers:

==============  ============  ==============
Syntax error    Bad practice  Good practice
==============  ============  ==============
Person Record   PRcrd         PersonRecord
DEFAULT-HEIGHT  Default_Ht    DEFAULT_HEIGHT
class           Class         AlgebraCourse
2totalweight    num2          total_weight
==============  ============  ==============

.. Note:: Be careful not to redefine existing variables accidentally
          by reusing their names.  This applies not only to your own
          variables, but to built-in Python functions like ``len``,
          ``max`` or ``sort``: these names are not keywords, and you
          will not get a syntax error if you reuse them, but you will
          encounter confusing results if you try to use the original
          functions later in your program.  Redefining variables
          (accidentally and on purpose) will be discussed in greater
          detail in the section about scope.

Exercise 1
^^^^^^^^^^

Write down why each of the entries in the left column will raise a
syntax error if used as an identifier.


Flow of control
---------------

In Python, statements are written as a list, in the way that a person
would write a list of things to do. The computer starts off by
following the first instruction, then the next, in the order that they
appear in the program. It only stops executing the program after the
last instruction is completed. We refer to the order in which the
computer executes instructions as the flow of control. When the
computer is executing a particular instruction, we can say that
control is at that instruction.

Indentation and (lack of) semicolons
------------------------------------

Many languages arrange code into blocks using curly braces (``{`` and
``}``) or ``BEGIN`` and ``END`` statements -- these languages
encourage you to indent blocks to make code easier to read, but
indentation is not compulsory.  Python uses indentation only to
delimit blocks, so you *must* indent your code::

    # this function definition starts a new block
    def add_numbers(a, b):
        # this instruction is inside the block, because it's indented
        c = a + b
        # so is this one
        return c

    # this if statement starts a new block
    if it_is_tuesday:
        # this is inside the block
        print("It's Tuesday!")
    # this is outside the block!
    print("Print this no matter what.")

In many languages you need to use a special character to mark the end
of each instruction -- usually a semicolon.  Python uses ends of lines
to determine where instructions end (except in some special cases when
the last symbol on the line lets Python know that the instruction will
span multiple lines).  You may optionally use semicolons -- this is
something you might want to do if you want to put more than one
instruction on a line (but that is usually bad style)::

    # These all individual instructions -- no semicolons required!
    print("Hello!")
    print("Here's a new instruction")
    a = 2

    # This instruction spans more than one line
    b = [1, 2, 3,
        4, 5, 6]

    # This is legal, but you shouldn't do it
    c = 1; d = 5

Exercise 2
^^^^^^^^^^

Write down the two statements inside the block created by the
``append_chickens`` function::

    no_chickens = "No chickens here ..."

    def append_chickens(text):
        text = text + " Rawwwk!"
        return text

    print(append_chickens(no_chickens))


Exercise 3
^^^^^^^^^^

The following Python program is not indented correctly. Re-write it so
that it is correctly indented::

    def happy_day(day):
    if day == "monday":
    return ":("
    if day != "monday":
    return ":D"

    print(happy_day("sunday"))
    print(happy_day("monday"))


Letter case
-----------

Unlike some languages (such as Pascal), Python is case-sensitive. This
means that the interpreter treats upper- and lowercase letters as
different from one another. For example, ``A`` is different from ``a``
and ``def main()`` is different from ``DEF MAIN()``. Also remember
that all reserved words (except ``True``, ``False`` and ``None``) are
in lowercase.

More on Comments
----------------

Recall that comments start with ``#`` and continue until the end of
the line, for example::

    # This is a comment
    print("Hello!")    # tells the computer to print "Hello!"

Comments are ignored by the interpreter and should be used by a
programmer to:

* describe what the program does
* describe (in higher-level terms than the code) how the program works

It is not necessary to comment each line. You should comment in
appropriate places where it might not be clear what is going on. You
can also put a short comment describing what is taking place in the
next few instructions following the comment.

Some languages also have support for comments that span multiple
lines, but Python does not.  If you want to type a very long comment
in Python, you should split it into multiple shorter lines and put a
``#`` at the start of each line.

.. Note:: It is possible to insert a multi-line string literal into
          your code by enclosing it in triple quotes.  This is not
          normally used for comments, except in the special case of
          docstrings: strings which are inserted at the top of
          structures like functions and classes, and which document
          them according to a standard format.  It is good practice to
          annotate your code in this way because automated tools can
          then parse it to generate documentation automatically.  We
          will discuss docstrings further in a future chapter.

.. Note:: You can easily disable part of your program temporarily by
          commenting out some lines.  Adding or removing many hashes
          by hand can be time-consuming -- your editor should have a
          keyboard shortcut which allows you to comment or uncomment
          all the text you have selected.

Reading and writing
-------------------

Many programs display text on the screen either to give some
information or to ask for some information. For example, you might
just want to tell the user what your program does::

    Welcome to John's Calculating Machine.

Perhaps you might want to ask the user for a number::

    Enter the first number:

The easiest way to output information is to display a string literal
using the built-in ``print`` function. A string literal is text
enclosed in quotes. You can use either single quotes (``'``) or double
quotes (``"``) -- but the start quote and the end quote have to match!

These are examples of string literals::

    "Welcome to John's Calculating Machine."
    'Enter the first number:'

We can tell the computer to print "Hello!" on the console with the
following instruction::

    print("Hello!")

As you can see the ``print`` function takes in a string literal as an
argument.  It prints the string literal, and by default also prints a
newline character at the end -- this is why the console's cursor
appears on a new line after you have printed something.

To query the user for information, use the ``input`` function::

    first_number = input('Enter the first number: ')

There are several things to note.  First, unlike the ``print``
function, the ``input`` function does *not* print a newline
automatically -- the text will be entered directly after the prompt.
That is why we have added a trailing space after the colon.  Second,
the function always returns a string -- we will have to convert it to
a number ourselves.

The string prompt is optional -- we could just use the ``input``
function without a parameter::

    second_number = input()

.. Note:: in Python 2, there is a function called ``raw_input`` which
          does what ``input`` does in Python 3: that is, it reads
          input from the user, and returns it as a string.  In Python
          2, the function called ``input`` does something different:
          it reads input from the user and tries to evaluate it as a
          Python expression.  There is no function like this in Python
          3, but you can achieve the same result by using the ``eval``
          function on the string returned by ``input``.  ``eval`` is
          almost always a bad idea, and you should avoid using it --
          especially on arbitrary user input that you haven't checked
          first.  It can be very dangerous -- the user could enter
          absolutely anything, including malicious code!

Files
-----

Although the ``print`` function prints to the console by default, you
can also use it to write to a file.  Here is a simple example::

    with open('myfile.txt', 'w') as myfile:
        print("Hello!", file=myfile)

.. Todo:: add a bigger section about simple file I/O here

Built-in types
--------------

There are many kinds of information that a computer can process, like
numbers and characters. In Python (and other programming languages),
the kinds of information the language is able to handle are known as
types.  Many common types are built into Python -- for example
integers, floating-point numbers and strings.  Users can also define
their own types using classes.

In many languages a distinction is made between built-in types (which
are often called "primitive types" for this reason) and classes, but
in Python they are indistinguishable.  Everything in Python is an
object (i.e. an instance of some class) -- that even includes lists
and functions.

A type consists of two parts: a domain of possible values and a set of
possible operations that can be performed on these values. For
example, the domain of the integer type (``int``) contains all
integers, while common integer operations are addition, subtraction,
multiplication and division.

Python is a dynamically (and not statically) typed language.  That
means that you don't have to specify a type for a variable when you
create it -- you can use the same variable to store values of
different types.  However, Python is also strongly (and not weakly)
typed -- at any given time, a variable has a definite type.  If you
try to perform operations on variables which have incompatible types
(for example, if you try to add a number to a string), Python will
exit with a type error instead of trying to guess what you mean.

Integers
========

An integer (``int`` type) is a whole number such as ``1``, ``5``,
``1350`` or ``-34``. ``1.5`` is not an integer because it has a
decimal point. Numbers with decimal points are floating-point
numbers. Even ``1.0`` is a floating-point number and not an integer.

Integer operations
------------------

Python can display an integer with the ``print`` function, but only if
it is the only argument::

    print(3)
    # You can add two numbers together
    print(1 + 2)

You can't combine a string and an integer directly, because Python is
strongly typed::

    >>> print("My number is " + 3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: Can't convert 'int' object to str implicitly

If you want to print a number and a string together, you will have to
convert the number to a string somehow::

    # str function converts things to strings.
    # Then you can concatenate two strings with +.
    print("My number is " + str(3))

    # String formatting does the conversion for you.
    print("My number is %d" % 3)

Other integer operations:

===================  ======  ============  ===================
Operation            Symbol  Example       Result
===================  ======  ============  ===================
Addition             ``+``   ``28 + 10``   ``38``
Subtraction          ``-``   ``28 - 10``   ``18``
Multiplication       ``*``   ``28 * 10``   ``280``
Division             ``//``  ``28 // 10``  ``2``
Modulus (remainder)  ``%``   ``28 % 10``   ``8``
Exponent (power)     ``**``  ``28**10``    ``296196766695424``
===================  ======  ============  ===================

Note that all these operations are integer operations. That is why the
answer to ``28 // 10`` is not ``2.8``, but ``2``. An integer operation
results in an integer solution.

.. Note:: In Python 2, the operator ``/`` performed integer division
          if both the dividend and the divisor were integers, and
          floating point division if at least one of them was a float.
          In Python 3, ``/`` *always* performs floating-point division
          and ``//`` *always* performs integer division -- even if the
          dividend and divisor are floats!


Operator precedence
-------------------

Another important thing to keep in mind is operator precedence. For
example, does ``1 + 2 // 3`` mean ``(1 + 2) // 3`` or ``1 + (2 //
3)``?  Python has a specific and predictable way to determine the
order in which it performs operations. For integer operations, the
system will first handle brackets ``()``, then ``**``, then ``*``,
``//`` and ``%``, and finally ``+`` and ``-``.

If an expression contains multiple operations which are at the same
level of precedence, like ``*``, ``//`` and ``%``, they will be
performed in order, either from left to right (for left-associative
operators) or from right to left (for right-associative operators).
All these arithmetic operators are left-associative, except for
``**``, which is right-associative::

    # all arithmetic operators other than ** are left-associative, so
    2 * 3 / 4
    # is evaluated left to right:
    (2 * 3) / 4

    # ** is right-associative, so
    2 ** 3 ** 4
    # is evaluated right to left:
    2 ** (3 ** 4)


The following table shows some more examples of precedence:

============   ====================  ======
Expression     How Python evaluates  Result
============   ====================  ======
20 + 10 // 2   20 + (10 // 2)        25
20 + 10 - 2    (20 + 10) - 2         28
20 - 10 + 2    (20 - 10) + 2         12
20 - 10 * 2    20 - (10 * 2)         0
20 // 10 * 2   (20 // 10) * 2        4
20 * 10 // 2   (20 * 10) // 2        100
20 * 10 ** 2   20 * (10 ** 2)        2000
============   ====================  ======

Sometimes it's a good idea to add brackets to arithmetic expressions
even if they're not compulsory, because it makes the code more
understandable.

.. Todo:: Exercise 5

Floating-point numbers
======================

Floating-point numbers (``float`` type) are numbers with a decimal
point or an exponent (or both). Examples are ``5.0``, ``10.24``,
``0.0``, ``12.`` and ``.3``. You can use scientific notation to denote
very large or very small floating point numbers, e.g. 3.8 x 10\
:sup:`15`. The first part of the number, 3.8, is the mantissa and 15
is the exponent. You can think of the exponent as the number of times
you have to move the decimal point to the right to get to the actual
value of the number.

In Python, you can write the number 3.8 x 10\ :sup:`15` as ``3.8e15``
or ``3.8e+15``. You can also write it as ``38e14`` or
``.038e17``. They are all the same value. A negative exponent
indicates smaller numbers, e.g. ``2.5e-3`` is the same as
``0.0025``. Negative exponents can be thought of as how many times you
have to move the decimal point to the left. Negative mantissa
indicates that the number itself is negative, e.g. ``-2.5e3`` equals
``-2500`` and ``-2.5e-3`` equals ``-0.0025``.

The ``print`` function will display floating-point numbers in decimal
notation if they are greater than or equal to ``1e-4`` and less than
``1e16``, but for smaller and larger numbers it will use scientific
notation::

    # This will print 10000000000.0
    print(1e10)

    # This will print 1e+100
    print(1e100)

    # This will print 1e-10
    print(0.0000000001)

When displaying floats, you will usually specify how you would like
them to be displayed, using string formatting::

    # This will print 12.35
    print("%.2f" % 12.3456)

    # This will print 1.234560e+01
    print("%e" % 12.3456)

Note that any rounding only affects the display of the numbers. The
precision of the number itself is not affected.

Floating-point operations and precedence
----------------------------------------

Arithmetic operations for floating-point numbers are the same as those
for integers: addition, subtraction, multiplication, division and
modulus.  They also use the same operators, except for division -- the
floating-point division operator is ``/``.  Floating-point operations
always produce a floating-point solution. The order of precedence for
these operators is the same as those for integer operators.

Often, you will have to decide which type of number to use in a
program. Generally, you should use an integer for counting and
measuring discrete whole numbers. Use floating-point numbers for
measuring things that are continuous.

You can combine integers and numbers in arithmetic expressions without
having to convert them -- this is something that Python will do for
you automatically.  If you perform an arithmetic operation on an
integer and a floating-point number, the result will always be a
floating-point number.

You can use the integer division operator on floating-point numbers,
and vice versa. The two division operators are at the same level in
the order of precedence.

.. Todo:: Exercise 6

Strings
=======

A string is a sequence of characters. You should already be familiar
with string literals from working with them in the last section.  In
Python, strings (type ``str``) are a special kind of type which is
similar to sequence types. In many ways, strings behave in similar
ways to lists (type ``list``), which we will discuss in a later
chapter, but they also have some functionality specific to text.

Many other languages have a different variable type for individual
characters -- but in Python single characters are just strings with a
length of 1.

.. Note:: In Python 2, the ``str`` type used the ASCII encoding. If
          you wanted to use strings containing Unicode (for example,
          characters from other alphabets or special punctuation) you
          had to use the ``unicode`` type. In Python 3, the ``str``
          type uses Unicode.

String formatting
-----------------

You will often need to print a message which is not a fixed string --
perhaps you want to include some numbers or other values which are
stored in variables.  The recommended way to include these variables
in your message is to use string formatting syntax::

    name = "Jane"
    age = 23
    print("Hello! My name is %s." % name)
    print("Hello! My name is %s and I am %d years old." % (name, age))

The symbols in the string which start with percent signs (``%``) are
placeholders, and the variables which are to be inserted into those
positions are given after the string formatting operator, ``%``, in
the same order in which they appear in the string.  If there is only
one variable, it doesn't require any kind of wrapper, but if you have
more than one you need to put them in a tuple (between round
brackets).  The placeholders symbols have different letters depending
on the type of the variable -- ``name`` is a string, but ``age`` is an
integer.  All the variables will be converted to strings before being
combined with the rest of the message.

Escape sequences
----------------

An escape sequence (of characters) can be used to denote a special
character which cannot be typed easily on a keyboard or one which has
been reserved for other purposes.  For example, you may want to insert
a newline into your string::

    print('This is one line.\nThis is another line.')

If your string is enclosed in single quotes, you will have to escape
apostrophes, and you need to do the same for double quotes in a string
enclosed in double quotes.  An escape sequence starts with a backslash
(``\``)::

    print('"Hi! I\'m Jane," she said.')
    print("\"Hi! I'm Jane,\" she said.")

If you did not escape one of these quotes, Python would treat it as
the end quote of your string -- and shortly afterwards it would fail
to parse the rest of the statement and give you a syntax error::

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

Triple quotes
-------------

In cases where you need to define a long literal spanning multiple
lines, or containing many quotes, it may be simplest and most legible
to enclose it in triple quotes (either single or double quotes, but of
course they must match).  Inside the triple quotes, all whitespace is
treated literally -- if you type a newline it will be reflected in
your string.  You also don't have to escape any quotes.  Be careful
that you don't include anything that you don't mean to -- any
indentation will also go inside your string!

These string literals will be identical::

    string_one = '''"Hello," said Jane.
    "Hi," said Bob.'''

    string_two = '"Hello," said Jane.\n"Hi," said Bob.'

.. Todo:: Exercise 4

String operations
-----------------

We have already introduced a string operation - concatenation
(``+``). It can be used to join two strings. There are many built-in
functions which perform operations on strings.  String objects also
have many useful methods (i.e. functions which are attached to the
objects, and accessed with the attribute reference operator, ``.``)::

    name = "Jane Smith"

    # Find the length of a string with the built-in len function
    print(len(name))

    # Print the string converted to lowercase
    print(name.lower())
    # Print the original string
    print(name)

Why does the last print statement output the original value of
``name``? It's because the ``lower`` method does not change the value
of ``name``.  It returns a modified *copy* of the value.  If you
wanted to change the value of ``name`` permanently, you would have to
assign the new value to the variable, like this::

    # Convert the string to lowercase
    name = name.lower()
    print(name)

In Python, strings are *immutable* -- that means that you can't modify
a string once it has been created.  However, you can assign a new
string value to an existing variable name.

.. Todo:: modules and tests are in a separate chapter -- should anything
be said here?

.. Todo:: should this be split again into two chapters, with all the
string and number stuff in another chapter?

.. Todo:: translate exercises

.. Todo:: change you to we almost everywhere


Answers to exercises
====================

Answer to exercise 1
--------------------

==============  ================================
Syntax error    Reason
==============  ================================
Person Record   Identifier contains a space.
DEFAULT-HEIGHT  Identifier contains a dash.
class           Identifier is a keyword.
2totalweight    Identifier starts with a number.
==============  ================================

Answer to exercise 2
--------------------

The two statements inside the block defined by the ``append_chickens`` function are::

    text = text + " Rawwwk!"
    return text

Answer to exercise 3
--------------------

The correctly indented code is::

    def happy_day(day):
        if day == "monday":
            return ":("
        if day != "monday":
            return ":D"

    print(happy_day("sunday"))
    print(happy_day("monday"))
