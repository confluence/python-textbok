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

.. Note:: Be careful not to redefine existing variables accidentally by reusing their names.  This applies not only to your own variables, but to built-in Python functions like ``len``, ``max`` or ``sort``: these names are not keywords, and you will not get a syntax error if you reuse them, but you will encounter confusing results if you try to use the original functions later in your program.  Redefining variables (accidentally and on purpose) will be discussed in greater detail in the section about scope.

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
    if it_is_tuesday:
        # this is inside the block
        print("It's Tuesday!")
    # this is outside the block!
    print("Print this no matter what.")

In many languages you need to use a special character to mark the end of each instruction -- usually a semicolon.  Python uses ends of lines to determine where instructions end (except in some special cases when the last symbol on the line lets Python know that the instruction will span multiple lines).  You may optionally use semicolons -- this is something you might want to do if you want to put more than one instruction on a line (but that is usually bad style)::

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

Unlike some languages (such as Pascal), Python is case-sensitive. This means that the interpreter treats upper- and lowercase letters as different from one another. For example, ``A`` is different from ``a`` and ``def main()`` is different from ``DEF MAIN()``. Also remember that all reserved words (except ``True``, ``False`` and ``None``) are in lowercase.

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

.. Note: in Python 2, there is a function called ``raw_input`` which does what ``input`` does in Python 3: that is, it reads input from the user, and returns it as a string.  In Python 2, the function called ``input`` does something different: it reads input from the user and tries to evaluate it as a Python expression.  There is no function like this in Python 3, but you can achieve the same result by using the ``eval`` function on the string returned by ``input``.  ``eval`` is almost always a bad idea, and you should avoid using it -- especially on arbitrary user input that you haven't checked first.  It can be very dangerous -- the user could enter absolutely anything, including malicious code!

String Formatting
-----------------

You will often need to print a message which is not a fixed string -- perhaps you want to include some numbers or other values which are stored in variables.  The recommended way to include these variables in your message is to use string formatting syntax::

    name = "Jane"
    age = 23
    print("Hello! My name is %s." % name)
    print("Hello! My name is %s and I am %d years old." % (name, age))

The symbols in the string which start with percent signs (``%``) are placeholders, and the variables which are to be inserted into those positions are given after the string formatting operator, ``%``, in the same order in which they appear in the string.  If there is only one variable, it doesn't require any kind of wrapper, but if you have more than one you need to put them in a tuple (between round brackets).  The placeholders symbols have different letters depending on the type of the variable -- ``name`` is a string, but ``age`` is an integer.  All the variables will be converted to strings before being combined with the rest of the message.  We will discuss types in more detail soon.


Files
-----

Although the ``print`` function prints to the console by default, you can also use it to write to a file.  Here is a simple example::

    with open('myfile.txt', 'w') as myfile:
        print("Hello!", file=myfile)


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

In Python, strings are *immutable* -- that means that you can't modify a string once it has been created.  However, you can assign a new string value to an existing variable name.

Variables
=========

Recall that a variable is a label for a location in memory.  It can be used to hold a value.  In statically typed languages, variables have predetermined types, and a variable can only be used to hold values of that type.  In Python, you may reuse the same variable to store values of any type.

A variable is similar to the memory functionality found in most calculators, in that it holds one value which can be retrieved many times, and that storing a new value erases the old. A variable differs from a calculator's memory in that one can have many variables storing different values, and that each variable is referred to by name.

Defining variables
------------------

To define a new variable in Python, you simply assign a value to a label.  For example, this is how you create a variable called ``count``, which contains an integer value of zero::

    count = 0

This is exactly the same syntax as assigning a new value to an existing variable called ``count``.  Later in this chapter we will discuss under what circumstances this statement will cause a new variable to be created.

If you try to access the value of a variable which hasn't been defined anywhere yet, the interpreter will exit with a name error.

We can define several variables in one line, but this is usually considered bad style::

    # Define three variables at once:
    count, result, total = 0, 0, 0

    # This is equivalent to:
    count = 0
    result = 0
    total = 0

