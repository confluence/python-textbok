***********************
Loop control statements
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

Exercise 1
----------

#. Write a program which uses a ``while`` loop to sum the squares of integers (starting from ``1``) until the total exceeds 200.  Print the final total and the last number to be squared and added.

#. Write a program which keeps prompting the user to guess a word.  The user is allowed up to ten guesses -- write your code in such a way that the secret word and the number of allowed guesses are easy to change.  Print messages to give the user feedback.

The ``for`` statement
=====================

Python's other loop statement is the ``for`` statement.  You should use it when you need to do something for some predefined number of steps.  Before we look at Python's ``for`` loop syntax, we will briefly look at the way *for* loops work in other languages.

Here is an example of a *for* loop in Java::

    for (int count = 1; count <= 8; count++) {
        System.out.println(count);
    }

You can see that this kind of *for* loop has a lot in common with a *while* loop -- in fact, you could say that it's just a special case of a *while* loop.  The initialisation step, the condition and the update step are all defined in the section in parentheses on the first line.

*for* loops are often used to perform an operation on every element of some kind of sequence. If you wanted to iterate over a list using the classic-style *for* loop, you would have to count from zero to the end of the list, and then access each list element by its index.

In Python, ``for`` loops make this use case simple and easy by allowing you to iterate over sequences directly.  Here is an example of a ``for`` statement which counts from 1 to 8::

    for i in range(1, 9):
        print(i)

As we saw in the previous chapter, ``range`` is an immutable sequence type used for ranges of integers -- in this case, the range is counting from ``1`` to ``8``. The ``for`` loop will step through each of the numbers in turn, performing the print action for each one.  When the end of the range is reached, the ``for`` loop will exit.

You can use ``for`` to iterate over other kinds of sequences too.  You can iterate over a list of strings like this::

    pets = ["cat", "dog", "budgie"]

    for pet in pets:
        print(pet)

At each iteration of the loop, the next element of the list ``pets`` is assigned to the variable ``pet``, which you can then access inside the loop body.  The example above is functionally identical to this::

    for i in range(len(pets)): # i will iterate over 0, 1 and 2
        pet = pets[i]
        print(pet)

That is similar to the way ``for`` loops are written in, for example, Java.  You should avoid doing this, as it's more difficult to read, and unnecessarily complex.  If for some reason you need the index inside the loop as well as the list element itself, you can use the ``enumerate`` function to number the elements::

    for i, pet in enumerate(pets):
        pets[i] = pet.upper() # rewrite the list in all caps

Like ``range``, ``enumerate`` also returns an iterator -- each item it generates is a tuple in which the first value is the index of the element (starting at zero) and the second is the element itself. In the loop above, at each iteration the value of the index is assigned to the variable ``i``, and the element is assigned to the variable ``pet``, as before.

Why couldn't we just write ``pet = pet.upper()``?  That would just assign a new value to the variable ``pet`` inside the loop, without changing the original list.

This brings us to a common ``for`` loop pitfall: modifying a list while you're iterating over it.  The example above only modifies elements in-place, and doesn't change their order around, but you can cause all kinds of errors and unintended behaviour if you insert or delete list elements in the middle of iteration::

    numbers = [1, 2, 2, 3]

    for i, num in enumerate(numbers):
        if num == 2:
            del numbers[i]

    print(numbers) # oops -- we missed one, because we shifted the elements around while we were iterating!

Sometimes you can avoid this by iterating over a *copy* of the list instead, but it won't help you in this case -- as you delete elements from the original list, it will shrink, so the indices from the unmodified list copy will soon exceed the length of the modified list and you will get an error.  In general, if you want to select a subset of elements from a list on the basis of some criterion, you should use a *list comprehension* instead. We will look at them at the end of this chapter.

Exercise 2
----------

#. Write a program which sums the integers from 1 to 10 using a ``for`` loop (and prints the total at the end).

#. Can you think of a way to do this without using a loop?

#. Write a program which finds the factorial of a given number. E.g. 3 factorial, or **3!** is equal to **3 x 2 x 1**; **5!** is equal to **5 x 4 x 3 x 2 x 1**, etc.. Your program should only contain a single loop.

#. Write a program which prompts the user for 10 floating-point numbers and calculates their sum, product and average. Your program should only contain a single loop.

#. Rewrite the previous program so that it has two loops -- one which collects and stores the numbers, and one which processes them.

