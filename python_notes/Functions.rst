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

    # todo

.. Note:: in some other languages, only functions that return a value are called functions (because of their similarity to mathematical functions).  Functions which have no return value are known as *procedures* instead.

Default parameters
------------------

* default parameters
* args and kwargs
* function scope
* recursion?
* decorators