In keeping with good programming style, you should make use of meaningful names for variables.

Variable scope and lifetime
---------------------------

Not all variables are accessible from all parts of your program, and not all variables exist for the same amount of time.  Where a variable is accessible and how long it exists depend on how it is defined.  We call the part of a program where a variable is accessible its *scope*, and the duration for which the variable exists its *lifetime*.

A variable which is defined in the main body of a file is called a *global* variable.  It will be visible throughout the file, and also inside any file which imports that file.  Global variables can have unintended consequences because of their wide-ranging effects -- that is why you should almost never use them.  Only objects which are intended to be used globally, like functions and classes, should be put in the global namespace.

A variable which is defined inside a function is *local* to that function.  It is accessible from the point at which it is defined until the end of the function, and exists for as long as the function is executing.  The parameter names in the function definition behave like local variables, but they contain the values that you pass into the function when you call it.  When you use the assignment operator (``=``) inside a function, its default behaviour is to create a new local variable -- unless a variable with the same name is already defined in the local scope.

Here is an example of variables in different scopes::

    # This is a global variable
    a = 0

    if a == 0:
        # This is still a global variable
        b = 1

    def my_function(c):
        # this is a local variable
        d = 3
        print(c)
        print(d)

    # Now we call the function, passing the value 7 as the first and only parameter
    my_function(7)

    # a and b still exist
    print(a)
    print(b)

    # c and d don't exist anymore -- these statements will give you name errors!
    print(c)
    print(d)


The assignment operator
-----------------------

As you saw in the previous sections, the assignment operator in Python is a single equals sign (``=``).  This operator assigns the value on the right hand side to the variable on the left hand side, sometimes creating the variable first.  If the right hand side is an expression (such as an arithmetic expression), it will be evaluated before the assignment occurs.  Here are a few examples::

    a_number = 5              # a_number becomes 5
    a_number = total          # a_number becomes the value of total
    a_number = total + 5      # a_number becomes the value of total + 5
    a_number = a_number + 1   # a_number becomes the value of a_number + 1

The last statement might look a bit strange if you were to interpret ``=`` as a mathematical equals sign -- clearly a number cannot be equal to the same number plus one!  Remember that ``=`` is an assignment operator -- this statement is assigning a new value to the variable ``a_number`` which is equal to the old value of ``a_number`` plus one.

Assigning an initial value to variable is called *initialising* the variable.  In some languages defining a variable can be done in a separate step before the first value assignment.  It is thus possible in those languages for a variable to be defined but not have a value -- which could lead to errors or unexpected behaviour if you try to use the value before it has been assigned.  In Python a variable is defined and assigned a value in a single step, so you will almost never encounter situations like this.

The left hand side of the assignment statement must be a valid target::

    # this is fine:
    a = 3

    # these are all illegal:
    3 = 4
    3 = a
    a + b = 3

An assignment statement may have multiple targets separated by equals signs.  The expression on the right hand side of the last equals sign will be assigned to all the targets.  All the targets must be valid::

    # both a and b will be set to zero:
    a = b = 0

    # this is illegal, because we can't set 0 to b:
    a = 0 = b


Compound assignment operators
-----------------------------

You have already seen that you can assign the result of an arithmetic expression to a variable::

    total = a + b + c + 50

Counting is something that is done often in a program. For example, you might want to keep count of how many times a certain event occurs by using a variable called ``count``.   You would initialise this variable to zero and add one to it every time the event occurs.  You would perform the addition with this statement::

    count = count + 1

This is in fact a very common operation.  Python has a shorthand operator, ``+=`` which lets you express it more cleanly, without having to write the name of the variable twice::

    # These statements mean exactly the same thing:
    count = count + 1
    count += 1

    # You can increment a variable by any number you like.
    count += 2
    count += 7
    count += a + b

There is a similar operator, ``-=``, which lets you decrement numbers::

    # These statements mean exactly the same thing:
    count = count - 3
    count -= 3

Other common compound assignment operators are given in the table below:

