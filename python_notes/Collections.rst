====================================
Lists, tuples, dictionaries and sets
====================================

We have already encountered some simple Python types like numbers, strings and booleans.  Now we will see how we can group multiple objects together in a *collection* -- like a *list* of numbers, or a *dictionary* which we can use to store and retrieve key-value pairs.  Many useful collections are built-in types in Python, and you will encounter them quite often.

Lists
=====

The Python list type is called ``list``.  It is a type of sequence -- you can use it to store multiple values, and access them sequentially, by their position, or *index*, in the list.  You define a list *literal* (i.e. a hard-coded value) by putting a comma-separated list of values inside square brackets (``[`` and ``]``)::

    # a list of strings
    animals = ['cat', 'dog', 'fish', 'bison']

    # a list of integers
    numbers = [1, 7, 34, 20, 12]

    # a list of variables you defined somewhere else
    things = [
        one_variable,
        another_variable,
        third_variable, # this trailing comma is legal in Python
    ]

To refer to an element in the list, use the list identifier followed by the index inside square brackets.  Indices are integers which start from zero::

    print(animals[0]) # cat
    print(numbers[1]) # 7

You can also count from the end::

    print(animals[-1]) # the last element -- bison
    print(numbers[-2]) # the second-last element -- 20

You can extract a subset of a list, which will itself be a list, using a *slice*.  This uses almost the same syntax as accessing a single element, but instead of specifying a single index between the square brackets you need to specify an upper and lower bound.   Note that your sublist will *include* the element at the lower bound, but *exclude* the element at the upper bound::

    print(animals[1:3]) # ['dog', 'fish']
    print(animals[1:-1]) # ['dog', 'fish']

If one of the bounds is one of the ends of the list, you can leave it out. A slice with neither bound specified gives you a copy of the list::

    print(animals[2:]) # ['fish', 'bison']
    print(animals[:2]) # ['cat', 'dog']
    print(animals[:]) # a copy of the whole list

You can even include a third parameter to specify the step size::

    print(animals[::2]) # ['cat', 'fish']

.. Todo:: include a diagram showing how to number list elements

Lists are mutable -- you can modify elements, add elements to them or remove elements from them.  A list will change size dynamically when you add or remove elements -- you don't have to manage this yourself::

    # assign a new value to an existing element
    animals[3] = "hamster"

    # add a new element
    animals.append("squirrel")

    # remove an element
    del animals[2]

    # remove an element and assign it to a variable
    my_animal = animals.pop(0)

You can mix the types of values that you store in a list::

    my_list = ['cat', 12, 35.8]

List methods and functions
--------------------------

Lists vs arrays
---------------

Tuples
======

Conversions
-----------

Sets
====

Dictionaries
============


FROM ROUGH NOTES:

* Replace with discussion of all the cool Python collections:
  * lists, dicts, sets
* Maybe move further up the discussion
* Should the linked list algorithm be replaced with something more relevant?
  * Maybe a tree or graph implementation?