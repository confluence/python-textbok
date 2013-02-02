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
        url='http://example.com',
        author='Jane Smith',
        author_email='jane.smith@example.com',
        license='GPL',
        packages=['ourprog'],
        zip_safe=False,
    )

We create the package with a single call of the ``setup`` function, which we import from the ``setuptools`` module.  We pass in several parameters which describe our package.

Installing and importing our modules
------------------------------------

Now that we have written a ``setup.py`` file, we can run it in order to install our package on our system.  Although this isn't obvious, ``setup.py`` is a script which takes various command-line parameters -- we got all this functionality when we imported ``setuptools``.  We have to pass an ``install`` parameter to the script to install the code.  We need to input this command on the commandline, while we are in the same directory as ``setup.py``::

    python3 setup.py install

If everything has gone well, we should now be able to import ``ourprog`` from anywhere on our system.

.. Todo:: should Virtualenv go here?

Documentation
=============

Code documentation is often treated as an afterthought.  While we are writing a program, it can seem to us that what our functions and classes do is obvious, and that writing down a lengthy explanation for each one is a waste of time.  We may feel very differently when we look at our code again after a break of several months, or when we are forced to read and understand somebody else's undocumented code!

We have already seen how we can insert comments into Python code using the ``#`` symbol.  Comments like this are useful for annotating individual lines, but they are not well-suited to longer explanations, or systematic documentation of all structures in our code.  For that, we use *docstrings*.

Docstrings
----------

A docstring is just an ordinary string -- it is usually written between triple quotes, because triple quotes are good for defining multiline string literals.  What makes a docstring special is its position in the code.  There are many tools which can parse Python code for strings which appear immediately after the definition of a module, class, function or method and aggregate them into an automatically generated body of documentation.

Documentation written like this can be easier to maintain than a completely separate document which is written by hand.  The docstring for each individual class or function is defined next to the function in our code, where we are likely to see it and notice if it is out of sync and needs to be updated.  Docstrings can also function as comments -- other people will be able to see them while reading our source code.  Interactive shells which use Python can also display docstrings when the user queries the usage of a function or class.

There are several different tools which parse docstrings -- the one which is currently used the most is called Sphinx.  In this course we won't go into detail about how to use Sphinx to generate documents, but we will see how to write docstrings in a format which is compatible with Sphinx.

Docstring examples
------------------

The Sphinx markup language is a variant of reStructuredText (reST) with some extra keywords defined. There is no set, compulsory Sphinx docstring format -- we can put any kind of Sphinx syntax inside the docstrings.  A docstring should at the very least contain a basic description of the structure being documented.

If the structure is a function, it is helpful to describe all the parameters and the return value, and also mention if the function can raise any exceptions.  Because Python isn't statically typed, it is important to provide information about the parameters that a function accepts.

We can also provide a much longer explanation after summarising all the basic information -- we can go into as much detail as we like; there is no length limit.

Here are some examples of docstrings form various objects::

    """This is a module for our Person class.
    .. moduleauthor: Jane Smith <jane.smith@example.com>
    """

    import datetime

    class Person:
        """This is a class which represents a person. It is a bit of a silly class.
        It stores some personal information, and can calculate a person's age.
        """

        def __init__(self, name, surname, birthdate, address, telephone, email):
            """This method creates a new person.

            :param name: first name
            :type name: str
            :param surname: surname
            :type surname: str
            :param birthdate: date of birth
            :type birthdate: datetime.date
            :param address: physical address
            :type address: str
            :param telephone: telephone number
            :type telephone: str
            :param email: email address
            :type email: str
            """

            self.name = name
            self.surname = surname
            self.birthdate = birthdate

            self.address = address
            self.telephone = telephone
            self.email = email

        def age(self):
            """This method calculates the person's age from the birthdate and the current date.

            :returns: int -- the person's age in years
            """
            today = datetime.date.today()
            age = today.year - self.birthdate.year

            if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
                age -= 1

            return age

.. Todo:: in this and other sections, "further reading" with links to documentation on the web.

Testing
=======

