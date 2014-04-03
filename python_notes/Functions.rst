*********
Functions
*********

Introduction
============

A function is a sequence of statements which performs some kind of task.  We use functions to eliminate code duplication -- instead of  writing all the statements at every place in our code where we want to perform the same task, we define them in one place and refer to them by the function name.  If we want to change how that task is performed, we will now mostly only need to change code in one place.

Here is a definition of a simple function which takes no parameters and doesn't return any values::

    def print_a_message():
        print("Hello, world!")

We use the ``def`` statement to indicate the start of a function definition. The next part of the definition is the function name, in this case ``print_a_message``, followed by round brackets (the definitions of any parameters that the function takes will go in between them) and a colon.  Thereafter, everything that is indented by one level is the body of the function.

Functions *do things*, so you should always choose a function name which explains as simply as accurately as possible *what the function does*.  This will usually be a verb or some phrase containing a verb.  If you change a function so much that the name no longer accurately reflects what it does, you should consider updating the name -- although this may sometimes be inconvenient.

This particular function always does exactly the same thing: it prints the message ``"Hello, world!"``.

Defining a function does not make it run -- when the flow of control reaches the function definition and executes it, Python just learns about the function and what it will do when we run it.  To run a function, we have to *call* it.  To call the function we use its name followed by round brackets (with any parameters that the function takes in between them)::

    print_a_message()

Of course we have already used many of Python's built-in functions, such as ``print`` and ``len``::

    print("Hello")
    len([1, 2, 3])

Many objects in Python are *callable*, which means that you can call them like functions -- a callable object has a special method defined which is executed when the object is called.  For example, types such as ``str``, ``int`` or ``list`` can be used as functions, to create new objects of that type (sometimes by converting an existing object)::

    num_str = str(3)
    num = int("3")

    people = list() # make a new (empty) list
    people = list((1, 2, 3)) # convert a tuple to a new list

In general, classes (of which types are a subset) are callable -- when we call a class we call its *constructor* method, which is used to create a new object of that class.  We will learn more about classes in the next chapter, but you may recall that we already called some classes to make new objects when we raised exceptions::

    raise ValueError("There's something wrong with your number!")

Because functions are objects in Python, we can treat them just like any other object -- we can assign a function as the value of a variable. To refer to a function without calling it, we just use the function name without round brackets::

    my_function = print_a_message

    # later we can call the function using the variable name
    my_function()

Because defining a function does not cause it to execute, we can use an identifier inside a function even if it hasn't been defined yet -- as long as it becomes defined by the time we run the function.  For example, if we define several functions which all call each other, the order in which we define them doesn't matter as long as they are all defined before we start using them::

    def my_function():
        my_other_function()

    def my_other_function():
        print("Hello!")

    # this is fine, because my_other_function is now defined
    my_function()

If we were to move that function call up, we would get an error::

    def my_function():
        my_other_function()

    # this is not fine, because my_other_function is not defined yet!
    my_function()

    def my_other_function():
        print("Hello!")

Because of this, it's a good idea to put all function definitions near the top of your program, so that they are executed before any of your other statements.

Exercise 1
----------

#. Create a function called ``func_a``, which prints a message.
#. Call the function.
#. Assign the function object as a value to the variable ``b``, without calling the function.
#. Now call the function using the variable ``b``.

Input parameters
================

It is very seldom the case that the task that we want to perform with a function is always exactly the same.  There are usually minor differences to what we need to do under different circumstances.  We don't want to write a slightly different function for each of these slightly different cases -- that would defeat the object of the exercise!  Instead, we want to pass information into the function and use it inside the function to tailor the function's behaviour to our exact needs.  We express this information as a series of *input parameters*.

For example, we can make the function we defined above more useful if we make the message customisable::

    def print_a_message(message):
        print(message)

More usefully, we can pass in two numbers and add them together::

    def print_sum(a, b):
        print(a + b)

``a`` and ``b`` are parameters.  When we call this function, we have to pass two paramenters in, or we will get an error::

    print_sum() # this won't work

    print_sum(2, 3) # this is correct

In the example above, we are passing ``2`` and ``3`` as parameters to the function when we call it.  That means that when the function is executed, the variable ``a`` will be given the value ``2`` and the variable ``b`` will be given the value ``3``.  You will then be able to refer to these values using the variable names ``a`` and ``b`` inside the function.

