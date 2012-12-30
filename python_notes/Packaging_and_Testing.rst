Packaging
=========

All software projects start out small, and you are likely to start off by writing all of your program's code in a single file.  As your project grows, it will become increasingly inconvenient to do this -- it's difficult to find anything in a single file of code, and eventually you are likely to encounter a problem if you want to call two different classes by the same name.  At some point it will be a good idea to tidy up the project by splitting it up into several files, putting related classes or functions together in the same file.

Sometimes there will be a natural way to split things up from the start of the project -- for example, if your program has a database backend, a business logic layer and a graphical user interface, it is a good idea to put these three things into three separate files from the start instead of mixing them up.

How do we access code in one file from another file?  Python provides a mechanism for creating a *package* from each file of source code.  You can use code which is defined inside a package by *importing* the package using the ``import`` keyword -- we have already done this with some built-in packages in previous examples.

Each package has its own namespace, so it's OK to have two classes which have the same name, as long as they are in different packages.  If we import the whole package, we can access properties defined inside that package with the ``.`` operator::

    import datetime
    today = datetime.date.today()

We can also import specific classes or functions from the package using the ``from`` keyword, and use their names independently::

    from datetime import date
    today = date.today()

We can use the ``as`` keyword to give an imported name an alias in our code -- we can use this to shorten a frequently used package name, or to import a class which has the same name as a class which is already in our namespace, without overriding it::

    import datetime as dt
    today = dt.date.today()

    from mypackage import MyClass as FirstClass
    from myotherpackage import MyClass as OtherClass

* arranging code in files
* setup.py install

Documentation
=============

* docstrings
* sphinx

Testing programs
================

* Something about unit tests
* Black box testing
* Glass box testing
* Add discussion of unit vs functional vs integrated tests