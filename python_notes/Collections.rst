===========
Collections
===========

We have already encountered some simple Python types like numbers, strings and booleans.  Now we will see how we can group multiple values together in a *collection* -- like a *list* of numbers, or a *dictionary* which we can use to store and retrieve key-value pairs.  Many useful collections are built-in types in Python, and we will encounter them quite often.

Lists
=====

The Python list type is called ``list``.  It is a type of sequence -- we can use it to store multiple values, and access them sequentially, by their position, or *index*, in the list.  We define a list *literal* by putting a comma-separated list of values inside square brackets (``[`` and ``]``)::

    # a list of strings
    animals = ['cat', 'dog', 'fish', 'bison']

    # a list of integers
    numbers = [1, 7, 34, 20, 12]

    # an empty list
    my_list = []

    # a list of variables we defined somewhere else
    things = [
        one_variable,
        another_variable,
        third_variable, # this trailing comma is legal in Python
    ]

As you can see, we have used plural nouns to name most of our list variables.  This is a common convention, and it's useful to follow it in most cases.

To refer to an element in the list, we use the list identifier followed by the index inside square brackets.  Indices are integers which *start from zero*::

    print(animals[0]) # cat
    print(numbers[1]) # 7

    # This will give us an error, because the list only has four elements
    print(animals[6])

We can also count from the end::

    print(animals[-1]) # the last element -- bison
    print(numbers[-2]) # the second-last element -- 20

We can extract a subset of a list, which will itself be a list, using a *slice*.  This uses almost the same syntax as accessing a single element, but instead of specifying a single index between the square brackets we need to specify an upper and lower bound.   Note that our sublist will *include* the element at the lower bound, but *exclude* the element at the upper bound::

    print(animals[1:3]) # ['dog', 'fish']
    print(animals[1:-1]) # ['dog', 'fish']

If one of the bounds is one of the ends of the list, we can leave it out. A slice with neither bound specified gives us a copy of the list::

    print(animals[2:]) # ['fish', 'bison']
    print(animals[:2]) # ['cat', 'dog']
    print(animals[:]) # a copy of the whole list

We can even include a third parameter to specify the step size::

    print(animals[::2]) # ['cat', 'fish']

.. Todo:: include a diagram showing how to number list elements

Lists are mutable -- we can modify elements, add elements to them or remove elements from them.  A list will change size dynamically when we add or remove elements -- we don't have to manage this ourselves::

    # assign a new value to an existing element
    animals[3] = "hamster"

    # add a new element to the end of the list
    animals.append("squirrel")

    # remove an element by its index
    del animals[2]

Because lists are mutable, we can *modify* a list variable without assigning the variable a completely new value.  Remember that if we assign the same ``list`` value to two variables, any in-place changes that we make while referring to the list by one variable name will also be reflected when we access the list through the other variable name::

    animals = ['cat', 'dog', 'goldfish', 'canary']
    pets = animals # now both variables refer to the same list object

    animals.append('aardvark')
    print(pets) # pets is still the same list as animals

    animals = ['rat', 'gerbil', 'hamster'] # now we assign a new list value to animals
    print(pets) # pets still refers to the old list

    pets = animals[:] # assign a *copy* of animals to pets
    animals.append('aardvark')
    print(pets) # pets remains unchanged, because it refers to a copy, not the original list

We can mix the types of values that we store in a list::

    my_list = ['cat', 12, 35.8]

How do we check whether a list contains a particular value?  We use ``in`` or ``not in``, the membership operators::

    numbers = [34, 67, 12, 29]
    my_number = 67

    if number in numbers:
        print("%d is in the list!" % number)

    my_number = 90
    if number not in numbers:
        print("%d is not in the list!" % number)

.. Note:: ``in`` and ``not in`` fall between the logical operators (``and``, ``or`` and ``not``) and the identity operators (``is`` and ``is not``) in the order of precedence.

List methods and functions
--------------------------

There are many built-in functions which we can use on lists and other sequences::

    # the length of a list
    len(animals)

    # the sum of a list of numbers
    sum(numbers)

    # are any of these values true?
    any([1,0,1,0,1])

    # are all of these values true?
    all([1,0,1,0,1])