========  ==========  =============
Operator  Example     Equivalent to
========  ==========  =============
``+=``    ``a += 5``  ``a = a + 5``
``-=``    ``a -= 5``  ``a = a - 5``
``*=``    ``a *= 5``  ``a = a * 5``
``/=``    ``a /= 5``  ``a = a / 5``
``%=``    ``a %= 5``  ``a = a % 5``
========  ==========  =============


More about scope: crossing boundaries
-------------------------------------

What if you want to access a global variable from inside a function?  It is possible, but doing so comes with a few caveats::

    a = 0

    def my_function():
        print(a)

    my_function()

The print statement will output ``0``, the value of the global variable ``a``, as you probably expected.  But what about this program? ::

    a = 0

    def my_function():
        a = 3
        print(a)

    my_function()

    print(a)

When you call the function, the print statement inside outputs ``3`` -- but why does the print statement at the end of the program output ``0``?

By default, the assignment statement creates variables in the local scope.  So the assignment inside the function does not modify the global variable ``a`` -- it creates a new local variable called ``a``, and assigns the value ``3`` to that variable.  The first print statement outputs the value of the new local variable -- because if a local variable has the same name as a global variable the local variable will always take precedence.  The last print statement prints out the global variable, which has remained unchanged.

What if you really want to modify a global variable from inside a function?  You can use the ``global`` keyword::

    a = 0

    def my_function():
        global a
        a = 3
        print(a)

    my_function()

    print(a)

You may not refer to both a global variable and a local variable by the same name inside the same function.  This program will give you an error::

    a = 0

    def my_function():
        print(a)
        a = 3
        print(a)

    my_function()

Because you haven't declared ``a`` to be global, the assignment in the second line of the function will create a local variable ``a``.  This means that you can't refer to the global variable ``a`` elsewhere in the function, even before this line!  The first print statement now refers to the local variable ``a`` -- but this variable doesn't have a value in the first line, because you haven't assigned it yet!

Note that it is usually very bad practice to access global variables from inside functions, and even worse practice to modify them.  This makes it difficult to arrange your program into logically encapsulated parts which do not affect each other in unexpected ways.  If a function needs to access some external value, you should pass the value into the function as a parameter.  If the function is a method of an object, it is sometimes appropriate to make the value an attribute of the same object -- we will discuss this in the chapter about object orientation.

.. Note:: There is also a ``nonlocal`` keyword in Python -- when you nest a function inside another function, it allows you to modify a variable in the outer function from inside the inner function (or, if the function is nested multiple times, a variable in one of the outer functions).  If you use the ``global`` keyword, the assignment statement will create the variable in the global scope if it does not exist already.  If you use the ``nonlocal`` keyword, however, the variable must be defined, because it is impossible for Python to determine in which scope it should be created.

Modifying values
================

Constants
---------

In some languages, it is possible to define special variables which can be assigned a value only once -- once their values have been set, they cannot be changed.  We call these kinds of variables *constants*.  Python does not allow you to set such a restriction on variables, but there is a widely used convention for marking certain variables to indicate that their values are not meant to change: we write their names in all caps, with underscores separating words::

    # These variables are "constants" by convention:
    NUMBER_OF_DAYS_IN_A_WEEK = 7
    NUMBER_OF_MONTHS_IN_A_YEAR = 12

    # Nothing is actually stopping us from redefining them...
    NUMBER_OF_DAYS_IN_A_WEEK = 8

    # ...but it's probably not a good idea.

Why do we bother defining variables that we don't intend to change?  Consider this example::

    MAXIMUM_MARK = 80

    tom_mark = 58
    print(("Tom's mark is %.2f%%" % (tom_mark / MAXIMUM_MARK * 100)))
    # %% is how we escape a literal % inside a string

There are several good reasons to define ``MAXIMUM_MARK`` instead of just writing ``80`` inside the print statement.  First, this gives the number a descriptive label which explains what it is -- this makes the code more understandable.  Second, you may eventually need to refer to this number in your program more than once.  If you ever need to update your code with a new value for the maximum mark, you will only have to change it in one place, instead of finding every place where it is used -- such replacements are often error-prone.

