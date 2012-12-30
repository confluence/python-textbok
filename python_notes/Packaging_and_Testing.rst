*********************
Packaging and testing
*********************

Modules
=======

All software projects start out small, and you are likely to start off by writing all of your program's code in a single file.  As your project grows, it will become increasingly inconvenient to do this -- it's difficult to find anything in a single file of code, and eventually you are likely to encounter a problem if you want to call two different classes by the same name.  At some point it will be a good idea to tidy up the project by splitting it up into several files, putting related classes or functions together in the same file.

Sometimes there will be a natural way to split things up from the start of the project -- for example, if your program has a database backend, a business logic layer and a graphical user interface, it is a good idea to put these three things into three separate files from the start instead of mixing them up.

How do we access code in one file from another file?  Python provides a mechanism for creating a *module* from each file of source code.  You can use code which is defined inside a module by *importing* the module using the ``import`` keyword -- we have already done this with some built-in modules in previous examples.

Each module has its own namespace, so it's OK to have two classes which have the same name, as long as they are in different modules.  If we import the whole module, we can access properties defined inside that module with the ``.`` operator::

    import datetime
    today = datetime.date.today()

We can also import specific classes or functions from the module using the ``from`` keyword, and use their names independently::

    from datetime import date
    today = date.today()

Creating a module is as simple as writing code into a Python file. A module which has the same name as the file (without the ``.py`` suffix) will automatically be created -- we will be able to import it if we run Python from the directory where the file is stored, or a script which is in the same directory as the other Python files.  If you want to be able to import your modules no matter where you run Python, you should package your code and install it -- we will look at this in the next chapter.

We can use the ``as`` keyword to give an imported name an alias in our code -- we can use this to shorten a frequently used module name, or to import a class which has the same name as a class which is already in our namespace, without overriding it::

    import datetime as dt
    today = dt.date.today()

    from mymodule import MyClass as FirstClass
    from myothermodule import MyClass as OtherClass

We can also import everything from a module using ``*``, but this is not recommended, since we might accidentally import things which redefine names in our namespace and not realise it::

    from mymodule import *

Packages
========

Just as a module is a collection of classes or functions, a package is a collection of modules.  We can organise several module files into a directory structure.  There are various tools which can then convert the directory into a special format (also called a "package") which we can use to install the code cleanly on our computer (or other people's computers).  This is called *packaging*.

Packaging a program with Distribute
-----------------------------------

A library called Distribute is currently the most popular tool for creating Python packages, and is recommended for use with Python 3.  It isn't a built-in library, but can be installed with a tool like ``pip`` or ``easy_install``.  Distribute is a more modern version of an older packaging library called Setuptools, and has been designed to replace it.  The original Setuptools doesn't support Python 3, but you may encounter it if you work on Python 2 code.  The two libraries have almost identical interfaces, and Distribute's module name, which you import in your code, is also ``setuptools``.

Let's say that we have split up our large program, which we will call "ourprog", into three files: ``db.py`` for the database backend, ``rules.py`` for the business logic, and ``gui.py`` for the graphical user interface.  First, we should arrange our files into the typical directory structure which packaging tools expect::

    ourprog/
        ourprog/
            __init__.py
            db.py
            gui.py
            rules.py
        setup.py

We have created two new files. ``__init__.py`` is a special file which marks the inner ``ourprog`` directory as a package, and also allows us to import all of ``ourprog`` as a module.  We can use this file to import classes or functions from our modules (``db``, ``gui`` and ``rules``) into the package's namespace, so that they can be imported directly from ``ourprog`` instead of from ``ourprog.db``, and so on -- but for now we will leave this file blank.

The other file, ``setup.py``, is the specification for our package.  Here is a minimal example::

    from setuptools import setup

    setup(name='ourprog',
        version='0.1',
        description='Our first program',
        url='http://ourwebsite.com',
        author='Jane Smith',
        author_email='jane.smith@example.com',
        license='GPL',
        packages=['ourprog'],
        zip_safe=False)

We create the package with a single call of the ``setup`` function, which we import from the ``setuptools`` module.  We pass in several parameters which describe our package.

Installing and importing our modules
------------------------------------

Now that we have written a ``setup.py`` file, we can run it in order to install our package on our system.  Although this isn't obvious, ``setup.py`` is a script which takes various command-line parameters -- we got all this functionality when we imported ``setuptools``.  We have to pass an ``install`` parameter to the script to install the code.  We need to input this command on the commandline, while we are in the same directory as ``setup.py``::

    python3 setup.py install

If everything has gone well, we should now be able to import ``ourprog`` from anywhere on our system.


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