Automated tests are a beneficial addition to any program. They not only help us to discover errors, but also make it easier for us to modify code -- we can run the tests after making a change to make sure that we haven't broken anything.  This is vital in any large project, especially if there are many people working on the same code.  Without tests, it can be very difficult for anyone to find out what other parts of the system a change could affect, and introducing any modification is thus a potential risk.  This makes development on the project move very slowly, and changes often introduce bugs.

Adding automated tests can seem like a waste of time in a small project, but they can prove invaluable if the project becomes larger or if we have to return to it to make a small change after a long absence.  They can also serve as a form of documentation -- by reading through test cases we can get an idea of how our program is supposed to behave. Some people even advocate writing tests *first*, thereby creating a specification for what the program is supposed to do, and filling in the actual program code afterwards.

We may find this approach a little extreme, but we shouldn't go too far in the opposite direction -- if we wait until we have written the entire program before writing any tests, we probably won't bother writing them at all.  It is a good idea to write portions of our code and the tests for them at approximately the same time -- then we can test our code while we are developing it.  Most programmers write at least temporary tests during development to make sure that a new function is working correctly -- we saw in a previous chapter how we can use print statements as a quick, but impermanent form of debugging.  It is better practice to write a permanent test instead -- once we have set up the testing framework, it really doesn't require a lot more effort.

In order for our code to be suitable for automated testing, we need to organise it in logical subunits which are easy to import and use independently from outside the program.  We should already be doing this by using functions and classes, and avoiding reliance on global variables.  If a function relies only on its input parameters to produce some kind of result, we can easily import this function into a separate testing module, and check that various examples of input produce the expected results.  Each matching set of input and expected output is called a *test case*.

Tests which are applied to individual components in our code are known as *unit tests* -- they verify that each of the components is working correctly.  Testing the interaction between different components in a system is known as *integration testing*.  A test can be called a *functional test* if it tests a particular feature, or *function* of the code -- this is usually a relatively high-level specification of a requirement, not an actual single function.

In this section we will mostly look at unit testing, but we can apply similar techniques at any level of automated tests.  When we are writing unit tests, as a rule of thumb, we should have a test for every function in our code (including each method of each class).

It is also good practice to write a new test whenever we fix a bug -- the test should specifically check for the bug which we have just fixed.  If the bug was caused by something which is a common mistake, it's possible that someone will make the same mistake again in the future -- our test will help to prevent that.  This is a form of *regression testing*, which aims to ensure that our code doesn't break when we add changes.

Selecting test cases
--------------------

How do we select test cases?  There are two major approaches that we can follow: *black-box* or *glass-box* testing.  We can also use a combination of the two.

In black-box testing, we treat our function like an opaque "black box".  We don't use our knowledge of how the function is written to pick test cases -- we only think about what the function is supposed to do.  A strategy commonly used in black-box testing is is *equivalence testing* and *boundary value analysis*.

An *equivalence class* is a set of input values which should all produce similar output, and there are *boundaries* between neighbouring equivalence classes.  Input values which lie near these boundaries are the most likely to produce incorrect output, because it's easy for a programmer to use ``<`` instead of ``<=`` or start counting from ``1`` instead of ``0``, both of which could cause an *off-by-one* error.  If we test an input value from inside each equivalence class, and additionally test values just before, just after and on each boundary, we can be reasonably sure that we have covered all the bases.

.. Todo:: the program for this function should be in an exercise in the selection statement chapter. Add a reference.

For example, consider a simple function which calculates a grade from a percentage mark.  If we were to use equivalence testing and boundary analysis on this function, we would pick the test cases like this:

=================  ======  ==============  ===================  ===================
Equivalence class  sample  lower boundary  just above boundary  just below boundary
=================  ======  ==============  ===================  ===================
mark > 100         150     100             101                  99
80 <= mark <= 100  90      80              81                   79
70 <= mark < 80    75      70              71                   69
60 <= mark < 70    65      60              61                   59
50 <= mark < 60    55      50              51                   49
0 <= mark < 50     25      0               1                    -1
mark < 0           -50
=================  ======  ==============  ===================  ===================

