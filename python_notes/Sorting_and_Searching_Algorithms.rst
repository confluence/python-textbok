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

* ordering a list of values, and
* finding the position of a value within a sorted list.

Algorithm analysis should begin with a clear statement of the task to
be performed. This allows us to both check that the algorithm is
correct and ensure that the algorithms we are comparing perform the
same task.

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

.. Note::

    The common sorting and searching algorithms are widely implemented
    and already available for most programming languages. You will
    seldom have to implement them yourself outside of the exercises in
    these notes. Nevertheless, understanding these algorithms is still
    important since you will likely be making use of them within your
    own programs and their space and time complexity will thus affect
    that of your own algorithms. You may also be required to select
    which sorting or searching algorithm to use which will require a
    good understanding of the characteristics of the algorithms
    available.


Sorting algorithms
==================

Sorting a list of values is a common computational task that has been
well studied. The classic description of the task is as follows:

    Given a *list of values* and a function that *compares two
    values*, order the values in the list from smallest to largest.

The values might be integers, or strings or even other kinds of
objects. We will examine two algorithms:

* *Selection sort* (which relies on repeatedly *selecting* the next
  smallest item), and
* *Merge sort* (which relies on repeatedly *merging* sections of the
  list that are already sorted)

Other well-known algorithms for sorting lists are *Insertion sort*,
*Bubble sort*, *Heap sort*, *Quicksort* and *Shell sort*.

There are also a variety of algorithms which perform the sorting task
for restricted kinds of values, for example:

* *Counting sort* (relies on values all belonging to a small set of items)
* *Bucket sort* (relies on being able to map each value to one of a
  small set of items)
* *Radix sort* (relies on values being sequences of digits)

Restricting the task enlarges the set of algorithms that can perform
it and among these new algorithms may be ones that have desirable
properties. For example, *Radix sort* uses fewer steps than any
generic sorting algorithm.


Selection sort
--------------

Selection sort orders a given list by repeatedly selecting the
smallest remaining element and moving it to the end of a growing
sorted list.

To illustrate selection sort, let us examine how it operates on a
small list of four elements:

.. blockdiag::

    blockdiag {
        class I [width = 64, fontsize = 16];
        A [numbered = 0, label = "7.2", class = "I"];
        B [numbered = 1, label = "3.8", class = "I"];
        C [numbered = 2, label = "1.5", class = "I"];
        D [numbered = 3, label = "2.7", class = "I"];

        group {
            A -> B -> C -> D;
            label = "Unsorted";
            color = "#EE0000";
        }
    }

Initially the entire list is unsorted. We will use the front of the
list to hold the sorted items in order to avoid using extra storage
space but at the start this sorted list is empty.

First we must find the smallest element in the unsorted portion of the
list. We take the first element of the unsorted list as a candidate
and compare it to each of the following elements in turn, replacing
our candidate with any element found to be smaller. This requires 3
comparisons and we find that element 1.5 at position 2 is smallest.

Now we will swap the first element of our unordered list with the
smallest element to start our ordered list:

.. blockdiag::

    blockdiag {
        class I [width = 64, fontsize = 16];
        A [numbered = 0, label = "1.5", class = "I"];
        B [numbered = 1, label = "3.8", class = "I"];
        C [numbered = 2, label = "7.2", class = "I"];
        D [numbered = 3, label = "2.7", class = "I"];

        A -> B;
        group {
            A;
            label = "Sorted";
            color = "#00EE00";
        }
        group {
            B -> C -> D;
            label = "Unsorted";
            color = "#EE0000";
        }
    }

We now repeat our previous steps, determining that 2.7 is the smallest
remaining element and swap it with 3.8, the first element of the
current unordered section, to get:

.. blockdiag::

    blockdiag {
        class I [width = 64, fontsize = 16];
        A [numbered = 0, label = "1.5", class = "I"];
        B [numbered = 1, label = "2.7", class = "I"];
        C [numbered = 2, label = "7.2", class = "I"];
        D [numbered = 3, label = "3.8", class = "I"];

        B -> C;
        group {
            A -> B;
            label = "Sorted";
            color = "#00EE00";
        }
        group {
            C -> D;
            label = "Unsorted";
            color = "#EE0000";
        }
    }

Finally, we determine that 3.8 is the smallest of the remaining
unordered elements and swap it with 7.2:

.. blockdiag::

    blockdiag {
        class I [width = 64, fontsize = 16];
        A [numbered = 0, label = "1.5", class = "I"];
        B [numbered = 1, label = "2.7", class = "I"];
        C [numbered = 2, label = "3.8", class = "I"];
        D [numbered = 3, label = "7.2", class = "I"];

        C -> D;
        group {
            A -> B -> C;
            label = "Sorted";
            color = "#00EE00";
        }
        group {
            D;
            label = "Unsorted";
            color = "#EE0000";
        }
    }


More generally, the algorithm for selection sort is as follows:

* Divide the list to be sorted into a sorted portion at the front
  (initially empty) and an unsorted portion at the end (initially the
  whole list).

* Find the smallest element in the unsorted list:

  * Select the first element of the unsorted list as the initial
    candidate.

  * Compare the candidate to each element of the unsorted list in
    turn, replacing the candidate with the current element if the
    current element is smaller.

  * Once the end of the unsorted list is reached, the candidate is the
    smallest element.

* Swap the smallest element found in the previous step with the first
  element in the unsorted list, thus extending the sorted list by one
  element.

* Repeat the two steps above until only one element remains in the
  unsorted list.

.. TODO::

   Count number of operations.

.. TODO::

   Determine number of operations required for N elements.

.. Note::

   Stable sorts.

.. Note::

   In place sorts.


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

Exercise 2
----------


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

Exercise 3
----------

Binary search
-------------

Exercise 4
----------


Algorithm complexity
====================


Complexities of common operations in Python
===========================================

.. TODO::

    Summarize the important bits from http://wiki.python.org/moin/TimeComplexity

Answers to exercises
====================

.. TODO::

   Put answers here.
