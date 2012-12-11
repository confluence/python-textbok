***********************
Loop Control Statements
***********************

Introduction
============

In this chapter, you will learn how to make the computer execute a group of statements over and over as long as certain criterion holds. The group of statements being executed repeatedly is called a loop. There are two loop statements in Python: ``for`` and ``while``.  We will discuss the difference between these statements later in the chapter, but first let us look at an example of a loop in the real world.

A petrol attendant performs the following actions when serving a customer:

#. greet customer
#. ask for required type of petrol and amount
#. ask whether customer needs other services
#. ask for required amount of money
#. give money to cashier
#. wait for change and receipt
#. give change and receipt to customer
#. say thank you and goodbye

A petrol attendant performs these steps for each customer, but he does not follow them when there is no customer to serve. He also only performs them when it is his shift. If we were to write a computer program to simulate this behaviour, it would not be enough just to provide the steps and ask the computer to repeat them over and over. We would also need to tell it when to stop executing them.

There are two major kinds of programming loops: counting loops and event-controlled loops.

In a counting loop, the computer knows at the beginning of the loop execution how many times it needs to execute the loop. In Python, this kind of loop is defined with the ``for`` statement, which executes the loop body *for* every item in some list.

In an event-controlled loop, the computer stops the loop execution when a condition is no longer true. In Python, you can use the ``while`` statement for this -- it executes the loop body *while* the condition is true.  The ``while`` statement checks the condition *before* performing each iteration of the loop.  Some languages also have a loop statement which performs the check *after* each iteration, so that the loop is always executed at least once.  Python has no such construct, but we will see later how you can simulate one.

Counting loops are actually subset of event-control loop - the loop is repeated until the required number of iterations is reached.

If you wanted to get from Cape Town to Camps Bay, what loop algorithm would you use?  If you started by putting your car on the road to Camps Bay, you could:

* drive for exactly 15 minutes. After 15 minutes, stop the car and get out.
* drive for exactly 8km. After 8km, stop the car and get out.
* drive as long as you are not in Camps Bay. When you arrive, stop the car and get out.

The first two algorithms are based on counting -- the first counts time, and the second counts distance.  Neither of these algorithms guarantees that you will arrive in Camps Bay. In the first case, you might hit heavy traffic or none at all, and either fall short of or overshoot your desired destination. In the second case, you might find a detour and end up nowhere near Camps Bay.

The third algorithm is event-controlled. You carry on driving as long as you are not at the beach. The condition you keep checking is *am I at the beach yet?*.

Many real-life activities are event-controlled. For example, you drink as long as you are thirsty. You read the newspaper as long as you are interested.  Some activities are based on multiple events -- for example, a worker works as long as there is work to do and the time is not 5pm.

The ``while`` statement
=======================

Python's event-controlled loop statement is the ``while`` statement. You should use it when you don't know beforehand how many times you will have to execute the body of the loop.  The while-body keeps repeating as long as the condition is true.  Here's a flow control diagram for the while statement:

.. blockdiag::

    blockdiag {
        orientation = portrait;

        beginpoint [shape = beginpoint, label = ""];
        init [shape = box, label = "Initialisation"];
        condition [shape = diamond, label = "Is the condition true?"];
        body [shape = box, label = "while-body"];
        update [shape = box, label = "Update"];
        next [shape = box, label = "Next statement"];

        beginpoint -> init -> condition -> body -> update;
        update -> condition;
        condition -> body [label = "YES"];
        condition -> next [label = "NO"];
    }

The loop consists of three important parts: the *initialisation*, the *condition*, and the *update*.  In the initialisation step, you set up the variable which you're going to use in the condition.  In the condition step, you perform a test on the variable to see whether you should terminate the loop or execute the body another time.  Then, after each successfully completed execution of the loop body, you update your variable.

Note that the condition is checked before the loop body is executed for the first time -- if the condition is false at the start, the loop body will never be executed at all.

Here is a simple Python example which adds the first ten integers together::

    total = 0
    i = 1

    while i <=10:
        total += i
        i += 1

The variable used in the loop condition is the number ``i``, which you use to count the integers from ``1`` to ``10``.  First you *initialise* this number to ``1``.  In the *condition*, you check whether ``i`` is less than or equal to ``10``, and if this is true you execute the loop body.  Then, at the end of the loop body, you *update* ``i`` by incrementing it by ``1``.