In glass-box testing, we pick our test cases by analysing the code inside our function.  The most extensive form of this strategy is *path coverage*, which aims to test every possible path through the function.

A function without any selection or loop statements has only one path. Testing such a function is relatively easy -- if it runs correctly once, it will probably run correctly every time.  If the function contains a selection or loop statement, there will be more than one possible path passing through it: something different will happen if an *if* condition is true or if it is false, and a loop will execute a variable number of times.  For a function like this, a single test case might not execute every statement in the code.

We could construct a separate test case for every possible path, but this rapidly becomes impractical. Each *if* statement doubles the number of paths -- if our function had 10 *if* statements, we would need more than a thousand test cases, and if it had 20, we would need over a million!  A more viable alternative is the *statement coverage* strategy, which only requires us to pick enough test cases to ensure that each *statement* inside our function is executed at least once.

Writing unit tests
------------------

We can write unit tests in Python using the built-in ``unittest`` module.  We typically put all our tests in a file hierarchy which is separate from our main program.  For example, if we were to add tests to our packaging example above, we would probably create a test module for each of our three program modules, and put them all in a separate test directory::

    ourprog/
        ourprog/
            __init__.py
            db.py
            gui.py
            rules.py
            test/
                __init__.py
                test_db.py
                test_gui.py
                test_rules.py
        setup.py

Suppose that our ``rules.py`` file contains a single class::

    class Person:
        TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

        def __init__(self, name, surname):
            self.name = name
            self.surname = surname

        def fullname(self, title):
            if title not in self.TITLES:
                raise ValueError("Unrecognised title: '%s'" % title)

            return "%s %s %s" % (title, self.name, self.surname)


Our ``test_rules.py`` file should look something like this::

    import unittest
    from ourprog.rules import Person

    class TestPerson(unittest.TestCase):

        def setUp(self):
            self.person = Person("Jane", "Smith")

        def test_init(self):
            self.assertEqual(self.person.name, "Jane")
            self.assertEqual(self.person.surname, "Smith")

        def test_fullname(self):
            self.assertEqual(self.person.fullname("Ms"), "Ms Jane Smith")
            self.assertEqual(self.person.fullname("Mrs"), "Mrs Jane Smith")
            self.assertRaises(ValueError, self.person.fullname, "HRH")

We import the ``unittest`` module, and also the class which we are going to test.  This example assumes that we have packaged our code and installed it on our system, so that Python can find ``ourprog.rules``.

In the ``unittest`` package, the ``TestCase`` class serves as a container for tests which need to share some data.  For each collection of tests that we want to write, we define a class which inherits from ``TestCase`` and define all our tests as methods on that class.

In this example, all the tests in this ``TestCase`` test the same class, and there is one test per method (including the initialisation method) -- but there is no compulsory mapping.  You can use multiple ``TestCase`` classes to test each of your own classes, or perhaps have one ``TestCase`` for each set of related functionality.

We set up the class which we are going to test in the ``setUp`` method -- this special method will be executed before each test is run.  There is also a ``tearDown`` method, which we can use if we need to do something *after* each test.

Inside each test, we use the *assertion* methods of ``TestCase`` to check if certain things are true about our program's behaviour.  As soon as one assertion statement fails, the whole test fails.  We will often use ``assertEqual``, but there are many other assertion methods like ``assertNotEqual``, ``assertTrue`` or ``assertIn``.  ``assertRaises`` lets us check that a function raises an exception.  Note that when we use this assertion method we don't call the function (because it would raise an exception!) -- we just pass in the function name and its parameters.

There are many ways of running the tests once we have written them.  Here is a simple way of running all the tests from a single file: at the bottom of ``test_rules.py``, we can add::

    if __name__ == '__main__':
        unittest.main()

Now if we execute ``test_rules.py`` with Python, ``unittest`` will run the ``TestCase`` which we have defined. The condition in the ``if`` statement detects whether we are running the file as a script, and prevents the ``main`` function from being executed if we import this module from another file.  We will learn more about writing scripts in the next chapter.