List objects also have useful methods which we can call::

    numbers = [1, 2, 3, 4, 5]

    # we already saw how to add an element to the end
    numbers.append(5)

    # count how many times a value appears in the list
    numbers.count(5)

    # append several values at once to the end
    numbers.extend([56, 2, 12])

    # find the index of a value
    numbers.index(3)
    # if the value appears more than once, we will get the index of the first one
    numbers.index(2)
    # if the value is not in the list, we will get a ValueError!
    numbers.index(42)

    # insert a value at a particular index
    numbers.insert(0, 45) # insert 45 at the beginning of the list

    # remove an element by its index and assign it to a variable
    my_number = numbers.pop(0)

    # remove an element by its value
    numbers.remove(12)
    # if the value appears more than once, only the first one will be removed
    numbers.remove(5)

If we want to sort or reverse a list, we can either call a method on the list to modify it *in-place*, or use a function to return a modified copy of the list while leaving the original list untouched::

    numbers = [3, 2, 4, 1]

    # these return a modified copy, which we can print
    print(sorted(numbers))
    print(list(reversed(numbers)))

    # the original list is unmodified
    print(numbers)

    # now we can modify it in place
    numbers.sort()
    numbers.reverse()

    print(numbers)

The ``reversed`` function actually returns a generator, not a list (we will look at generators in the next chapter), so we have to convert it to a list before we can print the contents.  To do this, we call the ``list`` type like a function, just like we would call ``int`` or ``float`` to convert numbers.  We can also use ``list`` as another way to make a copy of a list::

    animals = ['cat', 'dog', 'goldfish', 'canary']
    pets = list(animals)

    animals.sort()
    pets.append('gerbil')

    print(animals)
    print(pets)

Using arithmetic operators with lists
-------------------------------------

Some of the arithmetic operators we have used on numbers before can also be used on lists, but the effect may not always be what we expect::

    # we can concatenate two lists by adding them
    print([1, 2, 3] + [4, 5, 6])

    # we can concatenate a list with itself by multiplying it by an integer
    print([1, 2, 3] * 3)

    # not all arithmetic operators can be used on lists -- this will give us an error!
    print([1, 2, 3] - [2, 3])

Lists vs arrays
---------------

Many other languages don't have a built-in type which behaves like Python's list.  You can use an implementation from a library, or write your own, but often programmers who use these languages use *arrays* instead.  Arrays are simpler, more low-level data structures, which don't have all the functionality of a list.  Here are some major differences between lists and arrays:

* An array has a fixed size which you specify when you create it.  If you need to add or remove elements, you have to make a new array.
* If the language is statically typed, you also have to specify a single type for the values which you are going to put in the array when you create it.
* In languages which have *primitive types*, arrays are usually not objects, so they don't have any methods -- they are just containers.

Arrays are less easy to use in many ways, but they also have some advantages: because they are so simple, and there are so many restrictions on what you can do with them, the computer can handle them very efficiently. That means that it is often much faster to use an array than to use an object which behaves like a list.  A lot of programmers use them when it is important for their programs to be fast.

Python has a built-in ``array`` type.  It's not quite as restricting as an array in C or Java -- you have to specify a type for the contents of the array, and you can only use it to store numeric values, but you can resize it dynamically, like a list.  You will probably never need to use it.

Exercise 1
----------

#. Create a list ``a`` which contains the first three odd positive integers and a list ``b`` which contains the first three even positive integers.
#. Create a new list ``c`` which combines the numbers from both lists (order is unimportant).
#. Create a new list ``d`` which is a sorted copy of ``c``, leaving ``c`` unchanged.
#. Reverse ``d`` in-place.
#. Set the fourth element of ``c`` to ``42``.
#. Append ``10`` to the end of ``d``.
#. Append ``7``, ``8`` and ``9`` to the end of ``c``.
#. Print the first three elements of ``c``.
#. Print the last element of ``d`` without using its length.
#. Print the length of ``d``.

Tuples
======

Python has another sequence type which is called ``tuple``.  Tuples are similar to lists in many ways, but they are immutable.  We define a tuple *literal* by putting a comma-separated list of values inside round brackets (``(`` and ``)``)::

    WEEKDAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

