****************************
Selection Control Statements
****************************

Introduction
============

In the last chapter, you were introduced to the concept of flow of control: the sequence of statements that the computer executes. In procedurally written code, the computer usually executes instructions in the order that they appear.  However, this is not always the case.  One of the ways in which programmers can change the flow of control is the use of selection control statements.

In this chapter you will learn about selection statements, which allow a program to choose when to execute certain instructions. For example, a program might choose how to proceed on the basis of the user's input. As you will be able to see, such statements make a program more versatile.

We will also look at different kinds of programming errors and discuss strategies for finding and correcting them.

Selection: ``if`` statement
---------------------------

People make decisions on a daily basis. What should I have for lunch? What should I do this weekend? Every time you make a decision you base it on some criterion. For example, you might decide what to have for lunch based on your mood at the time, or whether you are on some kind of diet. After making this decision, you act on it. Thus decision-making is a two step process -- first deciding what to do based on a criterion, and secondly taking an action.

Decision-making by a computer is based on the same two-step process. In Python, decisions are made with the ``if`` statement, also known as the selection statement. When processing an ``if`` statement, the computer first evaluates some criterion or condition.  If it is met, the specified action is performed. Here is the syntax for the ``if`` statement::

    if condition:
        # if-body

When it reaches an ``if`` statement, the computer only executes the body of the statement (the statements inside the indented block) only if the condition is true. Here is an example in Python, with a corresponding flowchart::

    if age < 18:
        print("Cannot vote")

.. blockdiag::

    blockdiag {
        orientation = portrait;

        beginpoint [shape = beginpoint, label = ""];
        condition [shape = diamond, label = "Is age less than 18?"];
        yes [shape = square, label = "YES"];
        no [shape = square, label = "NO"];
        body [shape = box, label = "print('Cannot vote')"];
        next [shape = box, label = "next statement\nin program"];

        beginpoint -> condition -> yes -> body -> next;
        condition -> no -> next;
    }

As you can see from the flowchart, the instructions in the ``if`` body are only executed if the condition is met (i.e. if it is true). If the condition is not met (i.e. false), the instructions in the ``if`` body are skipped.


* Put boolean values in here?

* Selection: if statement
  * == vs "is"
  * translate examples

* More on the if statement
  * nested if
  * dangling else not applicable
  * if ladders -> elif

* Boolean Operators and Expression
  * and, or and not operators
  * translate operator precedence
  * translate De Morgan's laws
  * remove char type discussion

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