Nested loops
============

We saw in the previous chapter that we can create multi-dimensional sequences -- sequences in which each element is another sequence.  How do we iterate over all the values of a multi-dimensional sequence?  We need to use loops inside other loops.  When we do this, we say that we are *nesting* loops.

Consider the timetable example from the previous chapter -- let us say that the timetable contains seven days, and each day contains 24 time slots.  Each time slot is a string, which is empty if there is nothing scheduled for that slot.  How can we iterate over all the time slots and print out all our scheduled events? ::

    # first let's define weekday names
    WEEKDAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

    # now we iterate over each day in the timetable
    for day in timetable:
        # and over each timeslot in each day
        for i, event in enumerate(day):
            if event: # if the slot is not an empty string
                print("%s at %02d:00 -- %s" % (WEEKDAYS[day], i, event))

Note that we have two ``for`` loops -- the inner loop will be executed once for every step in the outer loop's iteration.  Also note that we are using the ``enumerate`` function when iterating over the days -- because we need both the index of each time slot (so that we can print the hour) and the contents of that slot.

You may have noticed that we look up the name of the weekday once for every iteration of the inner loop -- but the name only changes once for every iteration of the outer loop.  We can make our loop a little more efficient by moving this lookup out of the inner loop, so that we only perform it seven times and not 168 times! ::

        for day in timetable:
            day_name = WEEKDAYS[day]
            for i, event in enumerate(day):
                if event:
                    print("%s at %02d:00 -- %s" % (day_name, i, event))

This doesn't make much difference when you are looking up a value in a short tuple, but it could make a big difference if it were an expensive, time-consuming calculation and you were iterating over hundreds or thousands of values.

Exercise 3
----------

#. Write a program which uses a nested ``for`` loop to populate a three-dimensional list representing a calendar: the top-level list should contain a sub-list for each month, and each month should contain four weeks.  Each week should be an empty list.

#. Modify your code to make it easier to access a month in the calendar by a human-readable month name, and each week by a name which is numbered starting from 1.  Add an event (in the form of a string description) to the second week in July.

Iterables, iterators and generators
===================================

In Python, any type which can be iterated over with a ``for`` loop is an *iterable*.  Lists, tuples, strings and dicts are all commonly used iterable types.  Iterating over a list or a tuple simply means processing each value in turn.

Sometimes we use a sequence to store a series of values which don't follow any particular pattern: each value is unpredictable, and can't be calculated on the fly.  In cases like this, we have no choice but to store each value in a list or tuple.  If the list is very large, this can use up a lot of memory.

What if the values in our sequence *do* follow a pattern, and *can* be calculated on the fly?  We can save a lot of memory by calculating values only when we need them, instead of calculating them all up-front: instead of storing a big list, we can store only the information we need for the calculation.

Python has a lot of built-in iterable types that generate values on demand -- they are often referred to as *generators*.  We have already seen some examples, like ``range`` and ``enumerate``.  You can mostly treat a generator just like any other sequence if you only need to access its elements one at a time -- for example, if you use it in a ``for`` loop::

    # These two loops will do exactly the same thing:

    for i in (1, 2, 3, 4, 5):
        print(i)

    for i in range(1, 6):
        print(i)

You may notice a difference if you try to print out the generator's contents -- by default all you will get is Python's standard string representation of the object, which shows you the object's type and its unique identifier.  To print out all the values of generator, we need to convert it to a sequence type like a list, which will force all of the values to be generated::

    # this will not be very helpful
    print(range(100))

    # this will show you all the generated values
    print(list(range(100)))

You can use all these iterables almost interchangeably because they all use the same interface for iterating over values: every *iterable* object has a method which can be used to return an *iterator* over that object.  The iterable and the iterator together form a consistent interface which can be used to loop over a sequence of values -- whether those values are all stored in memory or calculated as they are needed:

* The *iterable* has a method for accessing an item by its index.  For example, a list just returns the item which is stored in a particular position.  A range, on the other hand, *calculates* the integer in the range which corresponds to a particular index.

* The *iterator* "keeps your place" in the sequence, and has a method which lets you access the next element.  There can be multiple iterators associated with a single iterable at the same time -- each one in a different place in the iteration.  For example, you can iterate over the same list in both levels of a nested loop -- each loop uses its own *iterator*, and they do not interfere with each other::

    animals = ['cat', 'dog', 'fish']

    for first_animal in animals:
        for second_animal in animals:
            print("Yesterday I bought a %s. Today I bought a %s." % (first_animal, second_animal))