Literal numbers scattered throughout a program are known as "magic numbers" -- using them is considered poor coding style.  This does not apply to small numbers which are considered self-explanatory -- it's easy to understand why a total is initialised to zero or incremented by one.

Sometimes we want to use a variable to distinguish between several discrete options.  It is useful to refer to the option values using constants instead of using them directly if the values themselves have no intrinsic meaning::

    # We define some options
    LOWER, UPPER, CAPITAL = 1, 2, 3

    name = "jane"
    # We use our constants when assigning these values...
    print_style = UPPER

    # ...and when checking them:
    if print_style == LOWER:
        print(name.lower())
    elif print_style == UPPER:
        print(name.upper())
    elif print_style == CAPITAL:
        print(name.capitalize())
    else:
        # Nothing prevents us from accidentally setting print_style to 4, 90 or
        # "spoon", so we put in this fallback just in case:
        print("Unknown style option!")

In the above example, the values ``1``, ``2`` and ``3`` are not important -- they are completely meaningless.  You could equally well use ``4``, ``5`` and ``6`` or the strings ``'lower'``, ``'upper'`` and ``'capital'``.  The only important thing is that the three values must be different.  If we used the numbers directly instead of the constants the program would be much more confusing to read.  Using meaningful strings would make the code more readable, but you could accidentally make a spelling mistake while setting one of the values and not notice -- if you mistype the name of one of the constants you are more likely to get an error straight away.

Some Python libraries define common constants for your convenience, for example::

    # you need to import these libraries before you use them
    import string
    import math
    import re

    # All the lowercase ASCII letters: 'abcdefghijklmnopqrstuvwxyz'
    print(string.ascii_lowercase)

    # The mathematical constants pi and e, both floating point numbers
    print(math.pi) # ratio of circumference of a circle to its diameter
    print(math.e) # natural base of logarithms

    # This integer is an option which you can pass to functions in the re
    # (regular expression) library.
    print(re.IGNORECASE)

Note that many built-in constants don't follow the all-caps naming convention.

Mutable and immutable types
---------------------------

Some *values* in python can be modified, and some cannot.  This does not ever mean that you can't change the value of a variable -- but if a variable contains a value of an *immutable type*, you can only assign it a *new value*.  You cannot *alter the existing value* in any way.

Integers, floating-point numbers and strings are all immutable types -- in all the previous examples, when we changed the values of existing variables we used the assignment operator to assign them new values::

    a = 3
    a = 2

    b = "jane"
    b = "bob"

Even this operator doesn't modify the value of ``total`` in-place -- it also assigns a new value::

    total += 4

We haven't encountered any mutable types yet, but we will use them extensively in later chapters.  Lists and dictionaries are mutable, and so are most objects that you are likely to write yourself::

    # this is a list of numbers
    my_list = [1, 2, 3]
    my_list[0] = 5 # we can change just the first element of the list
    print(my_list)

    class MyClass(object):
        pass # this is a very silly class

    # Now we make a very simple object using our class as a type
    my_object = MyClass()

    # We can change the values of attributes on the object
    my_object.some_property = 42

.. Todo:: Exercise 7

More about input
----------------

In the earlier sections of this unit you learned how to make a program display a message using the ``print`` function or read a string value from the user using the ``input`` function.  What if you want the user to input numbers or other types of variables?  You still use the ``input`` function, but you must convert the string values returned by ``input`` to the types that you want.  Here is a simple example::

    height = int(input("Enter height of rectangle: "))
    width = int(input("Enter width of rectangle: "))

    print("The area of the rectangle is %d" % (width * height))

