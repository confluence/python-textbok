****************************
Selection Control Statements
****************************

Introduction
============

In the last chapter, you were introduced to the concept of flow of control: the sequence of statements that the computer executes. In procedurally written code, the computer usually executes instructions in the order that they appear.  However, this is not always the case.  One of the ways in which programmers can change the flow of control is the use of selection control statements.

In this chapter you will learn about selection statements, which allow a program to choose when to execute certain instructions. For example, a program might choose how to proceed on the basis of the user's input. As you will be able to see, such statements make a program more versatile.

We will also look at different kinds of programming errors and discuss strategies for finding and correcting them.

Selection: ``if`` statement
===========================

People make decisions on a daily basis. What should I have for lunch? What should I do this weekend? Every time you make a decision you base it on some criterion. For example, you might decide what to have for lunch based on your mood at the time, or whether you are on some kind of diet. After making this decision, you act on it. Thus decision-making is a two step process -- first deciding what to do based on a criterion, and secondly taking an action.

Decision-making by a computer is based on the same two-step process. In Python, decisions are made with the ``if`` statement, also known as the selection statement. When processing an ``if`` statement, the computer first evaluates some criterion or condition.  If it is met, the specified action is performed. Here is the syntax for the ``if`` statement::

    if condition:
        if_body

When it reaches an ``if`` statement, the computer only executes the body of the statement only if the condition is true. Here is an example in Python, with a corresponding flowchart::

    if age < 18:
        print("Cannot vote")

.. blockdiag::

    blockdiag {
        orientation = portrait;

        beginpoint [shape = beginpoint, label = ""];
        condition [shape = diamond, label = "Is age less than 18?"];
        body [shape = box, label = "print('Cannot vote')"];
        next [shape = box, label = "next statement\nin program"];

        beginpoint -> condition -> body -> next;
        condition -> body [label = "YES"];
        condition -> next [label = "NO"];
    }

As you can see from the flowchart, the instructions in the ``if`` body are only executed if the condition is met (i.e. if it is true). If the condition is not met (i.e. false), the instructions in the ``if`` body are skipped.

Relational operators
--------------------

Many ``if`` statements compare two values in order to make a decision. In the last example, we compared the variable ``age`` to the integer ``18`` to test if age less than 18. We used the operator ``<`` for the comparison. This operator is one of the relational operators that can be used in Python. The table below shows Python's relational operators.

========  ========================  ====================
Operator  Description               Example
========  ========================  ====================
==        equal to                  if (age == 18)
!=        not equal to              if (score != 10)
>         greater than              if (num_people > 50)
<         less than                 if (price < 25)
>=        greater than or equal to  if (total >= 50)
<=        less than or equal to     if (value <= 30)
========  ========================  ====================

Note that the condition statement can either be true or false. Also note that the operator for equality is ``==`` -- a double equals sign.  Remember that ``=``, the single equals sign, is the assignment operator.  If you accidentally use ``=`` when you mean ``==``, you are likely to get a syntax error::

    >>> if choice = 3:
    File "<stdin>", line 1
      if choice = 3:
                ^
    SyntaxError: invalid syntax

This is correct::

    if choice == 3:
        print("Thank you for using this program.")

.. Note:: in some languages, an assignment statement *is* a valid conditional expression: it is evaluated as true if the assignment is executed successfully, and as false if it is not. In such languages, it is easier to use the wrong operator by accident and not notice!

Value vs identity
-----------------

So far, we have only compared integers in our examples.  We can also use any of the above relational operators to compare floating-point numbers, strings and many other types::

    # we can compare the values of strings
    if name == "Jane":
        print("Hello, Jane!")

    # ... or floats
    if size < 10.5:
        print(size)

When comparing variables using ``==``, we are doing a *value* comparison: we are checking whether the two variables have the same value.  In contrast to this, we might want to know if two objects such as lists, dictionaries or custom objects that we have created ourselves are *the exact same object*.  This is a test of *identity*.  Two objects might have identical contents, but be two different objects.  We compare identity with the ``is`` operator::

    a = [1,2,3]
    b = [1,2,3]

    if a == b:
        print("These lists have the same value.")

    if a is b:
        print("These lists are the same list.")