We can use tuples in much the same way as we use lists, except that we can't modify them::

    animals = ('cat', 'dog', 'fish')

    # an empty tuple
    my_tuple = ()

    # we can access a single element
    print(animals[0])

    # we can get a slice
    print(animals[1:]) # note that our slice will be a new tuple, not a list

    # we can count values or look up an index
    animals.count('cat')
    animals.index('cat')

    # ... but this is not allowed:
    animals.append('canary')
    animal[1] = 'gerbil'

What are tuples good for?  We can use them to create a sequence of values that we don't want to modify.  For example, the list of weekday names is never going to change.  If we store it in a tuple, we can make sure it is never modified accidentally in an unexpected place::

    # Here's what can happen if we put our weekdays in a mutable list

    WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    def print_funny_weekday_list(weekdays):
        weekdays[5] = 'Caturday' # this is going to modify the original list!
        print(weekdays)

    print_funny_weekday_list(WEEKDAYS)

    print(WEEKDAYS) # oops

We have already been using tuples when inserting multiple values into a formatted string::

    print("%d %d %d" % (1, 2, 3))

How do we define a tuple with a single element?  We can't just put round brackets around a value, because round brackets are also used to change the order of precedence in an expression -- a value in brackets is just another way of writing the value::

    print(3)
    print((3)) # this is still just 3

To let Python know that we want to create a tuple, we have to add a trailing comma::

    print((3,))

Exercise 2
----------

#. Create a tuple ``a`` which contains the first four positive integers and a tuple ``b`` which contains the next four positive integers.
#. Create a tuple ``c`` which combines all the numbers from ``a`` and ``b`` in any order.
#. Create a tuple ``d`` which is a sorted copy of ``c``.
#. Print the third element of ``d``.
#. Print the last three elements of ``d`` without using its length.
#. Print the length of ``d``.

Sets
====

The Python set type is called ``set``.  A set is a collection of *unique elements*.  If we add multiple copies of the same element to a set, the duplicates will be eliminated, and we will be left with one of each element.  To define a set literal, we put a comma-separated list of values inside curly brackets (``{`` and ``}``)::

    animals = {'cat', 'dog', 'goldfish', 'canary', 'cat'}
    print(animals) # the set will only contain one cat

We can perform various set operations on sets::

    even_numbers = {2, 4, 6, 8, 10}
    big_numbers = {6, 7, 8, 9, 10}

    # subtraction: big numbers which are not even
    print(big_numbers - even_numbers)

    # union: numbers which are big or even
    print(big_numbers | even_numbers)

    # intersection: numbers which are big and even
    print(big_numbers & even_numbers)

    # numbers which are big or even but not both
    print(big_numbers ^ even_numbers)

It is important to note that unlike lists and tuples sets are *not ordered*.  When we print a set, the order of the elements will be random.  If we want to process the contents of a set in a particular order, we will first need to convert it to a list or tuple and sort it::

    print(animals)
    print(sorted(animals))

The ``sorted`` function returns a ``list`` object.

How do we make an empty set?  We have to use the ``set`` function.  Dictionaries, which we will discuss in the next section, used curly brackets before sets adopted them, so an empty set of curly brackets is actually an empty dictionary::

    # this is an empty dictionary
    a = {}

    # this is how we make an empty set
    b = set()

We can use the ``list``, ``tuple``, ``dict`` and even ``int``, ``float`` or ``str`` functions in the same way -- they all have sensible defaults -- but we will probably seldom find a reason to do so.

Exercise 3
----------

#. Create a set ``a`` which contains the first four positive integers and a set ``b`` which contains the first four odd positive integers.
#. Create a set ``c`` which combines all the numbers which are in ``a`` or ``b`` (or both).
#. Create a set ``d`` which contains all the numbers in ``a`` but not in ``b``.
#. Create a set ``e`` which contains all the numbers in ``b`` but not in ``a``.
#. Create a set ``f`` which contains all the numbers which are both in ``a`` and in ``b``.
#. Create a set ``g`` which contains all the numbers which are either in ``a`` or in ``b`` but not in both.
#. Print the number of elements in ``c``.