In languages which are statically typed, we have to declare the types of parameters when we define the function, and we can only use variables of those types when we call the function.  If we want to perform a similar task with variables of different types, we must define a separate function which accepts those types.

In Python, parameters have no declared types.  We can pass any kind of variable to the ``print_message`` function above, not just a string.  We can use the ``print_sum`` function to add any two things which can be added: two integers, two floats, an integer and a float, or even two strings.  We can also pass in an integer and a string, but although these are permitted as parameters, they cannot be added together, so we will get an error when we actually try to add them inside the function.

The advantage of this is that we don't have to write a lot of different ``print_sum`` functions, one for each different pair of types, when they would all be identical otherwise.  The disadvantage is that since Python doesn't check parameter types against the function definition when a function is called, we may not immediately notice if the wrong type of parameter is passed in -- if, for example, another person interacting with code that we have written uses parameter types that we did not anticipate, or if we accidentally get the parameters out of order.

This is why it is important for us to test our code thoroughly -- something we will look at in a later chapter. If we intend to write code which is robust, especially if it is also going to be used by other people, it is also often a good idea to check function parameters early in the function and give the user feedback (by raising exceptions) if the are incorrect.

Exercise 2
----------

#. Create a function called ``hypotenuse``, which takes two numbers as parameters and prints the square root of the sum of their squares.
#. Call this function with two floats.
#. Call this function with two integers.
#. Call this function with one integer and one float.

Return values
=============

The function examples we have seen above don't return any values -- they just result in a message being printed.  We often want to use a function to calculate some kind of value and then *return* it to us, so that we can store it in a variable and use it later.  Output which is returned from a function is called a *return value*.  We can rewrite the ``print_sum`` function to return the result of its addition instead of printing it::

    def add(a, b):
        return a + b

We use the ``return`` keyword to define a return value.  To access this value when we call the function, we have to *assign* the result of the function to a variable::

    c = add(a, b)

Here the return value of the function will be assigned to ``c`` when the function is executed.

A function can only have a single return value, but that value can be a list or tuple, so in practice you can return as many different values from a function as you like.  It usually only makes sense to return multiple values if they are tied to each other in some way.  If you place several values after the ``return`` statement, separated by commas, they will automatically be converted to a tuple.  Conversely, you can assign a tuple to multiple variables separated by commas at the same time, so you can *unpack* a tuple returned by a function into multiple variables::

    def divide(dividend, divisor):
        quotient = dividend // divisor
        remainder = dividend % divisor
        return quotient, remainder

    # you can do this
    q, r = divide(35, 4)

    # but you can also do this
    result = divide(67, 9)
    q1 = result[0]
    q2 = result[1]

    # by the way, you can also do this
    a, b = (1, 2)
    # or this
    c, d = [5, 6]

What happens if you try to assign one of our first examples, which don't have a return value, to a variable? ::

    mystery_output = print_message("Boo!")
    print(mystery_output)

All functions do actually return *something*, even if we don't define a return value -- the default return value is ``None``, which is what our mystery output is set to.

When a ``return`` statement is reached, the flow of control immediately exits the function -- any further statements in the function body will be skipped.  We can sometimes use this to our advantage to reduce the number of conditional statements we need to use inside a function::

    def divide(dividend, divisor):
        if not divisor:
            return None, None # instead of dividing by zero

        quotient = dividend // divisor
        remainder = dividend % divisor
        return quotient, remainder

If the ``if`` clause is executed, the first ``return`` will cause the function to exit -- so whatever comes after the ``if`` clause doesn't need to be inside an ``else``.  The remaining statements can simply be in the main body of the function, since they can only be reached if the ``if`` clause is not executed.

This technique can be useful whenever we want to check parameters at the beginning of a function -- it means that we don't have to indent the main part of the function inside an ``else`` block.  Sometimes it's more appropriate to raise an exception instead of returning a value like ``None`` if there is something wrong with one of the parameters::

    def divide(dividend, divisor):
        if not divisor:
            raise ValueError("The divisor cannot be zero!")

        quotient = dividend // divisor
        remainder = dividend % divisor
        return quotient, remainder

Having multiple exit points scattered throughout your function can make your code difficult to read -- most people expect a single ``return`` right at the end of a function.  You should use this technique sparingly.

.. Note:: in some other languages, only functions that return a value are called functions (because of their similarity to mathematical functions).  Functions which have no return value are known as *procedures* instead.