It is generally the case (with some caveats) that if two variables are the same object, they are also equal.  The reverse is not true -- two variables could be equal in value, but not the same object.

.. Note:: In many cases, variables of built-in immutable types which have the same value will also be identical.  In some cases this is because the Python interpreter saves memory (and comparison time) by representing multiple values which are equal by the same object.  You shouldn't rely on this behaviour and make value comparisons using ``is`` -- if you want to compare values, always use ``==``.

.. Todo:: Activity 1

Using indentation
-----------------

In the examples which have appeared in this chapter so far, there has only been one statement appearing in the ``if`` body. Of course it is possible to have more than one statement there; for example::

    if choice == 1:
        count += 1
        print("Thank you for using this program.")
    print("Always print this.") # this is outside the if block

The interpreter will treat all the statements inside the indented block as one statement -- it will process all the instructions in the block before moving on to the next instruction.  This allows you to specify multiple instructions to be executed when the condition is met.

``if`` is referred to as a *compound statement* in Python because it combines multiple other statements together.  A compound statement comprises one or more *clauses*, each of which has a *header* (like ``if``) and a *suite* (which is a list of statements, like the ``if`` body).  The contents of the suite are delimited with indentation -- you have to indent lines to the same level to put them in the same block.

The ``else`` clause
-------------------

An optional part of an if statement is the ``else`` clause. It allows you to specify an alternative instruction (or set of instructions) to be executed if the condition is *not* met::

    if condition:
        if_body
    else:
        else_body

To put it another way, the computer will execute the ``if`` body if the condition is true, otherwise it will execute the        ``else`` body. In the example below, the computer will add 1 to x if it is zero, otherwise it will subtract 1 from x::

    if x == 0:
        x += 1
    else:
        x -= 1

This flowchart represents the same statement:

.. blockdiag::

    blockdiag {
        orientation = portrait;

        beginpoint [shape = beginpoint, label = ""];
        condition [shape = diamond, label = "Is x equal\nto 0?"];
        body [shape = box, label = "Add 1 to x"];
        elsebody [shape = box, label = "Subtract 1 from x"];
        next [shape = box, label = "next statement"];

        beginpoint -> condition;
        condition -> body [label = "YES"];
        condition -> elsebody [label = "NO"];
        body, elsebody -> next;
    }

The computer will execute one of the branches before proceeding to the next instruction.

.. Todo:: Exercise 1

More on the ``if`` statement
============================

Nested ``if`` statements
------------------------

In some cases you may want one decision to depend on the result of an earlier decision. For example, you might only have to choose which shop to visit if you decide that you are going to do your shopping, or what to have for dinner after you have made a decision that you are hungry enough for dinner.

.. blockdiag::

    blockdiag {
        orientation = portrait;

        beginpoint [shape = beginpoint, label = ""];
        shopping [shape = diamond, label = "Do I want to go shopping?"];
        where [shape = diamond, label = "Where should I go?"];
        north [shape = box, label = "Shopping at\nNorthgate"];
        south [shape = box, label = "Shopping at\nSouthgate"];
        home [shape = box, label = "Go home"];
        nap [shape = box, label = "Take a nap"];

        beginpoint -> shopping;
        shopping -> where [label = "YES"];
        shopping -> nap [label = "NO"];
        where -> south [label = "Southgate", fontsize = 9];
        where -> north [label = "Northgate", fontsize = 9];
        north, south -> home -> nap;
    }

In Python this is equivalent to putting an ``if`` statement within the body of either the ``if`` or the ``else`` clause of another ``if`` statement.  The following code fragment calculates the cost of sending a small parcel. The post office charges R5 for the first 300g, and R2 for every 100g thereafter (rounded up), up to a maximum weight of 1000g::

    if weight <= 1000:
        if weight <= 300:
            cost = 5
        else:
            cost = 5 + 2 * round((weight - 300)/100)

        print("Your parcel will cost R%d." % cost)

    else:
        print("Maximum weight for small parcel exceeded.")
        print("Use large parcel service instead.")

Note that the bodies of the outer ``if`` and ``else`` clauses are indented, and the bodies of the inner ``if`` and ``else`` clauses are indented one more time.  It is important to keep track of indentation, so that each statement is in the correct block.  It doesn't matter that there's an empty line between the last line of the inner ``if`` statement and the following print statement -- they are still both part of the same block (the outer ``if`` body) because they are indented by the same amount.  You can use empty lines (sparingly) to make your code more readable.