We will look in more detail at how these methods are defined in a later chapter, when we discuss writing custom objects.  For now, here are some more examples of built-in generators defined in Python's ``itertools`` module::

    # we need to import the module in order to use it
    import itertools

    # unlike range, count doesn't have an upper bound, and is not restricted to integers
    for i in itertools.count(1):
        print(i) # 1, 2, 3....

    for i in itertools.count(1, 0.5):
        print(i) # 1.0, 1.5, 2.0....

    # cycle repeats the values in another iterable over and over
    for animal in itertools.cycle(['cat', 'dog']):
        print(animal) # 'cat', 'dog', 'cat', 'dog'...

    # repeat repeats a single item
    for i in itertools.repeat(1): # ...forever
        print(i) # 1, 1, 1....

    for i in itertools.repeat(1, 3): # or a set number of times
        print(i) # 1, 1, 1

    # chain combines multiple iterables sequentially
    for i in itertools.chain(numbers, animals):
        print(i) # print all the numbers and then all the animals

Some of these generators can go on for ever, so if you use them in a ``for`` loop you will need some other check to make the loop terminate!

There is also a built-in function called ``zip`` which allows us to combine multiple iterables pairwise. It also outputs a generator::

    for i in zip((1, 2, 3), (4, 5, 6)):
        print(i)

    for i in zip(range(5), range(5, 10), range(10, 15)):
        print(i)

The combined iterable will be the same length as the shortest of the component iterables -- if any of the component iterables are longer than that, their trailing elements will be discarded.

Exercise 4
----------

#. Create a tuple of month names and a tuple of the number of days in each month (assume that February has 28 days). Using a single ``for`` loop, construct a dictionary which has the month names as keys and the corresponding day numbers as values.

#. Now do the same thing without using a ``for`` loop.

Comprehensions
==============

Suppose that we have a list of numbers, and we want to build a new list by doubling all the values in the first list.  Or that we want to extract all the even numbers from a list of numbers.  Or that we want to find and capitalise all the animal names in a list of animal names that start with a vowel.  We can do each of these things by iterating over the original list, performing some kind of check on each element in turn, and appending values to a new list as we go::

    numbers = [1, 5, 2, 12, 14, 7, 18]

    doubles = []
    for number in numbers:
        doubles.append(2 * number)

    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    animals = ['aardvark', 'cat', 'dog', 'opossum']

    vowel_animals = []
    for animal in animals:
        if animal[0] in 'aeiou':
            vowel_animals.append(animal.title())

That's quite an unwieldy way to do something very simple.  Fortunately, we can rewrite simple loops like this to use a cleaner and more readable syntax by using *comprehensions*.

A comprehension is a kind of filter which we can define on an iterable based on some condition.  The result is another iterable.  Here are some examples of list comprehensions::

    doubles = [2 * number for number in numbers]
    even_numbers = [number for number in numbers if number % 2 == 0]
    vowel_animals = [animal.title() for animal in animals if animal[0] in 'aeiou']

The comprehension is the part written between square brackets on each line.  Each of these comprehensions results in the creation of a new ``list`` object.

You can think of the comprehension as a compact form of ``for`` loop, which has been rearranged slightly.

* The first part (``2 * number`` or ``number`` or ``animal.title()``) defines what is going to be inserted into the new list at each step of the loop.  This is usually some function of each item in the original iterable as it is processed.
* The middle part (``for number in numbers`` or ``for animal in animals``) corresponds to the first line of a ``for`` loop, and defines what iterable is being iterated over and what variable name each item is given inside the loop.
* The last part (nothing or ``if number % 2 == 0`` or ``if animal[0] in 'aeiou'``) is a condition which filters out some of the original items.  Only items for which the condition is true will be processed (as described in the first part) and included in the new list.  You don't have to include this part -- in the first example, we want to double *all* the numbers in the original list.

List comprehensions can be used to replace loops that are a lot more complicated than this -- even nested loops.  The more complex the loop, the more complicated the corresponding list comprehension is likely to be.  A long and convoluted list comprehension can be very difficult for someone reading your code to understand -- sometimes it's better just to write the loop out in full.

