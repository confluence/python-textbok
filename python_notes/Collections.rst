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

To refer to an element in the list, we use the list identifier followed by the index inside square brackets.  Indices are integers which start from zero::

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

We can mix the types of values that you store in a list::

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

There are many built-in functions which you can use on lists and other sequences::

    # the length of a list
    len(animals)

    # the sum of a list of numbers
    sum(numbers)

    # are any of these values true?
    any([1,0,1,0,1])

    # are all of these values true?
    all([1,0,1,0,1])

List objects also have methods which you can call::

    numbers = [1, 2, 3, 4, 5]

    # we already saw how to add an element to the end
    numbers.append(5)

    # count how many times a value appears in the list
    numbers.count(5)

    # append several values at once to the end
    numbers.extend([56, 2, 12])

    # find the index of a value
    numbers.index(3)
    # if the value appears more than once, you will get the index of the first one
    numbers.index(2)
    # if the value is not in the list, you will get a ValueError!
    numbers.index(42)

    # insert a value at a particular index
    numbers.insert(0, 45) # insert 45 at the beginning of the list

    # remove an element by its index and assign it to a variable
    my_number = numbers.pop(0)

    # remove an element by its value
    numbers.remove(12)
    # if the value appears more than once, only the first one will be removed
    numbers.remove(5)

If you want to sort or reverse a list, you can either call a method on the list to modify in *in-place*, or use a function to return a modified copy of the list while leaving the original list untouched::

    numbers = [3, 2, 4, 1]

    # these return a modified copy, which we can print
    print(sorted(numbers))
    print(list(reversed(numbers))

    # the original list is unmodified
    print(numbers)

    # now we can modify it in place
    numbers.sort()
    numbers.reverse()

    print(numbers)

The ``reversed`` function actually returns an iterator object, not a list (we will look at iterators later in this chapter), so we have to convert it to a list before we can print the contents.  To do this, we call the ``list`` type like a function, just like we would call ``int`` or ``float`` to convert numbers.  We can also use ``list`` as another way to make a copy of a list::

    animals = ['cat', 'dog', 'goldfish', 'canary']
    pets = list(animals)

    animals.sort()
    pets.append('gerbil')

    print(animals)
    print(pets)

Lists vs arrays
---------------

Many other languages don't have a built-in type which behaves like Python's list.  You can use an implementation from a library, or write your own, but often programmers who use these languages use *arrays* instead.  Arrays are simpler, more low-level data structures, which don't have all the functionality of a list.  Here are some major differences between lists and arrays:

* An array has a fixed size which you specify when you create it.  If you need to add or remove elements, you have to make a new array.
* If the language is statically typed, you also have to specify a single type for the values which you are going to put in the array when you create it.
* In languages which have *primitive types*, arrays are usually not objects, so they don't have any methods -- they are just containers.

Arrays are less easy to use in many ways, but they also have some advantages: because they are so simple, and there are so many restrictions on what you can do with them, the computer can handle them very efficiently. That means that it is often much faster to use an array than to use an object which behaves like a list.  A lot of programmers use them when it is important for their programs to be fast.

Python has a built-in ``array`` type.  It's not quite as restricting as an array in C or Java -- you have to specify a type for the contents of the array, and you can only use it to store numeric values, but you can resize it dynamically, like a list.  You will probably never need to use it.

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
    print(big numbers ^ even_numbers)

It is important to note that unlike lists and tuples sets are *not ordered*.  When we print a set, the order of the elements will be random.  If we want to process the contents of a set in a particular order, we will first need to convert it to a list or tuple and sort it::

    print(animals)
    print(sorted(animals))

The ``sorted`` function returns a ``list`` object.

How do we make an empty set?  We have to use the ``set`` function.  Dictionaries, which we will discuss in the next section, used curly brackets before sets adopted them, so an empty set of curly brackets is actually an empty dictionary::

    # this is an empty dictionary
    a = {}

    # this is how you make an empty set
    b = set()

You can use the ``list, ``tuple``, ``dict`` and even ``int``, ``float`` or ``str`` functions in the same way -- they all have sensible defaults -- but you will probably seldom find a reason to do so.

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

Like sets, dictionaries are not ordered -- if you print a dictionary, the order will be random.

Here are some commonly used methods of dictionary objects::

    marbles = {"red": 34, "green": 30, "brown": 31, "yellow": 29 }

    # Get a value by its key, or None if it doesn't exist
    marbles.get("orange")
    # You can specify a different default
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

Converting between collection types
===================================

Implicit conversions
--------------------

If you try to iterate over a collection in a ``for`` loop (something we will discuss in the next section), Python will try to convert it into something that you can iterate over if it knows how to.  For example, the dictionary views we saw above are not actually iterators, but Python knows how to make them into iterators -- so you can use them in a ``for`` loop without having to convert them yourself.

Sometimes the iterator you get by default may not be what you expected -- if you iterate over a dictionary in a ``for`` loop, you will iterate over the *keys*.  If what you actually want to do is iterate over the values, or key and value pairs, you will have to specify that yourself by using the dictionary's ``values`` or ``items`` view instead.

Explicit conversions
--------------------

You can convert between the different sequence types quite easily by using the type functions to ``cast`` sequences to the desired types -- just like you would use ``float`` and ``int``

Another look at strings
-----------------------


FROM ROUGH NOTES:

* Replace with discussion of all the cool Python collections:
  * lists, dicts, sets
* Maybe move further up the discussion
* Should the linked list algorithm be replaced with something more relevant?
  * Maybe a tree or graph implementation?