Ranges
======

``range`` is another kind of immutable sequence type. It is very specialised -- we use it to create ranges of integers.  Ranges are also *generators*.  We will find out more about generators in the next chapter, but for now we just need to know that the numbers in the range are generated one at a time as they are needed, and not all at once.  In the examples below, we convert each range to a list so that all the numbers are generated and we can print them out::

    # print the integers from 0 to 9
    print(list(range(10)))

    # print the integers from 1 to 10
    print(list(range(1, 11)))

    # print the odd integers from 1 to 10
    print(list(range(1, 11, 2)))

We create a range by calling the ``range`` function.  As you can see, if we pass a single parameter to the ``range`` function, it is used as the upper bound.  If we use two parameters, the first is the lower bound and the second is the upper bound.  If we use three, the third parameter is the step size.  The default lower bound is zero, and the default step size is one.  Note that the range *includes* the lower bound and *excludes* the upper bound.

Exercise 4
----------

#. Create a range ``a`` which starts from ``0`` and goes on for 20 numbers.
#. Create a range ``b`` which starts from ``3`` and ends on ``12``.
#. Create a range ``c`` which contains every third integer starting from ``2`` and ending at ``50``.

Dictionaries
============

.. Todo:: we need some kind of discussion of hashing and direct vs sequential access

The Python dictionary type is called ``dict``.  We can use a dictionary to store key-value pairs.  To define a dictionary literal, we put a comma-separated list of key-value pairs between curly brackets.  We use a colon to separate each key from its value.  We access values in the dictionary in much the same way as list or tuple elements, but we use keys instead of indices::

    marbles = {"red": 34, "green": 30, "brown": 31, "yellow": 29 }

    personal_details = {
        "name": "Jane Doe",
        "age": 38, # trailing comma is legal
    }

    print(marbles["green"])
    print(personal_details["name"])

    # This will give us an error, because there is no such key in the dictionary
    print(marbles["blue"])

    # modify a value
    marbles["red"] += 3
    personal_details["name"] = "Jane Q. Doe"

The keys of a dictionary don't have to be strings -- they can be *any immutable type*, including numbers and even tuples. We can mix different types of keys and different types of values in one dictionary.  Keys are unique -- if we repeat a key, we will overwrite the old value with the new value.  When we store a value in a dictionary, the key doesn't have to exist -- it will be created automatically::

    battleship_guesses = {
        (3, 4): False,
        (2, 6): True,
        (2, 5): True,
    }

    surnames = {} # this is an empty dictionary
    surnames["John"] = "Smith"
    surnames["John"] = "Doe"
    print(surnames) # we overwrote the older surname

    marbles = {"red": 34, "green": 30, "brown": 31, "yellow": 29 }
    marbles["blue"] = 30 # this will work
    marbles["purple"] += 2 # this will fail -- the increment operator needs an existing value to modify!

Like sets, dictionaries are not ordered -- if we print a dictionary, the order will be random.

Here are some commonly used methods of dictionary objects::

    marbles = {"red": 34, "green": 30, "brown": 31, "yellow": 29 }

    # Get a value by its key, or None if it doesn't exist
    marbles.get("orange")
    # We can specify a different default
    marbles.get("orange", 0)

    # Add several items to the dictionary at once
    marbles.update({"orange": 34, "blue": 23, "purple": 36})

    # All the keys in the dictionary
    marbles.keys()
    # All the values in the dictionary
    marbles.values()
    # All the items in the dictionary
    marbles.items()

The last three methods return special sequence types which are read-only *views* of various properties of the dictionary.  We cannot edit them directly, but they will be updated when we modify the dictionary.  We most often access these properties because we want to iterate over them (something we will discuss in the next chapter), but we can also convert them to other sequence types if we need to.

We can check if a key is in the dictionary using ``in`` and ``not in``::

    print("purple" in marbles)
    print("white" not in marbles)

We can also check if a value is in the dictionary using ``in`` in conjunction with the ``values`` method::

    print("Smith" in surnames.values())

You should avoid using ``mykey in mydict.keys()`` to check for key membership, however, because it's less efficient than ``mykey in mydict``.