The ``elif`` clause and ``if`` ladders
--------------------------------------

The addition of the else keyword allows you to specify actions for the case in which the condition is false. However, there may be cases in which you would like to handle more than two alternatives. For example, here is a flowchart of a program which works out which grade should be assigned to a particular mark in a test:

.. blockdiag::

    blockdiag {

        beginpoint [shape = beginpoint, label = ""];
        grade [shape = diamond, label = "Which grade?"];
        A [shape = square];
        B [shape = square];
        C [shape = square];
        D [shape = square];
        next [shape = box, label = "Next statement"];

        beginpoint -> grade;
        grade -> A, B, C, D [folded];
        grade -> A [label = "mark >=\n80", fontsize = 9];
        grade -> B [label = "65 <=\nmark < 80", fontsize = 9];
        grade -> C [label = "50 <=\nmark < 65", fontsize = 9];
        grade -> D [label = "mark < 50", fontsize = 9];
        A, B, C, D -> next [folded];
    }

You should be able to write a code fragment for this program using nested if statements. It might look something like this::

    if mark >= 80:
        grade = A
    else:
        if mark >= 65:
            grade = B
        else:
            if mark >= 50:
                grade = C
            else:
                grade = D

This code is a bit difficult to read.  Every time you add a nested ``if``, you have to increase the indentation, so all of your alternatives are indented differently.  You can write this code more cleanly using ``elif`` clauses::

    if mark >= 80:
        grade = A
    elif mark >= 65:
        grade = B
    elif mark >= 50:
        grade = C
    else:
        grade = D

Now all the alternatives are clauses of one ``if`` statement, and are indented to the same level.  This is called an *if ladder*.  Here is a flowchart which more accurately represents this code:

.. blockdiag::

    blockdiag {
        orientation = portrait;

        beginpoint [shape = beginpoint, label = ""];
        mark_80 [shape = diamond, label = "Mark >= 80?"];
        mark_65 [shape = diamond, label = "Mark >= 65?"];
        mark_50 [shape = diamond, label = "Mark >= 50?"];
        A [shape = square];
        B [shape = square];
        C [shape = square];
        D [shape = square];

        beginpoint -> mark_80;
        mark_80 -> A [label = "YES"];
        mark_80 -> mark_65 [label = "NO"];
        mark_65 -> B [label = "YES"];
        mark_65 -> mark_50 [label = "NO"];
        mark_50 -> C [label = "YES"];
        mark_50 -> D [label = "NO"];
    }

The default (catch-all) condition is the ``else`` clause at the end of the statement. If none of the conditions specified earlier is matched, the actions in the ``else`` body will be executed. It is a good idea to include a final ``else`` clause in each ladder to make sure that you are covering all cases, especially if there's a possibility that the options will change in the future.  Consider the following code fragment::

    if course_code == "CSC":
        department_name = "Computer Science"
    elif course_code == "MAM":
        department_name = "Mathematics and Applied Mathematics"
    elif course_code == "STA":
        department_name = "Statistical Sciences"
    else:
        department_name = None
        print("Unknown course code: %s" % course_code)

    if department_name:
        print("Department: %s" % department_name)

What if we unexpectedly encounter an informatics course, which has a course code of ``"INF"``?  The catch-all ``else`` clause will be executed, and we will immediately see a printed message that this course code is unsupported.  If the ``else`` clause were omitted, we might not have noticed that anything was wrong until we tried to use ``department_name`` and discovered that it had never been assigned a value.  Including the ``else`` clause helps us to pick up potential errors caused by missing options early.

Switch statements and dictionary-based dispatch
-----------------------------------------------

``if`` ladders can get unwieldy if they become very long.  Many languages have a control statement called a switch, which tests the value of a single variable and makes a decision on the basis of that value. It is similar to an ``if`` ladder, but can be a little more readable, and is often optimised to be faster.

