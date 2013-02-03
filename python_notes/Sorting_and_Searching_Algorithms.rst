*****************************************
Sorting, searching and algorithm analysis
*****************************************

Introduction
============

We have learned that in order to write a computer program that
performs some taks, we must construct a suitable algorithm. However,
the algorithm we construct is unlikely to be unique -- there are
likely many algorithms that perform the same task. The question then
arises as to whether some of these algorithms are in any sense better
than others. Algorithm analysis is the study of this question.


Sorting algorithms
==================


Selection sort
--------------

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


Merge sort
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


Binary search
-------------


Algorithm complexity
====================


Complexities of common operations in Python
===========================================