.. Note:: in Python 2, ``keys``, ``values`` and ``items`` return list copies of these sequences, ``iterkeys``, ``itervalues`` and ``iteritems`` return iterator objects, and ``viewkeys``, ``viewvalues`` and ``viewitems`` return the view objects which are the default in Python 3 (but these are only available in Python 2.7 and above). In Python 2 you should *really* not use ``mykey in mydict.keys()`` to check for key membership -- if you do, you will be searching the entire list of keys sequentially, which is much slower than a direct dictionary lookup.

Exercise 5
----------

#. Create a dict ``directory`` which stores telephone numbers (as string values), and populate it with these key-value pairs:

   ==========  ================
   Name        Telephone number
   ==========  ================
   Jane Doe    +27 555 5367
   John Smith  +27 555 6254
   Bob Stone   +27 555 5689
   ==========  ================

#. Change Jane's number to *+27 555 1024*
#. Add a new entry for a person called *Anna Cooper* with the phone number *+27 555 3237*
#. Print Bob's number.
#. Print Bob's number in such a way that ``None`` would be printed if Bob's name were not in the dictionary.
#. Print all the keys. The format is unimportant, as long as they're all visible.
#. Print all the values.

Converting between collection types
===================================

Implicit conversions
--------------------

If we try to iterate over a collection in a ``for`` loop (something we will discuss in the next chapter), Python will try to convert it into something that we can iterate over if it knows how to.  For example, the dictionary views we saw above are not actually iterators, but Python knows how to make them into iterators -- so we can use them in a ``for`` loop without having to convert them ourselves.

Sometimes the iterator we get by default may not be what we expected -- if we iterate over a dictionary in a ``for`` loop, we will iterate over the *keys*.  If what we actually want to do is iterate over the values, or key and value pairs, we will have to specify that ourselves by using the dictionary's ``values`` or ``items`` view instead.

.. Todo:: I'm not convinced that there's any point to having this subsection here. Maybe this should be mentioned in the loop chapter. "Iteration" isn't even defined here.

Explicit conversions
--------------------

We can convert between the different sequence types quite easily by using the type functions to *cast* sequences to the desired types -- just like we would use ``float`` and ``int`` to convert numbers::

    animals = ['cat', 'dog', 'goldfish', 'canary', 'cat']

    animals_set = set(animals)
    animals_unique_list = list(animals_set)
    animals_unique_tuple = tuple(animals_unique_list)

We have to be more careful when converting a dictionary to a sequence: do we want to use the keys, the values or pairs of keys and values? ::

    marbles = {"red": 34, "green": 30, "brown": 31, "yellow": 29 }

    colours = list(marbles) # the keys will be used by default
    counts = tuple(marbles.values()) # but we can use a view to get the values
    marbles_set = set(marbles.items()) # or the key-value pairs

If we convert the key-value pairs of a dictionary to a sequence, each pair will be converted to a tuple containing the key followed by the value.

We can also convert a sequence to a dictionary, but only if it's a sequence of *pairs* -- each pair must itself be a sequence with two values::

    # Python doesn't know how to convert this into a dictionary
    dict([1, 2, 3, 4])

    # but this will work
    dict([(1, 2), (3, 4)])

We will revisit conversions in the next chapter, when we learn about *comprehensions* -- an efficient syntax for filtering sequences or dictionaries.  By using the right kind of comprehension, we can filter a collection and convert it to a different type of collection at the same time.

Another look at strings
-----------------------

Strings are also a kind of sequence type -- they are sequences of characters, and share some properties with other sequences.  For example, we can find the length of a string or the index of a character in the string, and we can access individual elements of strings or slices::

    s = "abracadabra"

    print(len(s))
    print(s.index("a"))

    print(s[0])
    print(s[3:5])

Remember that strings are immutable -- modifying characters in-place isn't allowed::

    # this will give us an error
    s[0] = "b"

The membership operator has special behaviour when applied to strings: we can use it to determine if a string contains a single character as an element, but we can also use it to check if a string contains a substring::

    print('a' in 'abcd') # True
    print('ab' in 'abcd') # also True

    # this doesn't work for lists
    print(['a', 'b'] in ['a', 'b', 'c', 'd']) # False