Python does not have a switch statement, but you can achieve something similar by using a dictionary. This example will be clearer when you have read more about dictionaries, but all you need to know for now is that a dictionary is a store of key and value pairs -- you retrieve a value by its key, the way you would retrieve a list element by its index.  Here is how we can rewrite the course code example::

    DEPARTMENT_NAMES = {
        "CSC": "Computer Science",
        "MAM": "Mathematics and Applied Mathematics",
        "STA": "Statistical Sciences", # Trailing commas like this are allowed in Python!
    }

    if course_code in DEPARTMENT_NAMES: # this tests whether the variable is one of the dictionary's keys
        print("Department: %s" % DEPARTMENT_NAMES[course_code])
    else:
        print("Unknown course code: %s" % course_code)

You are not limited to storing simple values like strings in the dictionary.  In Python, functions can be stored in variables just like any other object, so you can even use this dispatch method to execute completely different statements in response to different values::

    def reverse(string):
        print("'%s' reversed is '%s'." % (string, string[::-1]))

    def capitalise(string):
        print("'%s' capitalised is '%s'." % (string, string.upper()))

    ACTIONS = {
        "r" = reverse, # use the function name without brackets to refer to the function without calling it
        "c" = capitalise,
    }

    my_function = ACTIONS[my_action] # now we retrieve the function
    my_function(my_string) # and now we call it

.. Todo:: Exercise?


The conditional operator
------------------------

Python has another way to write a selection in a program -- the conditional operator. It can be used within an expression (i.e. it can be evaluated) -- in contrast to ``if`` and ``if``-``else``, which are just statements and not expressions.  It is often called the *ternary* operator because it has *three* operands (binary operators have two, and unary operators have one). The syntax is as follows:

*true expression* ``if`` *condition* ``else`` *false expression*

For example::

    result = "Pass" if (score >= 50) else "Fail"

This means that if ``score`` is at least 50, ``result`` is assigned ``"Pass"``, otherwise it is assigned ``"Fail"``. This is equivalent to the following ``if`` statement:

    if (score >= 50):
        result = "Pass"
    else:
        result = "Fail"

The ternary operator can make simple ``if`` statements shorter and more legible, but some people may find your code harder to understand. There is no functional or efficiency difference between a normal ``if``-``else`` and the ternary operator.  You should use the operator sparingly.

.. Todo: exercise 3?


Boolean values, operators and expressions
=========================================

The ``bool`` type
-----------------

In Python there is a value type for variables which can either be true or false: the boolean type, ``bool``.  The true value is ``True`` and the false value is ``False``.  Python will implicitly convert any other value type to a boolean if you use it like a boolean, for example as a condition in an ``if`` statement.   You will almost never have to cast values to ``bool`` explicitly.  You also don't have to use the ``==`` operator explicitly to check if a variable's value evaluates to ``True`` -- you can use the variable name by itself as a condition::

    name = "Jane"

    # This is shorthand for checking if name evaluates to True:
    if name:
        print("Hello, %s!" % name)

    # It means the same thing as this:
    if bool(name) == True:
        print("Hello, %s!" % name)

    # This won't give you the answer you expect:
    if name == True:
        print("Hello, %s!" % name)

Why won't the last ``if`` statement do what you expect?  If you cast the string ``"Jane"`` to a boolean, it will be equal to ``True``, but it isn't equal to ``True`` while it's still a string -- so the condition in the last ``if`` statement will evaluate to ``False``.  This is why you should always use the shorthand syntax, as shown in the first statement -- Python will then do the implicit cast for you.

.. Note:: For historical reasons, the numbers ``0`` and ``0.0`` are actually equal to ``False`` and ``1`` and ``1.0`` are equal to ``True``.  They are not, however, identical objects -- you can test this by comparing them with the ``is`` operator.

At the end of the previous chapter, we discussed how Python converts values to booleans implicitly.  Remember that all non-zero numbers and all non-empty strings are ``True`` and zero and the empty string (``""``) are ``False``.  Other built-in data types that can be considered to be "empty" or "not empty" follow the same pattern.

Boolean operations
------------------

Decisions are often based on more than one factor. For example, you might decide to buy a shirt only if you like it AND it costs less than R100. Or you might decide to go out to eat tonight if you don't have anything in the fridge OR you don't feel like cooking. You can also alter conditions by negating them -- for example you might only want to go to the concert tomorrow if it is NOT raining.  Conditions which consist of simpler conditions joined together with AND, OR and NOT are referred to as *compound conditions*. These operators are known as *boolean operators*.