Exercise 3
----------

#. Rewrite the ``hypotenuse`` function from exercise 2 so that it returns a value instead of printing it.  Add exception handling so that the function returns ``None`` if it is called with parameters of the wrong type.
#. Call the function with two numbers, and print the result.
#. Call the function with two strings, and print the result.
#. Call the function with a number and a string, and print the result.

The stack
=========

Python stores information about functions which have been called in a *call stack*.  Whenever a function is called, a new *stack frame* is added to the stack -- all of the function's parameters are added to it, and as the body of the function is executed, local variables will be created there.  When the function finishes executing, its stack frame is discarded, and the flow of control returns to wherever you were before you called the function, at the previous level of the stack.

If you recall the section about variable scope from the beginning of the course, this explains a little more about the way that variable names are resolved.  When you use an identifier, Python will first look for it on the current level of the stack, and if it doesn't find it it will check the previous level, and so on -- until either the variable is found or it isn't found anywhere and you get an error.  This is why a local variable will always take precedence over a global variable with the same name.

Python also searches the stack whenever it handles an exception: first it checks if the exception can be handled in the current function, and if it cannot, it terminates the function and tries the next one down -- until either the exception is handled on some level or the program itself has to terminate.  The traceback you see when an exception is printed shows the path that Python took through the stack.

Recursion
---------

We can make a function call itself.  This is known as *recursion*. A common example is a function which calculates numbers in the Fibonacci sequence: the zeroth number is ``0``, the first number is ``1``, and each subsequent number is the sum of the previous two numbers::

    def fibonacci(n):
        if n == 0:
            return 0

        if n == 1:
            return 1

        return fibonacci(n - 1) + fibonacci(n - 2)

Whenever we write a recursive function, we need to include some kind of condition which will allow it to *stop* recursing -- an end case in which the function *doesn't* call itself.  In this example, that happens at the beginning of the sequence: the first two numbers are *not* calculated from any previous numbers -- they are constants.

What would happen if we omitted that condition from our function?  When we got to *n = 2*, we would keep calling the function, trying to calculate ``fibonacci(0)``, ``fibonacci(-1)``, and so on.  In theory, the function would end up recursing forever and never terminate, but in practice the program will crash with a ``RuntimeError`` and a message that we have exceeded the maximum recursion depth.  This is because Python's stack has a finite size -- if we keep placing instances of the function on the stack we will eventually fill it up and cause a *stack overflow*.  Python protects itself from stack overflows by setting a limit on the number of times that a function is allowed to recurse.

Writing fail-safe recursive functions is difficult.  What if we called the function above with a parameter of ``-1``?  We haven't included any error checking which guards against this, so we would skip over the end cases and try to calculate ``fibonacci(-2)``, ``fibonacci(-3)``, and keep going.

Any recursive function can be re-written in an *iterative* way which avoids recursion.  For example::

    def fibonacci(n):
        current, next = 0, 1

        for i in range(n):
            current, next = next, current + next

        return current

This function uses *iteration* to count up to the desired value of *n*, updating variables to keep track of the calculation.  All the iteration happens within a single instance of the function.  Note that we assign new values to both variables at the same time, so that we can use both old values to calculate both new values on the right-hand side.

Exercise 4
----------

#. Write a recursive function which calculates the factorial of a given number.  Use exception handling to raise an appropriate exception if the input parameter is not a positive integer, but allow the user to enter floats as long as they are whole numbers.

Default parameters
==================

The combination of the function name and the number of parameters that it takes is called the *function signature*.  In statically typed languages, there can be multiple functions with the same name in the same scope as long as they have different numbers or types of parameters (in these languages, parameter types and return types are also part of the signature).

In Python, there can only be one function with a particular name defined in the scope -- if you define another function with the same name, you will overwrite the first function.  You must call this function with the correct number of parameters, otherwise you will get an error.

Sometimes there is a good reason to want to have two versions of the same function with different sets of parameters.  You can achieve something similar to this by making some parameters *optional*.  To make a parameter optional, we need to supply a default value for it.  Optional parameters must come after all the required parameters in the function definition::

    def make_greeting(title, name, surname, formal=True):
        if formal:
            return "Hello, %s %s!" % (title, surname)

        return "Hello, %s!" % name

    print(make_greeting("Mr", "John", "Smith"))
    print(make_greeting("Mr", "John", "Smith", False))