We can easily convert a string to a list of characters::

    abc_list = list("abracadabra")

What if we want to convert a list of characters into a string? Using the ``str`` function on the list will just give us a printable string of the list, including commas, quotes and brackets.  To join a sequence of characters (or longer strings) together into a single string, we have to use ``join``.

``join`` is not a function or a sequence method -- it's a *string* method which takes a sequence of strings as a parameter.  When we call a string's ``join`` method, we are using that string to glue the strings in the sequence together.  For example, to join a list of single characters into a string, with no spaces between them, we call the ``join`` method on the *empty string*::

    l = ['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a']

    s = "".join(l)
    print(s)

We can use any string we like to join a sequence of strings together::

    animals = ('cat', 'dog', 'fish')

    # a space-separated list
    print(" ".join(animals))

    # a comma-separated list
    print(",".join(animals))

    # a comma-separated list with spaces
    print(", ".join(animals))

The opposite of *joining* is *splitting*.  We can split up a string into a list of strings by using the ``split`` method.  If called without any parameters, ``split`` divides up a string into words, using any number of consecutive whitespace characters as a delimiter.  We can use additional parameters to specify a different delimiter as well as a limit on the maximum number of splits to perform::

    print("cat    dog fish\n".split())
    print("cat|dog|fish".split("|"))
    print("cat, dog, fish".split(", "))
    print("cat, dog, fish".split(", ", 1))

Exercise 6
----------

#. Convert a list which contains the numbers ``1``, ``1``, ``2``, ``3`` and ``3``, and convert it to a tuple ``a``.
#. Convert ``a`` to a list ``b``. Print its length.
#. Convert ``b`` to a set ``c``. Print its length.
#. Convert ``c`` to a list ``d``. Print its length.
#. Create a range which starts at ``1`` and ends at ``10``. Convert it to a list ``e``.
#. Create the ``directory`` dict from the previous example. Create a list ``t`` which contains all the key-value pairs from the dictionary as tuples.
#. Create a list ``v`` of all the values in the dictionary.
#. Create a list ``k`` of all the keys in he dictionary.
#. Create a string ``s`` which contains the word ``"antidisestablishmentarianism"``. Use the ``sorted`` function on it. What is the output type? Concatenate the letters in the output to a string ``s2``.
#. Split the string ``"the quick brown fox jumped over the lazy dog"`` into a list ``w`` of individual words.

Two-dimensional sequences
=========================

Most of the sequences we have seen so far have been one-dimensional: each sequence is a row of elements.  What if we want to use a sequence to represent a two-dimensional data structure, which has both rows and columns?  The easiest way to do this is to make a sequence in which each element is also a sequence.  For example, we can create a list of lists::

    my_table = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12],
    ]

The outer list has four elements, and each of these elements is a list with three elements (which are numbers).  To access one of these numbers, we need to use two indices -- one for the outer list, and one for the inner list::

    print(my_table[0][0])

    # lists are mutable, so we can do this
    my_table[0][0] = 42

We have already seen an example of this in the previous chapter, when we created a list of tuples to convert into a dict.

When we use a two-dimensional sequence to represent tabular data, each inner sequence will have the same length, because a table is rectangular -- but nothing is stopping us from constructing two-dimensional sequences which don't have this property::

    my_2d_list = [
        [0],
        [1, 2, 3, 4],
        [5, 6],
    ]

We can also make a three-dimensional sequence by making a list of lists of lists::

    my_3d_list = [
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]],
    ]

    print(my_3d_list[0][0][0])

Of course we can also make a list of lists of lists of lists and so forth -- we can nest lists as many times as we like.

If we wanted to make a two-dimensional list to represent a weekly timetable, we could either have days as the outer list and time slots as the inner list or the other way around -- we would have to remember which range we picked to be the rows and which the columns.

Suppose that we wanted to initialise the timetable with an empty string in each time slot -- let us say that we have 24 hour-long time slots in each day.  That's seven lists of 24 elements each -- quite long and unwieldy to define using literals, the way we defined the smaller lists in the examples above!