The ``and`` operator
--------------------

The AND operator in Python is ``and``. A compound expression made up of two subexpressions and the ``and`` operator is only true when *both* subexpressions are true::

    if mark >= 50 and mark < 65:
        print("Grade B")

The compound condition is only true if the given mark is less than 50 *and* it is less than 65. The ``and`` operator works in the same way as its English counterpart. We can define the ``and`` operator formally with a truth table such as the one below.    The table shows the truth value of ``a and b`` for every possible combination of subexpressions ``a`` and ``b``.  For example, if ``a`` is true and ``b`` is true, then ``a and b`` is true.

=========  =========  ===========
``a``      ``b``      ``a and b``
=========  =========  ===========
``True``   ``True``   ``True``
``True``   ``False``  ``False``
``False``  ``True``   ``False``
``False``  ``False``  ``False``
=========  =========  ===========

``and`` is a binary operator so it must be given two operands.  Each subexpression must be a valid complete expression::

    # This is correct:
    if (x > 3 and x < 300):
        x += 1

    # This will give you a syntax error:
    if (x > 3 and < 300): # < 300 is not a valid expression!
        x += 1

You can join three or more subexpressions with ``and`` -- they will be evaluated from left to right::

    condition_1 and condition_2 and condition_3 and condition_4
    # is the same as
    ((condition_1 and condition_2) and condition_3) and condition_4

.. Note:: for the special case of testing whether a number falls within a certain range, you don't have to use the ``and`` operator at all.  Instead of writing ``mark >= 50 and mark < 65`` you can simply write ``50 <= mark < 65``.  This doesn't work in many other languages, but it's a useful feature of Python.

Short-circuit evaluation
------------------------

Note that if ``a`` is false, the expression ``a and b`` is false whether ``b`` is true or not.  The interpreter can take advantage of this to be more efficient: if it evaluates the first subexpression in an AND expression to be false, it does not bother to evaluate the second subexpression.  We call ``and`` a *shortcut operator* or *short-circuit* operator because of this behaviour.

This behaviour doesn't just make the interpreter slightly faster -- you can also use it to your advantage when writing programs.  Consider this example::

    if x > 0 and 1/x < 0.5:
        print("x is %f" % x)

What if x is zero?  If the interpreter were to evaluate both of the subexpressions, you would get a divide by zero error.  But because ``and`` is a short-circuit operator, the second subexpression will only be evaluated if the first subexpression is true.  If x is zero, it will evaluate to false, and the second subexpression will not be evaluated at all.

You could also have used nested ``if`` statements, like this::

    if x > 0:
        if 1/x < 0.5:
            print("x is %f" % x)

Using ``and`` instead is more compact and readable -- especially if you have more than two conditions to check.  These two snippets do the same thing::

    if x != 0:
        if y != 0:
            if z != 0:
                print(1/(x*y*z))

    if x != 0 and y != 0 and z != 0:
        print(1/(x*y*z))

This often comes in useful if you want to access an object's attribute or an element from a list or a dictionary, and you first want to check if it exists::

    if hasattr(my_person, "name") and len(myperson.name) > 30:
        print("That's a long name, %s!" % myperson.name)

    if i < len(mylist) and mylist[i] == 3:
        print("I found a 3!")

    if key in mydict and mydict[key] == 3:
        print("I found a 3!")

The ``or`` operator
-------------------

The OR operator in Java is ``or``.  A compound expression made up of two subexpressions and the ``or`` operator is true when *at least one* of the subexpressions is true.  This means that it is only false in the case where both subexpressions are false, and is true for all other cases. This can be seen in the truth table below:

=========  =========  ==========
``a``      ``b``      ``a or b``
=========  =========  ==========
``True``   ``True``   ``True``
``True``   ``False``  ``True``
``False``  ``True``   ``True``
``False``  ``False``  ``False``
=========  =========  ==========

The following code fragment will print out a message if the given age is less than 0 *or* if it is more than 120::

    if age < 0 or age > 120:
        print("Invalid age: %d" % age)

The interpreter also performs a short-circuit evaluation for ``or`` expressions.  If it evaluates the first subexpression to be true, it will not bother to evaluate the second, because this is suffifent to determine that the whole expression is true.