It is very important that you increment ``i`` at the end.  If you did not, ``i`` would always be equal to ``1``, the condition would always be true, and your program would never terminate -- we call this an infinite loop.  Whenever you write a ``while`` loop, make sure that the variable you use in your condition is updated inside the loop body!

Here are a few common errors which might result in an infinite loop::

    x = 0
    while x < 3:
        y += 1 # wrong variable updated

    product = 1
    count = 1

    while count <= 10:
        product *= count
        # forgot to update count

    x = 0
    while x < 5:
        print(x)
    x += 1 # update statement is indented one level too little, so it's outside the loop body

    x = 0
    while x != 5:
        print(x)
        x += 2 # x will never equal 5, because we are counting in even numbers!

You might be wondering why the Python interpreter cannot catch infinite loops. This is known as the halting problem. It is impossible for a computer to detect all possible infinite loops in another program. It is up to the programmer to avoid infinite loops.

In many of the examples above, we are counting to a predetermined number, so it would really be more appropriate for us to use a ``for`` loop (which will be introduced in the next section) -- that is the loop structure which is more commonly used for counting loops.  Here is a more realistic example::

    # numbers is a list of numbers -- we don't know what the numbers are!

    total = 0
    i = 0

    while i < len(numbers) and total < 100:
        total += numbers[i]
        i +=1

Here we add up numbers from a list until the total reaches 100.  We don't know how many times we will have to execute the loop, because we don't know the values of the numbers.  Note that we might reach the end of the list of numbers before the total reaches 100 -- if we try to access an element beyond the end of the list we will get an error, so we should add a check to make sure that this doesn't happen.


The ``for`` statement
=====================

Python's other loop statement is the ``for`` statement.  You should use it when you need to do something for some predefined number of steps.  Before we look at Python's ``for`` loop syntax, we will briefly look at the way *for* loops work in other languages.

Here is an example of a *for* loop in Java::

    for (int count = 1; count <= 8; count++) {
        System.out.println(count);
    }

You can see that this kind of *for* loop has a lot in common with a *while* loop -- in fact, you could say that it's just a special case of a *while* loop.  The initialisation step, the condition and the update step are all defined in the section in parentheses on the first line.

*for* loops are often used to perform an operation on every element of some kind of sequence. If you wanted to iterate over a list using the classic-style *for* loop, you would have to count from zero to the end of the list, and then access each list element by its index.

In Python, ``for`` loops make this use case simple and easy by allowing you to iterate over sequences directly.  Here is an example of a ``for`` statement which counts from 1 to 8:

    for i in range(8):
        print(i + 1) # range(8) starts at 0 and ends at 7

``range`` is a special kind of Python function called a *generator* -- it returns an *iterator* object, which *yields* a series of values until it stops.  In this case, the iterator will yield the integers from ``0`` to ``7``, one at a time.  When the end of the iterator is reached, the ``for`` loop will exit.

You can use ``for`` to iterate over any kind of sequence, whether it's an iterator or a list.  You can iterate over a list of strings like this:

    pets = ["cat", "dog", "budgie"]

    for pet in pets:
        print(pet)

At each iteration of the loop, the next element of the list ``pets`` is assigned to the variable ``pet``, which you can then access inside the loop body.  The example above is functionally identical to this:

    for i in range(len(pets)): # i will iterate over 0, 1 and 2
        pet = pets[i]
        print(pet)

That is similar to the way ``for`` loops are written in, for example, Java.  You should avoid doing this, as it's more difficult to read, and unnecessarily complex.  If for some reason you need the index inside the loop as well as the list element itself, you can use the ``enumerate`` function to number the elements:

    for i, pet in enumerate(pets):
        pets[i] = pet.upper() # rewrite the list in all caps

``enumerate`` also returns an iterator -- each item it returns is a ``tuple``, or pair of values -- the first is the element index (starting at zero) and the second is the element itself.  In the loop above, at each iteration the value of the index is assigned to the variable ``i``, and the element is assigned to the variable ``pet``, as before.

Why couldn't we just write ``pet = pet.upper()``?  That would just assign a new value to the variable ``pet`` inside the loop, without changing the original list.

This brings us to a common ``for`` loop pitfall: modifying a list while you're iterating over it.  The example above only modifies elements in-place, and doesn't change their order around, but you can cause all kinds of errors and unintended behaviour if you insert or delete list elements in the middle of iteration::

    numbers = [1, 2, 2, 3]

    for i, num in enumerate(numbers):
        if num == 2:
            del numbers[i]

    print(numbers) # oops -- we missed one, because we shifted the elements around while we were iterating!