When we call the function, we can leave the optional parameter out -- if we do, the default value will be used.  If we include the parameter, our value will override the default value.

We can define multiple optional parameters::

    def make_greeting(title, name, surname, formal=True, time=None):
        if formal:
            fullname =  "%s %s" % (title, surname)
        else:
            fullname = name

        if time is None:
            greeting = "Hello"
        else:
            greeting = "Good %s" % time

        return "%s, %s!" % (greeting, fullname)

    print(make_greeting("Mr", "John", "Smith"))
    print(make_greeting("Mr", "John", "Smith", False))
    print(make_greeting("Mr", "John", "Smith", False, "evening"))

What if we want to pass in the *second* optional parameter, but not the *first*?  So far we have been passing *positional* parameters to all these functions -- a tuple of values which are matched up with parameters in the function signature based on their *positions*.  We can also, however, pass these values in as *keyword* parameters -- we can explicitly specify the parameter names along with the values::

    print(make_greeting(title="Mr", name="John", surname="Smith"))
    print(make_greeting(title="Mr", name="John", surname="Smith", formal=False, time="evening"))

We can mix positional and keyword parameters, but the keyword parameters must come *after* any positional parameters::

    # this is OK
    print(make_greeting("Mr", "John", surname="Smith"))
    # this will give you an error
    print(make_greeting(title="Mr", "John", "Smith"))

We can specify keyword parameters in any order -- they don't have to match the order in the function definition::

    print(make_greeting(surname="Smith", name="John", title="Mr"))

Now we can easily pass in the second optional parameter and not the first::

    print(make_greeting("Mr", "John", "Smith", time="evening"))

Mutable types and default parameters
------------------------------------

We should be careful when using mutable types as default parameter values in function definitions if we intend to modify them in-place::

    def add_pet_to_list(pet, pets=[]):
        pets.append(pet)
        return pets

    list_with_cat = add_pet_to_list("cat")
    list_with_dog = add_pet_to_list("dog")

    print(list_with_cat)
    print(list_with_dog) # oops

Remember that although we can execute a function *body* many times, a function *definition* is executed only once -- that means that the empty list which is created in this function definition will be the same list for all instances of the function.  What we really want to do in this case is to create an empty list inside the function body::

    def add_pet_to_list(pet, pets=None):
        if pets is None:
            pets = []
        pets.append(pet)
        return pets

Exercise 4
----------

#. Write a function called ``calculator``.  It should take the following parameters: two numbers, an arithmetic operation (which can be addition, subtraction, multiplication or division and is addition by default), and an output format (which can be integer or floating point, and is floating point by default).  Division should be floating-point division.

   The function should perform the requested operation on the two input numbers, and return a result in the requested format (if the format is integer, the result should be rounded and not just truncated).  Raise exceptions as appropriate if any of the parameters passed to the function are invalid.

#. Call the function with the following sets of parameters, and check that the answer is what you expect:

    #. ``2``, ``3.0``
    #. ``2``, ``3.0``, output format is integer
    #. ``2``, ``3.0``, operation is division
    #. ``2``, ``3.0``, operation is division, output format is integer

``*args`` and ``**kwargs``
==========================

Sometimes we may want to pass a variable-length list of positional or keyword parameters into a function.  We can put ``*`` before a parameter name to indicate that it is a variable-length tuple of positional parameters, and we can use ``**`` to indicate that a parameter is a variable-length dictionary of keyword parameters.  By convention, the parameter name we use for the tuple is ``args`` and the name we use for the dictionary is ``kwargs``::

    def print_args(*args):
        for arg in args:
            print(arg)

    def print_kwargs(**kwargs):
        for k, v in kwargs.items():
            print("%s: %s" % (k, v))

Inside the function, we can access ``args`` as a normal tuple, but the ``*`` means that ``args`` isn't passed into the function as a single parameter which is a tuple: instead, it is passed in as a series of individual parameters.  Similarly, ``**`` means that ``kwargs`` is passed in as a series of individual keyword parameters, rather than a single parameter which is a dictionary::

    print_args("one", "two", "three")
    print_args("one", "two", "three", "four")

    print_kwargs(name="Jane", surname="Doe")
    print_kwargs(age=10)