We can also execute the unittest module on the commandline and use it to import and run some or all of our tests.  By default the module will try to *discover* all the tests that can be imported from the current directory, but we can also specify one or more module, class or test method::

    # these commands will try to find all our tests
    python -m unittest
    python -m unittest discover

    # but we can be more specific
    python -m unittest ourprog.test.test_rules
    python -m unittest ourprog.test.test_rules.TestPerson
    python -m unittest ourprog.test.test_rules.TestPerson.test_fullname

    # we can also turn on verbose output with -v
    python -m unittest -v test_rules

The ``unittest`` package also allows us to group some or all of our tests into *suites*, so that we can run many related tests at once.  One way to add all the tests from our ``TestPerson`` class to a suite is to add this function to the ``test_rules.py`` file::

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(TestPerson)
        return suite

We could define a suite in ``ourprog/test/__init__py`` which contains all the tests from all our modules, either by combining suites from all the modules or just adding all the tests directly. The ``TestSuite`` class and the ``TestLoader`` class, which we can use to build suites, are both very flexible.  They allow us to construct test suites in many different ways.

We can integrate our tests with our packaging code by adding a ``test_suite`` parameter to our ``setup`` call in ``setup.py``.  Despite its name, this parameter doesn't have to be a suite -- we can just specify the full name of our ``test`` module to include all our tests::

    setup(name='ourprog',
        # (...)
        test_suite='ourprog.test',
        # (...)
    )

Now we can build our package and run all our tests by passing the ``test`` parameter to ``setup.py``::

    python setup.py test

    # We can override what to run using -s
    # For example, we can run a single module
    python setup.py test -s ourprog.test.test_rules

In previous versions of Python, we would have needed to define a test suite just to run all our tests at once, but in newer versions it is no longer necessary to define our own suites for simple test organisation.  We can now easily run all the tests, or a single module, class or method just by using ``unittest`` on the commandline or ``setup.py test``.  We may still find it useful to write custom suites for more complex tasks -- we may wish to group tests which are spread across multiple modules or classes, but which are all related to the same feature.

Checking for test coverage
--------------------------

How do we know if our test cases cover all the statements in our code?  There are many third-party unit testing libraries which include functionality for calculating coverage, but we can perform a very simple check by using ``unittest`` together with the built-in ``trace`` module.  We can modify our test module like this::

    import trace, sys

    # all our test code

    if __name__ == "__main__":
        t = trace.Trace(ignoredirs=[sys.prefix, sys.exec_prefix], count=1, trace=0)
        t.runfunc(unittest.main)
        r = t.results()
        r.write_results(show_missing=True)

The first line in the ``if`` block creates a ``Trace`` object which is going to trace the execution of our program -- across all the source files in which code is found. We use the ``ignoredirs`` parameter to ignore any code in Python's installed modules -- now we should only see results from our program file and our test file.  Setting the ``count`` parameter to ``1`` makes the ``Trace`` object count the number of times that each line is executed, and setting ``trace`` to ``0`` prevents it from printing out lines as they are executed.

The second line specifies that we should run our test suite's main function.  The third line retrieves the results from the object -- the results are another kind of object, which is based on a dictionary.  This object has a convenient ``write_results`` method which we use in the fourth line to output a file of line counts for each of our source files. They will be written to the current directory by default, but we could also specify another directory with an optional parameter.  The ``show_missing`` parameter ensures that lines which were *never* executed are included in the files and clearly marked.

We need to run the test file directly to make sure that the code inside the ``if`` block is executed.  Afterwards, we should find two files which end in ``.cover`` in the current directory -- one for our program file and one for our test file.  Each line should be annotated with the number of times that it was executed when we ran our test code.

Exercise 1
----------

In this exercise you will write a program which estimates the cost of a telephone call, and design and implement unit tests for the program.

The phone company applies the following rules to a phone call to calculate the charge:

