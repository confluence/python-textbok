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


Insertion sort
--------------


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



Merge sort
----------



Python's sorting algorithm
--------------------------

.. TODO::
   mention tim sort


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