The final product of a comprehension doesn't have to be a list.  You can create dictionaries or generators in a very similar way -- a generator expression uses round brackets instead of square brackets, a set comprehension uses curly brackets, and a dict comprehension uses curly brackets *and* separates the key and the value using a colon::

    numbers = [1, 5, 2, 12, 14, 7, 18]

    # a generator comprehension
    doubles_generator = (2 * number for number in numbers)

    # a set comprehension
    doubles_set = {2 * number for number in numbers}

    # a dict comprehension which uses the number as the key and the doubled number as the value
    doubles_dict = {number: 2 * number for number in numbers}

If your generator expression is a parameter being passed to a function, like ``sum``, you can leave the round brackets out::

    sum_doubles = sum(2 * number for number in numbers)

.. Note:: dict and set comprehensions were introduced in Python 3.  In Python 2 you have to create a list or generator instead and convert it to a set or a dict yourself.

Exercise 5
----------

#. Create a string which contains the first ten positive integers separated by commas and spaces. Remember that you can't join numbers -- you have to convert them to strings first.  Print the output string.

#. Rewrite the calendar program from exercise 3 using nested comprehensions instead of nested loops.  Try to append a string to one of the week lists, to make sure that you haven't reused the same list instead of creating a separate list for each week.

#. Now do something similar to create a calendar which is a list with 52 empty sublists (one for each week in the whole year). Hint: how would you modify the nested ``for`` loops?

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

Exercise 6
----------

#. Write a program which repeatedly prompts the user for an integer. If the integer is even, print the integer. If the integer is odd, don't print anything. Exit the program if the user enters the integer ``99``.

#. Some programs ask the user to input a variable number of data entries, and finally to enter a specific character or string (called a *sentinel*) which signifies that there are no more entries.  For example, you could be asked to enter your PIN followed by a hash (``#``). The hash is the sentinel which indicates that you have finished entering your PIN.

   Write a program which averages positive integers.  Your program should prompt the user to enter integers until the user enters a negative integer.  The negative integer should be discarded, and you should print the average of all the previously entered integers.

#. Implement a simple calculator with a menu.  Display the following options to the user, prompt for a selection, and carry out the requested action (e.g. prompt for two numbers and add them).  After each operation, return the user to the menu. Exit the program when the user selects ``0``. If the user enters a number which is not in the menu, ignore the input and redisplay the menu. You can assume that the user will enter a valid integer::

    -- Calculator Menu --
    0. Quit
    1. Add two numbers
    2. Subtract two numbers
    3. Multiply two numbers
    4. Divide two numbers

Using loops to simplify code
----------------------------

We can use our knowledge of loops to simplify some kinds of redundant code.  Consider this example, in which we prompt a user for some personal details::

    name = input("Please enter your name: ")
    surname = input("Please enter your surname: ")
    # let's store these as strings for now, and convert them to numbers later
    age = input("Please enter your age: ")
    height = input("Please enter your height: ")
    weight = input("Please enter your weight: ")

There's a lot of repetition in this snippet of code.  Each line is exactly the same except for the name of the variable and the name of the property we ask for (and these values match each other, so there's really only one difference).  When we write code like this we're likely to do a lot of copying and pasting, and it's easy to make a mistake.  If we ever want to change something, we'll need to change each line.

How can we improve on this?  We can separate the parts of these lines that differ from the parts that don't, and use a loop to iterate over them.  Instead of storing the user input in separate variables, we are going to use a dictionary -- we can easily use the property names as keys, and it's a sensible way to group these values::

    person = {}

    for prop in ["name", "surname", "age", "height", "weight"]:
        person[prop] = input("Please enter your %s: " % prop)

Now there is no unnecessary duplication.  We can easily change the string that we use as a prompt, or add more code to execute for each property -- we will only have to edit the code in one place, not in five places.  To add another property, all we have to do is add another name to the list.

Exercise 7
----------

#. Modify the example above to include type conversion of the properties: age should be an integer, height and weight should be floats, and name and surname should be strings.

.. Todo:: change you to we almost everywhere

Answers to exercises
====================

Answer to exercise 1
--------------------

#. Here is an example program::

    total = 0
    number = 0

    while total < 200:
        number += 1
        total += number**2

    print("Total: %d" % total)
    print("Last number: %d" % number)