The || operator is also binary::

    # This is correct:
    if x < 3 or x > 300:
        x += 1

    # This will give you a syntax error:
    if x < 3 or > 300: # > 300 is not a valid expression!
        x += 1

    # This may not do what you expect:
    if x == 2 or 3:
        print("x is 2 or 3")

The last example won't give you an error, because ``3`` is a valid subexpression -- and since it is a non-zero number it evaluates to ``True``.  So the last ``if`` body will always execute, regardless of the value of ``x``!


.. Todo:: at the end mention crazy magic behaviour of ``and`` and ``or``, and what they actually return if they're not applied to booleans.

The ``not`` operator
--------------------

The NOT operator, ``not`` in Python, is a unary operator: it only requires one operand. It is used to reverse an expression, as shown in the following truth table:

=========  =========
``a``      ``not a``
=========  =========
``True``   ``False``
``False``  ``True``
=========  =========

The ``not`` operator can be used to write a less confusing expression. For example, consider the following example in which we want to check whether a string *doesn't* start with "A"::

    if name.startswith("A"):
        pass # a statement body can't be empty -- this is an instruction which does nothing.
    else:
        print("'%s' doesn't start with A!" % s)

    # That's a little clumsy -- let's use "not" instead!
    if not name.startswith("A"):
        print("'%s' doesn't start with A!" % s)

Here are a few other examples::

    # Do something if a flag is False:
    if not my_flag:
        print("Hello!")

    # This...
    if not x == 5:
        x += 1

    # ... is equivalent to this:
    if x != 5:
        x += 1

Precedence rules for boolean expressions
----------------------------------------

Here is a table indicating the relative level of precedence for all the operators we have seen so far, including the arithmetic, relational and boolean operators.

+-------------------------+
| Operators               |
+=========================+
| ``()`` (highest)        |
+-------------------------+
| ``**``                  |
+-------------------------+
| ``*, /, %``             |
+-------------------------+
| ``+, -``                |
+-------------------------+
| ``<, <=, >, >= ==, !=`` |
+-------------------------+
| ``is, is not``          |
+-------------------------+
| ``not``                 |
+-------------------------+
| ``and``                 |
+-------------------------+
| ``or`` (lowest)         |
+-------------------------+

It is always a good idea to use brackets to clarify what you mean, even though you can rely on the order of precedence above.  Brackets can make complex expressions in your code easier to read and understand, and reduce the opportunity for errors.

DeMorgan's law for manipulating boolean expressions
---------------------------------------------------

The ``not`` operator can make expressions more difficult to understand, especially if it is used multiple times.  Try only to use the ``not`` operator where it makes sense to have it.  Most people find it easier to read positive statements than negative ones.  Sometimes you can use the opposite relational operator to avoid using the ``not`` operator, for example::

    if not mark < 50:
        print("You passed")

    # is the same as

    if mark >= 50:
        print("You passed")

This table shows each relational operator and its opposite:

========  ========
Operator  Opposite
========  ========
``==``    ``!=``
``>``     ``<=``
``<``     ``>=``
========  ========

There are other ways to rewrite boolean expressions.  The 19th-century logician DeMorgan proved two properties of negation that we can use.

Consider this example in English: *it is not both cool and rainy today.* Does this sentence mean the same thing as *it is not cool and not rainy today?*  No, the first sentence says that both conditions are not true, but either one of them could be true.  The correct equivalent sentence is *it is not cool or not rainy today.*

We have just used DeMorgan's law to distribute NOT over the first sentence.  Formally, DeMorgan's laws state:

1. NOT (a AND b) = (NOT a) OR (NOT b)
2. NOT (a OR b) = (NOT a) AND (NOT b)

We can use these laws to distribute the ``not`` operator over boolean expressions in Python.  For example::

    if not (age > 0 and age <= 120):
        print("Invalid age")

    # can be rewritten as

    if age <= 0 or age > 120:
        print("Invalid age")

Instead of negating each operator, we used its opposite, eliminating ``not`` altogether.

.. Todo:: Is there anything else to be said about booleans?  Should we add an aside about (the lack of) chars to the previous chapter where we discuss strings?

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