* The minimum before-tax charge of 59.400 cents applies to all calls to any destination up to 50km away and 89.000 cents for any destination further than 50km away.
* Calls are charged on a per-second basis at 0.759 cents per second (<= 50km) and 1.761 cents per second (> 50km)
* Off-peak seconds (from 19:00:00 to 06:59:59 the next day) are given a discount of 40% off (<= 50km) and 50% off (> 50km) off the above rate
* If the type of call was share-call AND the destination is more than 50km away, there is a discount of 50% off after any off-peak discount (minimum charge still applies). However, share-calls over shorter distances are not discounted.
* Finally, VAT of 14% is added to give the final cost.

Your program should ask for the following input:

* The starting time of the call (to be split up into hours, minutes and seconds)
* The duration of the call (to be split up into minutes and seconds)
* Whether the duration was more than 50km away
* Whether the call was share-call

Hint: you can prompt the user to input hours, minutes and seconds at once by asking for a format like *HH:MM:SS* and splitting the resulting string by the delimiter.  You may assume that the user will enter valid input, and that no call will exceed 59 minutes and 59 seconds.

Your program should output the following information:

* The basic cost
* The off-peak discount
* The share-call discount
* The net cost
* The VAT
* The total cost

#. Before you write the program, identify the equivalence classes and boundaries that you will need to use in equivalence testing and boundary analysis when writing black-box tests. This may help you to design the program itself, and not just the tests!

#. Write the program.  Remember that you will need to write unit tests for this program, and design it accordingly -- the calculation that you need to test should be placed in some kind of unit, like a function, which can be imported from outside of the program and used independently of the rest of the code (like the user input)!

#. Now implement the black-box tests which you have designed by writing a unit test module for your program. Run all the tests, and make sure that they pass!  Then use the ``trace`` module to check how well your tests cover your function code.

Answers to exercises
====================

Answer to exercise 1
--------------------

#. Peak and off-peak times provide an obvious source of equivalence classes for the start and duration of the call.  A call could start during peak or off-peak hours, and it could end in peak or off-peak hours (because the maximum duration of a call is just under an hour, a call can cross the peak/off-peak boundary once, but not twice).  A call could also cross over the boundary between days, and this wrapping must be handled correctly.

   A good set of boundaries for the start of the call would be: 00:00, 06:00, 07:00, 18:00 and 19:00.  A good set of boundaries for the duration of the call would be the minimum and maximum durations -- 00:00 and 59:59.  We don't need to test every combination of start time and duration -- the duration of the call is only really important if the call starts within an hour of the peak/off-peak switch.  We can test the remaining start times with a single duration.

   The other input values entered by the user are boolean, so only a true value and a false value needs to be tested for each.  Again, we don't need to test each boolean option with every possible combination of the previous options -- one or two cases should be sufficient.