We can use ``*`` or ``**`` when we are *calling* a function to *unpack* a sequence or a dictionary into a series of individual parameters::

    my_list = ["one", "two", "three"]
    print_args(*my_list)

    my_dict = {"name": "Jane", "surname": "Doe"}
    print_kwargs(**my_dict)

This makes it easier to build lists of parameters programmatically.  Note that we can use this for *any* function, not just one which uses ``*args`` or ``**kwargs``::

    my_dict = {
        "title": "Mr",
        "name": "John",
        "surname": "Smith",
        "formal": False,
        "time": "evening",
    }

    print(make_greeting(**my_dict))

We can mix ordinary parameters, ``*args`` and ``**kwargs`` in the same function definition. ``*args`` and ``**kwargs`` must come after all the other parameters, and ``**kwargs`` must come after ``*args``.  You cannot have more than one variable-length list parameter or more than one variable dict parameter (recall that you can call them whatever you like)::

    def print_everything(name, time="morning", *args, **kwargs):
        print("Good %s, %s." % (time, name))

        for arg in args:
            print(arg)

        for k, v in kwargs.items():
            print("%s: %s" % (k, v))

If we use a ``*`` expression when you call a function, it must come after all the positional parameters, and if we use a ``**`` expression it must come right at the end::

    def print_everything(*args, **kwargs):
        for arg in args:
            print(arg)

        for k, v in kwargs.items():
            print("%s: %s" % (k, v))

    # we can write all the parameters individually
    print_everything("cat", "dog", day="Tuesday")

    t = ("cat", "dog")
    d = {"day": "Tuesday"}

    # we can unpack a tuple and a dictionary
    print_everything(*t, **d)
    # or just one of them
    print_everything(*t, day="Tuesday")
    print_everything("cat", "dog", **d)

    # we can mix * and ** with explicit parameters
    print_everything("Jane", *t, **d)
    print_everything("Jane", *t, time="evening", **d)
    print_everything(time="evening", *t, **d)

    # none of these are allowed:
    print_everything(*t, "Jane", **d)
    print_everything(*t, **d, time="evening")

If a function takes only ``*args`` and ``**kwargs`` as its parameters, it can be called with *any set of parameters*.  One or both of ``args`` and ``kwargs`` can be empty, so the function will accept any combination of positional and keyword parameters, including no parameters at all.  This can be useful if we are writing a very generic function, like ``print_everything`` in the example above.

Exercise 5
----------

#. Rewrite the calculator function from exercise 4 so that it takes any number of number parameters as well as the same optional keyword parameters.  The function should apply the operation to the first two numbers, and then apply it again to the result and the next number, and so on. For example, if the numbers are ``6``, ``4``, ``9`` and ``1`` and the operation is subtraction the function should return ``6 - 4 - 9 - 1``.  If only one number is entered, it should be returned unmodified.  If no numbers are entered, raise an exception.

Decorators
==========

Sometimes we may need to modify several functions in the same way -- for example, we may want to perform a particular action before and after executing each of the functions, or pass in an extra parameter, or convert the output to another format.

We may also have good reasons not to write the modification into all the functions -- maybe it would make the function definitions very verbose and unwieldy, and maybe we would like the option to apply the modification quickly and easily to any function (and remove it just as easily).

To solve this problem, we can write a function which modifies functions.  We call a function like this a *decorator*.  Our function will take a function object as a parameter, and will return a new function object -- we can then assign the new function value to the old function's name to replace the old function with the new function.  For example, here is a decorator which logs the function name and its arguments to a log file whenever the function is used::

    # we define a decorator
    def log(original_function):
        def new_function(*args, **kwargs):
            with open("log.txt", "w") as logfile:
                logfile.write("Function '%s' called with positional arguments %s and keyword arguments %s.\n" % (original_function.__name__, args, kwargs))

            return original_function(*args, **kwargs)

        return new_function

    # here is a function to decorate
    def my_function(message):
        print(message)

    # and here is how we decorate it
    my_function = log(my_function)

Inside our decorator (the outer function) we define a replacement function and return it.  The replacement function (the inner function) writes a log message and then simply calls the original function and returns its value.

Note that the decorator function is only called once, when we replace the original function with the decorated function, but that the inner function will be called every time we use ``my_function``.  The inner function can access both variables in its own scope (like ``args`` and ``kwargs``) and variables in the decorator's scope (like ``original_function``).

