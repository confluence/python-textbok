*********
Functions
*********

A function is a sequence of statements which performs some kind of task.  We use functions to eliminate code duplication -- instead of  writing all the statements at every place in our code where we want to perform the same task, we define them in one place and refer to them by the function name.  If we want to change how that task is performed, we will now mostly only need to change code in one place.

Here is a definition of a simple function which takes no parameters and doesn't return any values::

    def print_a_message():
        print("Hello, world!")

We use the ``def`` statement to indicate the start of a function definition. The next part of the definition is the function name, in this case ``print_a_message``, followed by round brackets (the definitions of any parameters that the function takes will go in between them) and a colon.  Thereafter, everything that is indented by one level is the body of the function.

Functions *do things*, so you should always choose a function name which explains as simply as accurately as possible *what the function does*.  This will usually be a verb or some phrase containing a verb.  If you change a function so much that the name no longer accurately reflects what it does, you should consider updating the name -- although this may sometimes be inconvenient.

This particular function always does exactly the same thing: it prints the message ``"Hello, world!"``. To call the function we use its name followed by round brackets (with any parameters that the function takes in between them)::

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

Input parameters
----------------

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

This is why it is important for us to test our code thoroughly -- something we will look at in a later chapter. If we intend to write code which is robust, especially if it is also going to be used by other people, it is also often a good idea to check function parameters early in the function and give the user feedback (by raising exceptions) if it is incorrect.

Return values
-------------

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

Default parameters
------------------

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

``*args`` and ``**kwargs``
--------------------------

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

This makes it easier to build lists of parameters programatically.  Note that we can use this for *any* function, not just one which uses ``*args`` or ``**kwargs``::

    my_dict = {
        "title": "Mr",
        "name": "John",
        "surname": "Smith",
        "formal": False,
        "time": "evening",
    }

    print(make_greeting(**my_dict))

We can mix ordinary parameters, ``*args`` and ``**kwargs`` in the same function.  In the function definition, ``*args`` and ``**kwargs`` must come after all the other parameters, and ``**kwargs`` must come after ``*args``.  You cannot have more than one variable-length list parameter or more than one variable dict parameter (recall that you can call them whatever you like)::


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

.. Todo:: are these actually the right rules? How do function signatures work with args, kwargs and inheritance?

Function scope
--------------

Recursion
---------

* brief example

Decorators
----------

* brief example, and examples of existing decorators?  Just a note that method decorators will be discussed in next chapter?

.. Todo:: Exercises