#. Here is an example program::

    import datetime

    # The first value in each tuple is for distances <= 50km
    # The second value is for distances > 50km
    MIN_CHARGE = (59.400, 89.000)
    CHARGE_PER_SEC = (0.759, 1.761)
    OFFPEAK_DISCOUNT = (0.4, 0.5)
    SHARECALL_DISCOUNT = (0.0, 0.5)

    NEAR, FAR = 0, 1

    OFF_PEAK_START = datetime.time(19, 0, 0)
    HOUR_BEFORE_OFF_PEAK_START = datetime.time(18, 0, 0)
    OFF_PEAK_END = datetime.time(7, 0, 0)
    HOUR_BEFORE_OFF_PEAK_END = datetime.time(6, 0, 0)

    VAT_RATE = 0.14

    def price_estimate(start_str, duration_str, destination_str, share_call_str):
        start = datetime.datetime.strptime(start_str, "%H:%M:%S").time()
        d_m, d_s = [int(p) for p in duration_str.split(":")]
        duration = datetime.timedelta(minutes=d_m, seconds=d_s).total_seconds()
        # We set the destination to an index value we can use with the tuple constants
        destination = FAR if destination_str.lower() == 'y' else NEAR
        share_call = True if share_call_str.lower() == 'y' else False

        peak_seconds = 0
        off_peak_seconds = 0

        if start >= OFF_PEAK_END and start <= HOUR_BEFORE_OFF_PEAK_START:
            # whole call fits in peak time
            peak_seconds = duration
        elif start >= OFF_PEAK_START or start <= HOUR_BEFORE_OFF_PEAK_END:
            # whole call fits in off-peak time
            off_peak_seconds = duration
        else:
            # call starts within hour of peak/off-peak boundary
            secs_left_in_hour = 3600 - start.minute * 60 + start.second

            if start < OFF_PEAK_END:
                # call starts in off-peak time
                if duration > secs_left_in_hour:
                    peak_seconds = duration - secs_left_in_hour
                off_peak_seconds = duration - peak_seconds
            else:
                # call starts in peak time
                if duration > secs_left_in_hour:
                    off_peak_seconds = duration - secs_left_in_hour
                peak_seconds = duration - off_peak_seconds

        basic = CHARGE_PER_SEC[destination] * duration
        offpeak_discount = OFFPEAK_DISCOUNT[destination] * CHARGE_PER_SEC[destination] * off_peak_seconds
        if share_call:
            share_call_discount =  SHARECALL_DISCOUNT[destination] * (basic - offpeak_discount)
        else:
            share_call_discount = 0
        net = basic - offpeak_discount - share_call_discount

        if net < MIN_CHARGE[destination]:
            net = MIN_CHARGE[destination]

        vat = VAT_RATE * net
        total = net + vat

        return basic, offpeak_discount, share_call_discount, net, vat, total

    if __name__ == "__main__":
        start_str = input("Please enter the starting time of the call (HH:MM:SS): ")
        duration_str = input("Please enter the duration of the call (MM:SS): ")
        destination_str = input("Was the destination more than 50km away? (Y/N): ")
        share_call_str = input("Was the call a share-call? (Y/N): ")

        results = price_estimate(start_str, duration_str, destination_str, share_call_str)

        print("""Basic cost: %g
        Off-peak discount: %g
        Share-call discount: %g
        Net cost: %g
        VAT: %g
        Total cost: %g
        """ % results)