``int`` is a function which converts values of various types to ints.  We will discuss type conversion in greater detail in the next section, but for now it is important to know that ``int`` will not be able to convert a string to an integer if it contains anything except digits.  The program above will exit with an error if the user enters ``"aaa"``, ``"zzz10"`` or even ``"7.5"``.  When we write a program which relies on user input, which can be incorrect, we need to add some safeguards so that we can recover if the user makes a mistake.  For example, we can detect if the user entered bad input and exit with a nicer error message::

    try:
        height = int(input("Enter height of rectangle: "))
        width = int(input("Enter width of rectangle: "))
    except ValueError as e: # if a value error occurs, we will skip to this point
        print("Error reading height and width: %s" % e)

This program will still only attempt to read in the input once, and exit if it is incorrect.  If we want to keep asking the user for input until it is correct, we can do something like this::

    correct_input = False # this is a boolean value -- it can be either true or false.

    while not correct_input: # this is a while loop
        try:
            height = int(input("Enter height of rectangle: "))
            width = int(input("Enter width of rectangle: "))
        except ValueError:
            print("Please enter valid integers for the height and width.")
        else: # this will be executed if there is no value error
            correct_input = True

We will learn more about boolean values, loops and exceptions later.

Example: calculating petrol consumption of a car
------------------------------------------------

In this example, we will write a simple program which asks the user for the distance travelled by a car, and the monetary value of the petrol that was used to cover that distance. From this information, together with the price per litre of petrol, the program will calculate the efficiency of the car, both in litres per 100 kilometres and and kilometres per litre.

First we will define the petrol price as a constant at the top. This will make it easy for us to update the price when it changes on the first Wednesday of every month::

    PETROL_PRICE_PER_LITRE = 4.50

When the program starts,we want to print out a welcome message::

    print("*** Welcome to the fuel efficiency calculator! ***\n")
    # we add an extra blank line after the message with \n

Ask the user for his or her name::

    name = input("Enter your name: ")

Ask the user for the distance travelled::

    # float is a function which converts values to floating-point numbers.
    distance_travelled = float(input("Enter distance travelled in km: "))

Then ask the user for the amount paid::

    amount_paid = float(input("Enter monetary value of fuel bought for the trip: R"))

Now we will do the calculations::

    fuel_consumed = amount_paid / PETROL_PRICE_PER_LITRE

    efficiency_l_per_100_km = fuel_consumed / distance_travelled * 100
    efficiency_km_per_l = distance_travelled / fuel_consumed

Finally, we output the results::

    print("Hi, %s!" % name)
    print("Your car's efficiency is %.2f litres per 100 km." % efficiency_l_per_100_km)
    print("This means that you can travel %.2f km on a litre of petrol." % efficiency_km_per_l)

    # we add an extra blank line before the message with \n
    print("\nThanks for using the program.")

.. Todo: Exercise 8

Type conversion
===============

As you write more programs, you will often find that you need to convert data from one type to another, for example for a string to an integer or from an integer to a floating-point number.  There are two kinds of type conversions in Python: implicit and explicit conversions.

Implicit conversion
-------------------

Recall from the section about floating-point operators that you can arbitrarily combine integers and floating-point numbers in an arithmetic expression -- and that the result of any such expression will always be a floating-point number.  This is because Python will convert the integers to floating-point numbers before evaluating the expression.  This is an *implicit conversion* -- you don't have to convert anything yourself.  There is usually no loss of precision when an integer is converted to a floating-point number.

For example, the integer ``2`` will automatically be converted to a floating-point number in the following example::

    result = 8.5 * 2

``8.5`` is a ``float`` while ``2`` is an ``int``.  Python will automatically convert operands so that they are of the same type.  In this case this is achieved if the integer ``2`` is converted to the floating-point equivalent ``2.0``.  Then the two floating-point numbers can be multiplied.

Let's have a look at a more complex example::

    result = 8.5 + 7 // 3 - 2.5

Python performs operations according to the order of precedence, and decides whether a conversion is needed on a per-operation basis. In our example ``//`` has the highest precedence, so it will be processed first.  ``7`` and ``3`` are both integers and ``//`` is the integer division operator -- the result of this operation is the integer ``2``. Now we are left with ``8.5 + 2 - 2.5``.  The addition and subtraction are at the same level of precedence, so they are evaluated left-to-right, starting with addition.  First ``2`` is converted to the floating-point number ``2.0``, and the two floating-point numbers are added, which leaves us with ``10.5 - 2.5``.  The result of this floating-point subtraction is ``2.0``, which is assigned to ``result``.