#. Here is an example program::

    GUESSES_ALLOWED = 10
    SECRET_WORD = "caribou"

    guesses_left = GUESSES_ALLOWED
    guessed_word = None

    while guessed_word != SECRET_WORD and guesses_left:
        guessed_word = input("Guess a word: ")

        if guessed_word == SECRET_WORD:
            print("You guessed! Congratulations!")
        else:
            guesses_left -= 1
            print("Incorrect! You have %d guesses left." % guesses_left)

Answer to exercise 2
--------------------

#. Here is an example program::

    total = 0

    for i in range(1, 10 + 1):
        total += i

    print(total)

#. Remember that we can use the ``sum`` function to sum a sequence::

    print(sum(range(1, 10 + 1)))

#. Here is an example program::

    num = int(input("Please enter an integer: "))

    num_fac = 1
    for i in range(1, num + 1):
        num_fac *= i

    print("%d! = %d" % (num, num_fac))

#. Here is an example program::

    total = 0
    product = 1

    for i in range(1, 10 + 1):
        num = float(input("Please enter number %d: " % i))
        total += num
        product *= num

    average = total/10

    print("Sum: %g\nProduct: %g\nAverage: %g" % (total, product, average))

#. Here is an example program::

    numbers = []

    for i in range(10):
        numbers[i] = float(input("Please enter number %d: " % (i + 1)))

    total = 0
    product = 1

    for num in numbers:
        total += num
        product *= num

    average = total/10

    print("Sum: %g\nProduct: %g\nAverage: %g" % (total, product, average))

Answer to exercise 3
--------------------

#. Here is an example program::

    calendar = []

    for m in range(12):
        month = []

        for w in range(4):
            month.append([])

        calendar.append(month)

#. Here is an example program::

    (JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST,
    SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER) = range(12)

    (WEEK_1, WEEK_2, WEEK_3, WEEK_4) = range(4)

    calendar[JULY][WEEK_2].append("Go on holiday!")

Answer to exercise 4
--------------------

#. Here is an example program::

    months = ("January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October",
              "November", "December")

    num_days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    month_dict = {}

    for month, days in zip(months, days):
        month_dict[month] = days

#. Here is an example program::

    months = ("January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October",
              "November", "December")

    num_days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    # the zipped output is a sequence of two-element tuples,
    # so we can just use a dict conversion.
    month_dict = dict(zip(months, days))

Answer to exercise 5
--------------------

#. Here is an example program::

    number_string = ", ".join(str(n) for n in range(1, 11))
    print(number_string)


#. Here is an example program::

    calendar = [[[] for w in range(4)] for m in range(12)]

    (JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST,
    SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER) = range(12)

    (WEEK_1, WEEK_2, WEEK_3, WEEK_4) = range(4)

    calendar[JULY][WEEK_2].append("Go on holiday!")

#. ::

    calendar = [[] for w in range(4) for m in range(12)]

Answer to exercise 6
--------------------

#. Here is an example program::

    while (True):
        num = int(input("Enter an integer: "))
        if num == 99:
            break
        if num % 2:
            continue
        print num

#. Here is an example program::

    print("Please enter positive integers to be averaged. Enter a negative integer to terminate the list.")

    nums = []

    while True:
        num = int(input("Enter a number: "))

        if num < 0:
            break

        nums.append(num)

    average = float(sum(nums))/len(nums)
    print("average = %g" % average)

#. Here is an example program::

    menu = """-- Calculator Menu --
    0. Quit
    1. Add two numbers
    2. Subtract two numbers
    3. Multiply two numbers
    4. Divide two numbers"""

    selection = None

    while selection != 0:
        print(menu)
        selection = int(input("Select an option: "))

        if selection not in range(5):
            print("Invalid option: %d" % selection)
            continue

        if selection == 0:
            continue

        a = float(input("Please enter the first number: "))
        b = float(input("Please enter the second number: "))

        if selection == 1:
            result = a + b
        elif selection == 2:
            result = a - b
        elif selection == 3:
            result = a * b
        elif selection == 4:
            result = a / b

        print("The result is %g." % result)

Answer to exercise 7
--------------------

#. Here is an example program::

    person = {}

    properties = [
        ("name", str),
        ("surname", str),
        ("age", int),
        ("height", float),
        ("weight", float),
    ]

    for prop, p_type in properties:
        person[prop] = p_type(input("Please enter your %s: " % prop))