Sometimes you can avoid this by iterating over a *copy* of the list instead, but it won't help you in this case -- as you delete elements from the original list, it will shrink, so the indices from the unmodified list copy will soon exceed the length of the modified list and you will get an error.  In general, if you want to select a subset of elements from a list on the basis of some criterion, you should use a *list comprehension* instead. We will look at them at the end of this chapter.

.. Todo:: exercise; and we definitely need to discuss lists before this chapter.

The ``break`` and ``continue`` statements
=========================================

``break``
---------

Inside the loop body, you can use the ``break`` statement to exit the loop immediately. You might want to test for a special case which will result in immediate exit from the loop. For example::

    x = 1

    while x <= 10:
        if x == 5:
            break

        print(x)
        x += 1

The code fragment above will only print out the numbers ``1`` to ``4``. In the case where ``x`` is ``5``, the ``break`` statement will be encountered, and the flow of control will leave the loop immediately.

``continue``
------------

The ``continue`` statement is similar to the ``break`` statement, in that it causes the flow of control to exit the current loop body at the point of encounter -- but the loop itself is not exited. For example::

    for x in range(1, 10 + 1): # this will count from 1 to 10
        if x == 5:
            continue

        print(x)

This fragment will print all the numbers from ``1`` to ``10`` *except* ``5``.  In the case where ``x`` is ``5``, the ``continue`` statement will be encountered, and the flow of control will leave that loop body -- but then the loop will *continue* with the next element in the range.

Note that if we replaced ``break`` with ``continue`` in the first example, we would get an infinite loop -- because the ``continue`` statement would be triggered before ``x`` could be updated. ``x`` would stay equal to ``5``, and keep triggering the ``continue`` statement, for ever!

.. Todo:: exercise

Using ``break`` to simulate a *do-while* loop
---------------------------------------------

Recall that a ``while`` loop checks the condition *before* executing the loop body for the first time.  Sometimes this is convenient, but sometimes it's not.  What if you always need to execute the loop body at least once? ::

    age = input("Please enter your age: ")
    while not valid_number(age): # let's assume that we've defined valid_number elsewhere
        age = input("Please enter your age: ")

We have to ask the user for input at least once, because the condition depends on the user input -- so we have to do it once outside the loop.  This is inconvenient, because we have to repeat the contents of the loop body -- and unnecessary repetition is usually a bad idea.  What if we want to change the message to the user later, and forget to change it in both places?  What if the loop body contains many lines of code?

Many other languages offer a structure called a *do-while* loop, or a *repeat-until* loop, which checks the condition *after* executing the loop body.  That means that the loop body will always be executed at least once.  Python doesn't have a structure like this, but we can simulate it with the help of the ``break`` statement::

    while True:
        age = input("Please enter your age: ")
        if valid_number(age):
            break

We have moved the condition *inside* the loop body, and we can check it at the end, *after* asking the user for input.  We have replaced the condition in the ``while`` statement with ``True`` -- which is, of course, always true.  Now the ``while`` statement  will *never* terminate after checking the condition -- it can *only* terminate if the ``break`` statement is triggered.

This trick can help us to make this particular loop use case look better, but it has its disadvantages.  If we accidentally leave out the ``break`` statement, or write the loop in such a way that it can never be triggered, we will have an infinite loop!  This code can also be more difficult to understand, because the actual condition which makes the loop terminate is hidden inside the body of the loop.  You should therefore use this construct sparingly.  Sometimes it's possible to rewrite the loop in such a way that the condition can be checked before the loop body *and* repetition is avoided::

    age = None # we can initialise age to something which is not a valid number
    while not valid_number(age): # now we can use the condition before asking the user anything
        age = input("Please enter your age: ")

List comprehensions
===================

.. Todo:: should the section about lists and dictionaries go earlier?

FROM ROUGH NOTES:

* The for statement
  * discuss differences between Python and C/Java/C++ for loops.

* The while statement

* Add section of looping pitfalls
  * not editing mutable sequences while you iterate over them.
  * infinite loops

* Do-while loops
  * Replace with mention of do-while in other languages and while True equivalent.

* The break and continue statements

* Add a section for list comprehensions
  * Potential replacement for some simple for loops.