#. Here is an example program, including a coverage test::

    import unittest
    import trace, sys

    from estimate import price_estimate

    class TestEstimate(unittest.TestCase):
        def test_off_peak(self):
            # all these cases should fall within off-peak hours and have the same result
            test_cases = [
                ("23:59:59", "10:00", "N", "N"),
                ("00:00:00", "10:00", "N", "N"),
                ("00:00:01", "10:00", "N", "N"),
                ("05:59:59", "10:00", "N", "N"),
                ("06:00:00", "10:00", "N", "N"),
                ("06:00:01", "10:00", "N", "N"),
                ("19:00:00", "10:00", "N", "N"),
                ("19:00:01", "10:00", "N", "N"),
            ]

            for start, duration, far_away, share_call in test_cases:
                basic, op_discount, sc_discount, net, vat, total = price_estimate(start, duration, far_away, share_call)
                self.assertAlmostEqual(basic, 455.4)
                self.assertAlmostEqual(op_discount, 182.16)
                self.assertAlmostEqual(sc_discount, 0)
                self.assertAlmostEqual(net, 273.24)
                self.assertAlmostEqual(vat, 38.2536)
                self.assertAlmostEqual(total, 311.4936)

        def test_peak(self):
            # all these cases should fall within peak hours and have the same result
            test_cases = [
                ("07:00:00", "10:00", "N", "N"),
                ("07:00:01", "10:00", "N", "N"),
                ("17:59:59", "10:00", "N", "N"),
                ("18:00:00", "10:00", "N", "N"),
                ("18:00:01", "10:00", "N", "N"),
            ]

            for start, duration, far_away, share_call in test_cases:
                basic, op_discount, sc_discount, net, vat, total = price_estimate(start, duration, far_away, share_call)
                self.assertAlmostEqual(basic, 455.4)
                self.assertAlmostEqual(op_discount, 0)
                self.assertAlmostEqual(sc_discount, 0)
                self.assertAlmostEqual(net, 455.4)
                self.assertAlmostEqual(vat, 63.756)
                self.assertAlmostEqual(total, 519.156)

        def test_peak_and_off_peak(self):
            # these test cases cross the peak / off-peak boundary, and all have different results.
            test_cases = [
                ("06:59:59", "59:59", "N", "N"),
                ("07:00:00", "59:59", "N", "N"),
                ("07:00:01", "59:59", "N", "N"),

                ("18:59:59", "59:59", "N", "N"),
                ("19:00:00", "59:59", "N", "N"),
                ("19:00:01", "59:59", "N", "N"),

                ("06:30:00", "00:00", "N", "N"),
                ("06:30:00", "00:01", "N", "N"),
                ("06:30:00", "59:58", "N", "N"),
                ("06:30:00", "59:59", "N", "N"),
            ]

            expected_results = [
                (2731.641, 36.128400000000006, 0, 2695.5126, 377.371764, 3072.884364),
                (2731.641, 0.0, 0, 2731.641, 382.42974, 3114.07074),
                (2731.641, 0.0, 0, 2731.641, 382.42974, 3114.07074),

                (2731.641, 1056.528, 0, 1675.113, 234.51582, 1909.62882),
                (2731.641, 1092.6564, 0, 1638.9846, 229.457844, 1868.442444),
                (2731.641, 1092.6564, 0, 1638.9846, 229.457844, 1868.442444),

                (0.0, 0.0, 0, 59.4, 8.316, 67.716), # minimum charge
                (0.759, 0.3036, 0, 59.4, 8.316, 67.716), # minimum charge
                (2730.882, 546.48, 0, 2184.402, 305.81628, 2490.21828),
                (2731.641, 546.48, 0, 2185.161, 305.92254, 2491.08354),
            ]

            for parameters, results in zip(test_cases, expected_results):
                basic, op_discount, sc_discount, net, vat, total = price_estimate(*parameters)
                exp_basic, exp_op_discount, exp_sc_discount, exp_net, exp_vat, exp_total = results
                self.assertAlmostEqual(basic, exp_basic)
                self.assertAlmostEqual(op_discount, exp_op_discount)
                self.assertAlmostEqual(sc_discount, exp_sc_discount)
                self.assertAlmostEqual(net, exp_net)
                self.assertAlmostEqual(vat, exp_vat)
                self.assertAlmostEqual(total, exp_total)

        def test_far_destination_share_call(self):
            # now we repeat some basic test cases with a far destination and/or share-call

            test_cases = [
                # off-peak
                ("23:59:59", "10:00", "Y", "N"),
                ("23:59:59", "10:00", "Y", "Y"),
                ("23:59:59", "10:00", "N", "Y"),
                # peak
                ("07:00:00", "10:00", "Y", "N"),
                ("07:00:00", "10:00", "Y", "Y"),
                ("07:00:00", "10:00", "N", "Y"),
            ]

            expected_results = [
                (1056.6, 528.3, 0, 528.3, 73.962, 602.262),
                (1056.6, 528.3, 264.15, 264.15, 36.981, 301.131),
                (455.4, 182.16, 0.0, 273.24, 38.2536, 311.4936),

                (1056.6, 0.0, 0, 1056.6, 147.924, 1204.524),
                (1056.6, 0.0, 528.3, 528.3, 73.962, 602.262),
                (455.4, 0.0, 0.0, 455.4, 63.756, 519.156),
            ]

            for parameters, results in zip(test_cases, expected_results):
                basic, op_discount, sc_discount, net, vat, total = price_estimate(*parameters)
                exp_basic, exp_op_discount, exp_sc_discount, exp_net, exp_vat, exp_total = results
                self.assertAlmostEqual(basic, exp_basic)
                self.assertAlmostEqual(op_discount, exp_op_discount)
                self.assertAlmostEqual(sc_discount, exp_sc_discount)
                self.assertAlmostEqual(net, exp_net)
                self.assertAlmostEqual(vat, exp_vat)
                self.assertAlmostEqual(total, exp_total)

    if __name__ == "__main__":
        t = trace.Trace(ignoredirs=[sys.prefix, sys.exec_prefix], count=1, trace=0)
        t.runfunc(unittest.main)

        r = t.results()
        r.write_results(show_missing=True)