Because the inner function takes ``*args`` and ``**kwargs`` as its parameters, we can use this decorator to decorate any function, no matter what its parameter list is.  The inner function accepts any parameters, and simply passes them to the original function.  We will still get an error inside the original function if we pass in the wrong parameters.

There is a shorthand syntax for applying decorators to functions: we can use the ``@`` symbol together with the decorator name before the definition of each function that we want to decorate::

    @log
    def my_function(message):
        print(message)

``@log`` before the function definition means exactly the same thing as ``my_function = log(my_function)`` after the function definition.

We can pass additional parameters to our decorator.  For example, we may want to specify a custom log file to use in our logging decorator::

    def log(original_function, logfilename="log.txt"):
        def new_function(*args, **kwargs):
            with open(logfilename, "w") as logfile:
                logfile.write("Function '%s' called with positional arguments %s and keyword arguments %s.\n" % (original_function.__name__, args, kwargs))

            return original_function(*args, **kwargs)

        return new_function

    @log("someotherfilename.txt")
    def my_function(message):
        print(message)

Python has several built-in decorators which are commonly used to decorate class methods.  We will learn about them in the next chapter.

.. Note:: A decorator doesn't have to be a function -- it can be any callable object.  Some people prefer to write decorators as classes.

Exercise 6
----------

#. Rewrite the ``log`` decorator example so that the decorator logs both the function name and parameters and the returned result.

#. Test the decorator by applying it to a function which takes two arguments and returns their sum.  Print the result of the function, and what was logged to the file.

Lambdas
=======

We have already seen that when we want to use a number or a string in our program we can either write it as a *literal* in the place where we want to use it or use a *variable* that we have already defined in our code.  For example, ``print("Hello!")`` prints the literal string ``"Hello!"``, which we haven't stored in a variable anywhere, but ``print(message)`` prints whatever string is stored in the variable ``message``.

We have also seen that we can store a function in a variable, just like any other object, by referring to it by its name (but not calling it).  Is there such a thing as a function literal?  Can we define a function on the fly when we want to pass it as a parameter or assign it to a variable, just like we did with the string ``"Hello!"``?

The answer is *yes*, but only for very simple functions.  We can use the ``lambda`` keyword to define anonymous, one-line functions *inline* in our code::

    a = lambda: 3

    # is the same as

    def a():
        return 3

