.. From http://www.cs.uct.ac.za/mit_notes/Java/Latest/html/single-html.html


Chapter 1: Introduction
=======================

* What is a Computer:
  * update hardware introduction

* Programming a Computer:
  * mention dynamic languages and interpreters somewhere
  * mention JITs somewhere
  * convert Java Programming Language to Python
  * convert Developing a Java Program to Python

* Types of Computers:
  * update section

* History of Computers:
  * add what happened after the 70s

* Programming Languages:
  * add static vs dynamic languages
  * add strongly vs weakly typed languages
  * explain where Python fits in


Chapter 2: Java Basics
======================

* Introduction
  * mention Python 3 and Python 2.

* Essentials of a Java Program
  * skeleton, keywords, identifiers, __main__, indentation, print,
    string formating, mention files

* Primitive Types
  * simple types -- integers, floats, boolean, strings
  * delay discussion of static and class variables until OO section

* Variables of Primitive Types and Strings
  * assignment is just labelling in Python

* Constants
  * replace with discussion of mutable vs immutable
  * mention constants in other languages.

* Input
  * input()
  * translate scanner example

* Type conversion
  * translate discussion to Python

* Compiling Java Programs
  * Running Python programs
  * Select appropriate Python IDE and translate wizard example

* Differences between Python 2 and 3
  * raw_input()
  * print
  * unicode vs bytes

* translate exercises


Chapter 3: Selection Control Statements
=======================================

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


Chapter 4: Loop Control Statements
==================================

* The for statement
  * discuss differences between Python and C/Java/C++ for loops.

* The while statement

* Add section of looping pitfalls
  * not editing mutable sequences while you iterate over them.
  * infinite loops

* Do-while loops
  * Replace with mention of do-while in other languages and while True
    equivalent.

* The break and continue statements

* Add a section for list comprehensions
  * Potential replacement for some simple for loops.


Chapter 5: Using Classes
========================

* Merge with chapter 6 probably.

Chapter 6: Writing Your Own Classes
===================================

* Translate to Python
* classmethod, staticmethod, __init__, magic methods (__str__, __eq__, ...)
* Translate section on packaging classes to discussion on packages, modules,
  etc. (probably move further up).


Chapter 7: Arrays
=================

* Discussions of arrays in other languages.
* Discussion of lists in Python.
* Discussion of tuples.
* Maybe move to a more generic section about sequences.
* Mention how to do 2D arrays in Python.
* Do we need a discussion / mention of Numpy?

Chapter 8: Sorting and Searching Arrays
=======================================

* Translate algorithms
* Using all the equivalent Python statements in the standard library
* How much of the algorithm stuff should be kept?
* Timsort. :)

Chapter 9: Object Orientated Approach to Programming
====================================================

* Mostly translating examples.
* Mention NotImplementedError.
* Mention Mix-ins.
* Are metaclasses too advanced to mention?
* Class decorators?

Chapter 10: Exceptions
======================

* Translate to Python

Chapters 11-12: Array List and Linked List
==========================================

* Replace with discussion of all the cool Python collections:
  * lists, dicts, sets
* Maybe move further up the discussion
* Should the linked list algorithm be replaced with something more relevant?
  * Maybe a tree or graph implementation?


Chapter 13: Better Collections: Using Interfaces, OO, and Generics
==================================================================

* Rewrite.
* Mention collections somewhere.
* Mention zope.interfaces somewhere.
* Generics mostly irrelevant.

Chapter 14: Introduction to GUI Programming with Swing
======================================================

* translate to Tcl/Tk.
* mention other toolkits.
* replace with introduction to web programming? Django? Flask?

Broader Issues
==============

* Add chapter on functions (before chapter 5 on classes)
  * Decorators!
* Parameter passing
* Scope! Where does it go?
* docstrings need to be mentioned somewhere
* Writing procedural code
* Writing functional code
  * Nested functions
* Split chapters more sensibly for Python
  * group sequence types
* Discussion of .pyc files.
* Do we want something about C extensions?
* Do we want something about regular expressions?
* Mention version control?
