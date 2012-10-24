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
        print("Unknown course code: %s" % course_code)

What if we unexpectedly encounter an informatics course, which has a course code of ``"INF"``?  The catch-all ``else`` clause will be executed, and we will immediately see a printed message that this course code is unsupported.  If the ``else`` clause were omitted, we might not have noticed that anything was wrong until we tried to use ``department_name`` and discovered that it had never been assigned a value.  Including the ``else`` clause helps us to pick up potential errors caused by missing options early.

* Boolean Operators and Expression
  * and, or and not operators
  * translate operator precedence
  * translate De Morgan's laws
  * remove char type discussion
  * Aha! Replace this with booleans!

* The switch Statement
  * mention Python doesn't have one
  * discuss dictionary-based dispatch

* Conditional Operators Shortcut
  * "x if y else z"

* Errors
  * SyntaxError
  * discussion of Python's exception hierarchy
  * explain where Python fits in
  * static error checking (pyflakes, pep8)

* Testing and Debugging Programs
  * Add discussion of unit vs functional vs integrated tests