Lambdas can take parameters -- they are written between the ``lambda`` keyword and the colon, without brackets.  A lambda function may only contain a single expression, and the result of evaluating this expression is implicitly returned from the function (we don't use the ``return`` keyword)::

    b = lambda x, y: x + y

    # is the same as

    def b(x, y):
        return x + y

Lambdas should only be used for very simple functions. If your lambda starts looking too complicated to be readable, you should rather write it out in full as a normal, named function.

Exercise 7
----------

#. Define the following functions as lambdas, and assign them to variables:

    #. Take one parameter; return its square
    #. Take two parameters; return the square root of the sums of their squares
    #. Take any number of parameters; return their average
    #. Take a string parameter; return a string which contains the unique letters in the input string (in any order)

#. Rewrite all these functions as named functions.

Generator functions and ``yield``
=================================

We have already encountered generators -- sequences in which new elements are generated as they are needed, instead of all being generated up-front.  We can create our own generators by writing functions which make use of the ``yield`` statement.

Consider this simple function which returns a range of numbers as a list::

    def my_list(n):
        i = 0
        l = []

        while i < n:
            l.append(i)
            i += 1

        return l

This function builds the full list of numbers and returns it.  We can change this function into a generator function while preserving a very similar syntax, like this::

    def my_gen(n):
        i = 0

        while i < n:
            yield i
            i += 1

The first important thing to know about the ``yield`` statement is that if we use it in a function, that function will return a generator.  We can test this by using the ``type`` function on the return value of ``my_gen``. We can also try using it in a ``for`` loop, like we would use any other generator, to see what sequence the generator represents::

    g = my_gen(3)

    print(type(g))

    for x in g:
        print(x)

What does the ``yield`` statement do?  Whenever a new value is requested from the generator, for example by our ``for`` loop in the example above, the generator begins to execute the function until it reaches the ``yield`` statement. The ``yield`` statement causes the generator to return a single value.

After the ``yield`` statement is executed, execution of the function does not end -- when the *next* value is requested from the generator, it will go back to the beginning of the function and execute it *again*.

If the generator executes the entire function without encountering a ``yield`` statement, it will raise a ``StopIteration`` exception to indicate that there are no more values.  A ``for`` loop automatically handles this exception for us.  In our ``my_gen`` function this will happen when ``i`` becomes equal to ``n`` -- when this happens, the ``yield`` statement inside the ``while`` loop will no longer be executed.

Exercise 8
----------

#. Write a generator function which takes an integer ``n`` as a parameter.  The function should return a generator which counts *down* from ``n`` to ``0``.  Test your function using a ``for`` loop.

Answers to exercises
====================

Answer to exercise 1
--------------------

Here is an example program::

    def func_a():
        print("This is my awesome function.")

    func_a()

    b = func_a

    b()

Answer to exercise 2
--------------------

Here is an example program::

    import math

    def hypotenuse(x, y):
        print(math.sqrt(x**2 + y**2))

    hypotenuse(12.3, 45.6)
    hypotenuse(12, 34)
    hypotenuse(12, 34.5)

Answer to exercise 3
--------------------

Here is an example program::

    import math

    def hypotenuse(x, y):
        try:
            return math.sqrt(x**2 + y**2)
        except TypeError:
            return None

    print(hypotenuse(12, 34))
    print(hypotenuse("12", "34"))
    print(hypotenuse(12, "34"))

Answer to exercise 3
--------------------

#. Here is an example program::

    def factorial(n):
        ni = int(n)

        if ni != n or ni <= 0:
            raise ValueError("%s is not a positive integer." % n)

        if ni == 1:
            return 1

        return ni * factorial(ni - 1)

Answer to exercise 4
--------------------

#. Here is an example program::

    import math

    ADD, SUB, MUL, DIV = range(4)

    def calculator(a, b, operation=ADD, output_format=float):
        if operation == ADD:
            result = a + b
        elif operation == SUB:
            result = a - b
        elif operation == MUL:
            result = a * b
        elif operation == DIV:
            result = a / b
        else:
            raise ValueError("Operation must be ADD, SUB, MUL or DIV.")

        if output_format == float:
            result = float(result)
        elif output_format == int:
            result = math.round(result)
        else:
            raise ValueError("Format must be float or int.")

        return result

#. You should get the following results:

    #. ``5.0``
    #. ``5``
    #. ``0.6666666666666666``
    #. ``1``

Answer to exercise 5
--------------------

#. Here is an example program::

    import math

    ADD, SUB, MUL, DIV = range(4)

    def calculator(operation=ADD, output_format=float, *args):
        if not args:
            raise ValueError("At least one number must be entered.")

        result = args[0]

        for n in args[1:]:
            if operation == ADD:
                result += n
            elif operation == SUB:
                result -= n
            elif operation == MUL:
                result *= n
            elif operation == DIV:
                result /= n
            else:
                raise ValueError("Operation must be ADD, SUB, MUL or DIV.")

        if output_format == float:
            result = float(result)
        elif output_format == int:
            result = math.round(result)
        else:
            raise ValueError("Format must be float or int.")

        return result

Answer to exercise 6
--------------------

#. Here is an example program::

    def log(original_function, logfilename="log.txt"):
        def new_function(*args, **kwargs):
            result = original_function(*args, **kwargs)

            with open(logfilename, "w") as logfile:
                logfile.write("Function '%s' called with positional arguments %s and keyword arguments %s. The result was %s.\n" % (original_function.__name__, args, kwargs, result))

            return result

        return new_function

#. Here is an example program::

    @log
    def add(x, y):
        return x + y

    print(add(3.5, 7))

    with open("log.txt", "r") as logfile:
        print(logfile.read())

Answer to exercise 7
--------------------

#. Here is an example program::

    import math

    a = lambda x: x**2
    b = lambda x, y: math.sqrt(x**2 + y**2)
    c = lambda *args: sum(args)/len(args)
    d = lambda s: "".join(set(s))

#. Here is an example program::

    import math

    def a(x):
        return x**2

    def b(x, y):
        return math.sqrt(x**2 + y**2)

    def c(*args):
        return sum(args)/len(args)

    def d(s):
        return "".join(set(s))

Answer to exercise 8
--------------------

#. Here is an example program::

    def my_gen(n):
        i = n

        while i >= 0:
            yield i
            i -= 1

    for x in my_gen(3):
        print(x)
