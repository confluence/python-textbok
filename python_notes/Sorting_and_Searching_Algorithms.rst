*****************************************
Sorting, searching and algorithm analysis
*****************************************

Introduction
============

We have learned that in order to write a computer program that
performs some task, we must construct a suitable algorithm. However,
the algorithm we construct is unlikely to be unique -- there are
likely many algorithms that perform the same task. The question then
arises as to whether some of these algorithms are in any sense better
than others. Algorithm analysis is the study of this question.

In this chapter we will analyze four algorithms, two for each of the
following tasks:

* sorting a list, and
* finding the position of a value within a sorted list.

Although there in general many ways that algorithms might be compared,
we will focus our attention on the two that are of primary importance
to many data processing algorithms:

* *time complexity* (how the number of steps required depends on the
  length of the input)

* *space complexity* (how the amount of extra memory or storage
  required depends on the length of the input)

.. Note::

    *Computational complexity theory* studies the inherent complexity
    of *tasks* themselves. Sometimes it is possible to prove that
    *any* algorithm that can perform a given task will require some
    minimum number of steps or amount of extra storage. A full
    introduction to computational complexity theory is outside the
    scope of these notes but we will mention some interesting results.


Sorting algorithms
==================

Selection sort
--------------

Here is the algorithm for selection sort:

* Search the whole list for the smallest element. Swap that element
  with the element at location 0.

* Search the list from location 1 to the end for the smallest
  element. Swap that element with the element at location 1.

* Search the list from location 2 to the end for the smallest
  element. Swap that element with the element at location 2.

* Continue in this way for all the other locations in the list.

To illustrate the principle behind selection sort, we use the
following array as an example:

.. blockdiag::

    blockdiag {
        class I [width = 64, fontsize = 16];
        A [numbered = 0, label = "7.2", class = "I"];
        B [numbered = 1, label = "3.5", class = "I"];
        C [numbered = 2, label = "0.8", class = "I"];
        D [numbered = 3, label = "2.7", class = "I"];
        E [numbered = 4, label = "9.5", class = "I"];
        F [numbered = 5, label = "5.8", class = "I"];

        A -> B -> C -> D -> E -> F;
    }

Exercise 1
----------

Complete the following code that will perform a selection sort in
Python. "..." denotes missing code that should be filled in::

    def selection_sort(items):
        """Sorts a list of items into ascending order using the
           selection sort algoright.
           """
        for step in range(len(items)):
            # Find the location of the smallest element in
            # items[step:].
            location_of_smallest = step
            for location in range(step, len(items)):
                # TODO: determine location of smallest
                ...
            # TODO: Exchange items[step] with items[location_of_smallest]
            ...


Merge sort
----------

Here are the steps for Merge sort:

* Each element in the array is a single partition. Merge adjacent
  partitions to a new array, resulting in partitions of size
  two. Assign the new array to the original.

* Each pair of elements in the array is a single partition. Merge
  adjacent partitions to another new array, resulting in partitions of
  size four. Assign the new array to the original.

* Each group of four elements in the original array is a single
  partition. Merge adjacent partitions to another new array, resulting
  in partitions of size eight. Assign the new array to the original.

* Continue this process until the partition size is at least as large
  as the whole array.



Python's sorting algorithm
--------------------------

Python's list objects use a sorting algorithm called *Timsort*
invented by Tim Peters in 2002 for use in Python. Timsort is a modifed
version of merge sort that uses insertion sort to arrange the list of
items into conveniently mergable sections.

.. Note::

   Tim Peters is also credited as the author of *The Zen of Python* --
   an attempt to summarize the early Python community's ethos in a
   short series of koans. You can read it by typing `import this` into
   the Python console.


Searching algorithms
====================

Linear search
-------------


Binary search
-------------


Algorithm complexity
====================


Complexities of common operations in Python
===========================================