Explicit conversion
-------------------

Converting numbers from ``float`` to ``int`` will result in a loss of precision. For example, try to convert ``5.834`` to an ``int`` -- it is not possible to do this without losing precision. In order for this to happen, you must explicitly tell Python that you are aware that precision will be lost. For example, you need to tell the compiler to convert a ``float`` to an ``int`` like this::

    i = int(5.834)

The ``int`` function converts a ``float`` to an ``int`` by discarding the fractional part -- it will always round down!  If you want more control over the way in which the number is rounded, you will need to use a different function::

    # the floor and ceil functions are in the math module
    import math

    # ceil returns the closest integer greater than or equal to the number
    # (so it always rounds up)
    i = math.ceil(5.834)

    # floor returns the closest integer less than or equal to the number
    # (so it always rounds down)
    i = math.floor(5.834)

    # round returns the closest integer to the number
    # (so it rounds up or down)
    # Note that this is a built-in function -- you don't need to import math to use it.
    i = round(5.834)

Explicit conversion is sometimes also called *casting* -- you may read about a ``float`` being *cast* to ``int`` or vice-versa.

Converting to and from strings
------------------------------

As you saw in the earlier sections, Python seldom performs implicit conversions to and from ``str`` -- you usually have to convert values explicitly.  If you pass a single number (or any other value) to the ``print`` function, it will be converted to a string automatically -- but if you try to add a number and a string, you will get an error::

    # This is OK
    print(5)
    print(6.7)

    # This is not OK
    print("3" + 4)

    # Do you mean this...
    print("3%d" % 4) # concatenate "3" and "4" to get "34"

    # Or this?
    print(int("3") + 4) # add 3 and 4 to get 7

To convert numbers to strings, you can use string formatting -- this is usually the cleanest and most readable way to insert multiple values into a message.  If you want to convert a single number to a string, you can also use the ``str`` function explicitly::

    # These lines will do the same thing
    print("3%d" % 4)
    print("3" + str(4))

More about conversions
----------------------

In Python, functions like ``str``, ``int`` and ``float`` will try to convert *anything* to their respective types -- for example, you can use the ``int`` function to convert strings to integers or to convert floating-point numbers to integers.  Note that although ``int`` can convert a float to an integer it can't convert a string containing a float to an integer directly! ::

    # This is OK
    int("3")

    # This is OK
    int(3.7)

    # This is not OK
    int("3.7") # This is a string representation of a float, not an integer!

    # You have to convert the string to a float first
    int(float("3.7"))

Values of type ``bool`` can contain the value ``True`` or ``False``.  These values are used extensively in conditional statements, which execute or do not execute parts of your program depending on some binary condition::

    my_flag = True

    if my_flag:
        print("Hello!")

The condition is often an expression which evaluates to a boolean value::

    if 3 > 4:
        print("This will not be printed.")

However, almost any value can implicitly be converted to a boolean if it is used in a statement like this::

    my_number = 3

    if my_number:
        print("My number is non-zero!")

This usually behaves in the way that you would expect: non-zero numbers are ``True`` values and zero is ``False``.  However, you should be careful when using strings -- the empty string is treated as ``False``, but any other string is ``True`` -- even ``"0"`` and ``"False"``! ::

    # bool is a function which converts values to booleans
    bool(34) # True
    bool(0) # False
    bool(1) # True

    bool("") # False
    bool("Jane") # True
    bool("0") # True!
    bool("False") # Also True!

.. Todo: come back to translate the section about compiling programs. Shouldn't this go at the *beginning* of the section?  Either way, say something about how to use the interactive interpreter at the beginning of the section.  Include something about an IDE (Wing?).

.. Todo: Differences between Python 2 and 3: unicode vs bytes -- add something about bytes where this is mentioned

.. Todo: translate exercises