This brings us to a common pitfall.  You may recall from a previous section that we can use the multiplication operator on lists -- this can be a convenient way to construct a long list in which all the elements are the same::

    my_long_list = [0] * 100 # a long list of zeros
    print(my_long_list)

You might think of using this method to construct our timetable.  We can certainly use it to create a list of empty strings to represent a day::

    day = [""] * 24
    print(day)

But what happens if we repeat a day seven times to make a week? ::

    timetable = day * 7
    print(timetable)

Everything looks fine so far, so what's the problem?  Well, let's see what happens when we try to schedule a meeting for Monday afternoon::

    timetable[0][15] = "meeting with Jane"
    print(timetable)

Every day has the same afternoon meeting!  How did that happen?  When we multiplied our day list by seven, we filled our timetable with *the same list object*, repeated seven times.  All the elements in our timetable are the same day, so no matter which one we modify we modify all of them at once.

Why didn't this matter when we made the day list by multiplying the same empty string 24 times?  Because strings are immutable.  We can only change the values of the strings in the day list by assigning them new values -- we can't modify them in-place, so it doesn't matter that they all start off as the same string object.  But because we *can* modify lists in-place, it does matter that all our day lists are the same list.  What we actually want is seven *copies* of a day list in our timetable::

    timetable = [[""] * 24 for day in range(7)]

Here we construct the timetable with a list comprehension instead.  We will learn more about comprehensions in the next chapter -- for now, it is important for us to know that this method creates a *new* list of empty strings for each day, unlike the multiplication operator.

Exercise 7
----------

#. Create a list ``a`` which contains three tuples. The first tuple should contain a single element, the second two elements and the third three elements.
#. Print the second element of the second element of ``a``.
#. Create a list ``b`` which contains four lists, each of which contains four elements.
#. Print the last two elements of the first element of ``b``.

Answers to exercises
====================

Answer to exercise 1
--------------------

::

    a = [1, 3, 5]
    b = [2, 4, 6]

    c = a + b

    d = sorted(c)
    d.reverse()

    c[3] = 42
    d.append(10)
    d.extend([7, 8, 9])

    print(c[:2])
    print(d[-1])
    print(len(d))

Answer to exercise 2
--------------------

::

    a = (1, 2, 3, 4)
    b = (5, 6, 7, 8)

    c = a + b
    d = sorted(c)

    print(d[3])
    print(d[-3:])
    print(len(d))

Answer to exercise 3
--------------------

::

    a = {1, 2, 3, 4}
    b = {1, 3, 5, 7}

    c = a | b
    d = a - b
    e = b - a
    f = a & b
    g = a ^ b

    print(len(c))

Answer to exercise 4
--------------------

::

    a = range(20)
    b = range(3, 13)
    c = range(2, 51, 3)

Answer to exercise 5
--------------------

::

    directory = {
        "Jane Doe": "+27 555 5367",
        "John Smith": "+27 555 6254",
        "Bob Stone": "+27 555 5689",
    }

    directory["Jane Doe"] = "+27 555 1024"
    directory["Anna Cooper"] = "+27 555 3237"

    print(directory["Bob Stone"])
    print(directory.get("Bob Stone", None))

    print(directory.keys())
    print(directory.values())

Answer to exercise 6
--------------------

::

    a = tuple([1, 1, 2, 3, 3])

    b = list(a)
    print(len(b))

    c = set(b)
    print(len(c))

    d = list(c)
    print(len(d))

    e = list(range(1, 11))

    directory = {
        "Jane Doe": "+27 555 5367",
        "John Smith": "+27 555 6254",
        "Bob Stone": "+27 555 5689",
    }

    t = list(directory.items())
    v = list(directory.values())
    k = list(directory)

    s = "antidisestablishmentarianism"
    s2 = "".join(sorted(s))

    w = "the quick brown fox jumped over the lazy dog".split()

Answer to exercise 7
--------------------

Here is a code example::

    a = [
        (1,),
        (2, 2),
        (3, 3, 3),
    ]

    print(a[1][1])

    b = [
        list(range(10)),
        list(range(10, 20)),
        list(range(20, 30)),
        list(range(30, 40)),
    ]

    print(b[0][1:-1])
