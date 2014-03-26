*******
Classes
*******

We have already seen how we can use a dictionary to group related data together, and how we can use functions to create shortcuts for commonly used groups of statements.  A function performs an action using some set of input parameters.  Not all functions are applicable to all kinds of data.  *Classes* are a way of grouping together related data *and* functions which act upon that data.

A class is a kind of data type, just like a string, integer or list.  When we create an object of that data type, we call it an *instance* of a class.

As we have already mentioned, in some other languages some entities are objects and some are not.  In Python, everything is an object -- everything is an instance of some class.  In earlier versions of Python a distinction was made between built-in types and user-defined classes, but these are now completely indistinguishable.  Classes and types are themselves objects, and they are of type ``type``.  You can find out the type of any object using the ``type`` function::

    type(any_object)

The data values which we store inside an object are called *attributes*, and the functions which are associated with the object are called *methods*.  We have already used the methods of some built-in objects, like strings and lists.

When we design our own objects, we have to decide how we are going to group things together, and what our objects are going to represent.

Sometimes we write objects which map very intuitively onto things in the real world.  For example, if we are writing code to simulate chemical reactions, we might have ``Atom`` objects which we can combine to make a ``Molecule`` object.  However, it isn't always necessary, desirable or even possible to make all code objects perfectly analogous to their real-world counterparts.

Sometimes we may create objects which don't have any kind of real-world equivalent, just because it's useful to group certain functions together.

Defining and using a class
==========================

Here is an example of a simple custom class which stores information about a person::

    import datetime # we will use this for date objects

    class Person:

        def __init__(self, name, surname, birthdate, address, telephone, email):
            self.name = name
            self.surname = surname
            self.birthdate = birthdate

            self.address = address
            self.telephone = telephone
            self.email = email

        def age(self):
            today = datetime.date.today()
            age = today.year - self.birthdate.year

            if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
                age -= 1

            return age

    person = Person(
        "Jane",
        "Doe",
        datetime.date(1992, 3, 12), # year, month, day
        "No. 12 Short Street, Greenville",
        "555 456 0987",
        "jane.doe@example.com"
    )

    print(person.name)
    print(person.email)
    print(person.age())

We start the class definition with the ``class`` keyword, followed by the class name and a colon.  We would list any parent classes in between round brackets before the colon, but this class doesn't have any, so we can leave them out.

Inside the class body, we define two functions -- these are our object's methods.  The first is called ``__init__``, which is a special method.  When we call the class object, a new instance of the class is created, and the ``__init__`` method on this new object is immediately executed with all the parameters that we passed to the class object.  The purpose of this method is thus to set up a new object using data that we have provided.

The second method is a custom method which calculates the age of our person using the birthdate and the current date.

.. Note:: ``__init__`` is sometimes called the object's *constructor*, because it is used similarly to the way that constructors are used in other languages, but that is not technically correct -- it's better to call it the *initialiser*.  There is a different method called ``__new__`` which is more analogous to a constructor, but it is hardly ever used.

You may have noticed that both of these method definitions have ``self`` as the first parameter, and we use this variable inside the method bodies -- but we don't appear to pass this parameter in.  This is because whenever we call a method on an object, *the object itself* is automatically passed in as the first parameter.  This gives us a way to access the object's properties from inside the object's methods.

In some languages this parameter is *implicit* -- that is, it is not visible in the function signature -- and we access it with a special keyword.  In Python it is explicitly exposed.  It doesn't have to be called ``self``, but this is a very strongly followed convention.

Now you should be able to see that our ``__init__`` function creates attributes on the object and sets them to the values we have passed in as parameters.  We use the same names for the attributes and the parameters, but this is not compulsory.

The ``age`` function doesn't take any parameters except ``self`` -- it only uses information stored in the object's attributes, and the current date (which it retrieves using the ``datetime`` module).

Note that the ``birthdate`` attribute is itself an object. The ``date`` class is defined in the ``datetime`` module, and we create a new instance of this class to use as the birthdate parameter when we create an instance of the ``Person`` class. We don't have to assign it to an intermediate variable before using it as a parameter to ``Person``; we can just create it when we call ``Person``, just like we create the string literals for the other parameters.

Remember that defining a function doesn't make the function run.  Defining a class also doesn't make anything run -- it just tells Python about the class.  The class will not be defined until Python has executed the entirety of the definition, so you can be sure that you can reference any method from any other method on the same class, or even reference the class inside a method of the class.  By the time you call that method, the entire class will definitely be defined.

Exercise 1
----------

#. Explain what the following variables refer to, and their scope:

    #. ``Person``
    #. ``person``
    #. ``surname``
    #. ``self``
    #. ``age`` (the function name)
    #. ``age`` (the variable used inside the function)
    #. ``self.email``
    #. ``person.email``

Instance attributes
===================

It is important to note that the attributes set on the object in the ``__init__`` function do not form an exhaustive list of all the attributes that our object is ever allowed to have.

In some languages you must provide a list of the object's attributes in the class definition, placeholders are created for these allowed attributes when the object is created, and you may not add new attributes to the object later.  In Python, you can add new attributes, and even new methods, to an object on the fly.  In fact, there is nothing special about the ``__init__`` function when it comes to setting attributes.  We could store a cached age value on the object from inside the ``age`` function::

    def age(self):
        if hasattr(self, "_age"):
            return self._age

        today = datetime.date.today()

        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        self._age = age
        return age

.. Note:: Starting an attribute or method name with an underscore (``_``) is a convention which we use to indicate that it is a "private" internal property and should not be accessed directly.  In a more realistic example, our cached value would sometimes expire and need to be recalculated -- so we should always use the ``age`` method to make sure that we get the right value.

We could even add a completely unrelated attribute from outside the object::

    person.pets = ['cat', 'cat', 'dog']

It is very common for an object's methods to *update* the values of the object's attributes, but it is considered bad practice to *create* new attributes in a method without initialising them in the ``__init__`` method.  Setting arbitrary properties from outside the object is frowned upon even more, since it breaks the object-oriented paradigm (which we will discuss in the next chapter).

The ``__init__`` method will definitely be executed before anything else when we create the object -- so it's a good place to do all of our initialisation of the object's data.  If we create a new attribute outside the ``__init__`` method, we run the risk that we will try to use it before it has been initialised.

In the ``age`` example above we have to check if an ``_age`` attribute exists on the object before we try to use it, because if we haven't run the ``age`` method before it will not have been created yet. It would be much tidier if we called this method at least once from ``__init__``, to make sure that ``_age`` is created as soon as we create the object.

Initialising all our attributes in ``__init__``, even if we just set them to empty values, makes our code less error-prone. It also makes it easier to read and understand -- we can see at a glance what attributes our object has.

An ``__init__`` method doesn't have to take any parameters (except ``self``) and it can be completely absent.

``getattr``, ``setattr`` and ``hasattr``
----------------------------------------

What if we want to get or set the value of an attribute of an object without hard-coding its name?  We may sometimes want to loop over several attribute names and perform the same operation on all of them, as we do in this example which uses a dictionary::

    for key in ["a", "b", "c"]:
        print(mydict[key])

How can we do something similar with an object?  We can't use the ``.`` operator, because it must be followed by the attribute name as a bare word.  If our attribute name is stored as a string value in a variable, we have to use the ``getattr`` function to retrieve the attribute value from an object::

    for key in ["a", "b", "c"]:
        print(getattr(myobject, key, None))

Note that ``getattr`` is a built-in function, not a method on the object: it takes the object as its first parameter.  The second parameter is the name of the variable as a string, and the optional third parameter is the default value to be returned if the attribute does not exist.  If we do not specify a default value, ``getattr`` will raise an exception if the attribute does not exist.

Similarly, ``setattr`` allows us to set the value of an attribute.  In this example, we copy data from a dictionary to an object::

    for key in ["a", "b", "c"]:
        setattr(myobject, key, mydict[key])

The first parameter of ``setattr`` is the object, the second is the name of the function, and the third is the new value for the attribute.

As we saw in the previous ``age`` function example, ``hasattr`` detects whether an attribute exists.

There's nothing preventing us from using ``getattr`` on attributes even if the name can be hard-coded, but this is not recommended: it's an unnecessarily verbose and round-about way of accessing attributes::

    getattr(myobject, "a")

    # means the same thing as

    myobject.a

You should only use these functions if you have a good reason to do so.

Exercise 2
----------

#. Rewrite the ``Person`` class so that a person's age is calculated for the first time when a new person instance is created, and recalculated (when it is requested) if the day has changed since the last time that it was calculated.

Class attributes
================

All the attributes which are defined on a ``Person`` instance are *instance attributes* -- they are added to the instance when the ``__init__`` method is executed.  We can, however, also define attributes which are set on the *class*.  These attributes will be shared by all instances of that class.  In many ways they behave just like instance attributes, but there are some caveats that you should be aware of.

We define class attributes in the body of a class, at the same indentation level as method definitions (one level up from the insides of methods)::

    class Person:

        TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

        def __init__(self, title, name, surname):
            if title not in self.TITLES:
                raise ValueError("%s is not a valid title." % title)

            self.title = title
            self.name = name
            self.surname = surname

As you can see, we access the class attribute ``TITLES`` just like we would access an instance attribute -- it is made available as a property on the instance object, which we access inside the method through the ``self`` variable.

All the ``Person`` objects we create will share the same ``TITLES`` class attribute.

Class attributes are often used to define constants which are closely associated with a particular class.  Although we can use class attributes from class instances, we can also use them from class objects, without creating an instance::

    # we can access a class attribute from an instance
    person.TITLES

    # but we can also access it from the class
    Person.TITLES

Note that the class object doesn't have access to any *instance* attributes -- those are only created when an instance is created! ::

    # This will give us an error
    Person.name
    Person.surname

Class attributes can also sometimes be used to provide default attribute values::

    class Person:
        deceased = False

        def mark_as_deceased(self):
            self.deceased = True

When we set an attribute on an instance which has the same name as a class attribute, we are *overriding* the class attribute with an instance attribute, which will take precedence over it. If we create two ``Person`` objects and call the ``mark_as_deceased`` method on one of them, we will not affect the other one.  We should, however, be careful when a class attribute is of a mutable type -- because if we modify it in-place, we *will* affect all objects of that class at the same time. Remember that all instances share the same class attributes::

    class Person:
        pets = []

        def add_pet(self, pet):
            self.pets.append(pet)

    jane = Person()
    bob = Person()

    jane.add_pet("cat")
    print(jane.pets)
    print(bob.pets) # oops!

What we *should* do in cases like this is initialise the mutable attribute *as an instance attribute*, inside ``__init__``.  Then every instance will have its own separate copy::

    class Person:

        def __init__(self):
            self.pets = []

        def add_pet(self, pet):
            self.pets.append(pet)

    jane = Person()
    bob = Person()

    jane.add_pet("cat")
    print(jane.pets)
    print(bob.pets)

Note that method definitions are in the same scope as class attribute definitions, so we can use class attribute names as variables in method definitions (without ``self``, which is only defined *inside* the methods)::

    class Person:
        TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

        def __init__(self, title, name, surname, allowed_titles=TITLES):
            if title not in allowed_titles:
                raise ValueError("%s is not a valid title." % title)

            self.title = title
            self.name = name
            self.surname = surname

Can we have class *methods*? Yes, we can.  In the next section we will see how to define them using a decorator.

Exercise 3
----------

#. Explain the differences between the attributes ``name``, ``surname`` and ``profession``, and what values they can have in different instances of this class::

    class Smith:
        surname = "Smith"
        profession = "smith"

        def __init__(self, name, profession=None):
            self.name = name
            if profession is not None:
                self.profession = profession

Class decorators
================

In the previous chapter we learned about decorators -- functions which are used to modify the behaviour of other functions.  There are some built-in decorators which are often used in class definitions.

``@classmethod``
----------------

Just like we can define class *attributes*, which are shared between all instances of a class, we can define class *methods*.  We do this by using the ``@classmethod`` decorator to decorate an ordinary method.

A class method still has its calling object as the first parameter, but by convention we rename this parameter from ``self`` to ``cls``.  If we call the class method from an instance, this parameter will contain the instance object, but if we call it from the class it will contain the class object.  By calling the parameter ``cls`` we remind ourselves that it is not guaranteed to have any *instance* attributes.

What are class methods good for?  Sometimes there are tasks associated with a class which we can perform using constants and other class attributes, without needing to create any class instances.  If we had to use instance methods for these tasks, we would need to create an instance for no reason, which would be wasteful.  Sometimes we write classes purely to group related constants together with functions which act on them -- we may never instantiate these classes at all.

Sometimes it is useful to write a class method which creates an instance of the class after processing the input so that it is in the right format to be passed to the class constructor.  This allows the constructor to be straightforward and not have to implement any complicated parsing or clean-up code::

    class Person:

        def __init__(self, name, surname, birthdate, address, telephone, email):
            self.name = name
            # (...)

        @classmethod
        def from_text_file(cls, filename):
            # extract all the parameters from the text file
            return cls(*params) # this is the same as calling Person(*params)

``@staticmethod``
-----------------

A static method doesn't have the calling object passed into it as the first parameter.  This means that it doesn't have access to the rest of the class or instance at all.  We can call them from an instance or a class object, but they are most commonly called from class objects, like class methods.

If we are using a class to group together related methods which don't need to access each other or any other data on the class, we may want to use this technique.  The advantage of using static methods is that we eliminate unnecessary ``cls`` or ``self`` parameters from our method definitions.  The disadvantage is that if we do occasionally want to refer to another class method or attribute inside a static method we have to write the class name out in full, which can be much more verbose than using the ``cls`` variable which is available to us inside a class method.

Here is a brief example comparing the three method types::

    class Person:
        TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

        def __init__(self, name, surname):
            self.name = name
            self.surname = surname

        def fullname(self): # instance method
            # instance object accessible through self
            return "%s %s" % (self.name, self.surname)

        @classmethod
        def allowed_titles_starting_with(cls, startswith): # class method
            # class or instance object accessible through cls
            return [t for t in cls.TITLES if t.startswith(startswith)]

        @staticmethod
        def allowed_titles_ending_with(endswith): # static method
            # no parameter for class or instance object
            # we have to use Person directly
            return [t for t in Person.TITLES if t.endswith(endswith)]


    jane = Person("Jane", "Smith")

    print(jane.fullname())

    print(jane.allowed_titles_starting_with("M"))
    print(Person.allowed_titles_starting_with("M"))

    print(jane.allowed_titles_ending_with("s"))
    print(Person.allowed_titles_ending_with("s"))

``@property``
--------------

Sometimes we use a method to generate a property of an object dynamically, calculating it from the object's other properties.  Sometimes you can simply use a method to access a single attribute and return it.  You can also use a different method to update the value of the attribute instead of accessing it directly.  Methods like this are called *getters* and *setters*, because they "get" and "set" the values of attributes, respectively.

In some languages you are encouraged to use getters and setters for all attributes, and never to access their values directly -- and there are language features which can make attributes inaccessible except through setters and getters.  In Python, accessing simple attributes directly is perfectly acceptable, and writing getters and setters for all of them is considered unnecessarily verbose.  Setters can be inconvenient because they don't allow use of compound assignment operators::

    class Person:
        def __init__(self, height):
            self.height = height

        def get_height(self):
            return self.height

        def set_height(self, height):
            self.height = height

    jane = Person(153) # Jane is 153cm tall

    jane.height += 1 # Jane grows by a centimetre
    jane.set_height(jane.height + 1) # Jane grows again

As we can see, incrementing the height attribute through a setter is much more verbose. Of course we could write a *second* setter which increments the attribute by the given parameter -- but we would have to do something similar for every attribute and every kind of modification that we want to perform.  We would have a similar issue with in-place modifications, like adding values to lists.

Something which is often considered an *advantage* of setters and getters is that we can change the way that an attribute is generated inside the object without affecting any code which uses the object.  For example, suppose that we initially created a ``Person`` class which has a ``fullname`` attribute, but later we want to change the class to have separate ``name`` and ``surname`` attributes which we combine to create a full name.  If we always access the ``fullname`` attribute through a setter, we can just rewrite the setter -- none of the code which calls the setter will have to be changed.

But what if our code accesses the ``fullname`` attribute directly?  We can write a ``fullname`` method which returns the right value, but a method has to be *called*.  Fortunately, the ``@property`` decorator lets us make a method behave like an attribute::

    class Person:
        def __init__(self, name, surname):
            self.name = name
            self.surname = surname

        @property
        def fullname(self):
            return "%s %s" % (self.name, self.surname)

    jane = Person("Jane", "Smith")
    print(jane.fullname) # no brackets!

There are also decorators which we can use to define a setter and a deleter for our attribute (a deleter will delete the attribute from our object). The getter, setter and deleter methods must all have the same name::

    class Person:
        def __init__(self, name, surname):
            self.name = name
            self.surname = surname

        @property
        def fullname(self):
            return "%s %s" % (self.name, self.surname)

        @fullname.setter
        def fullname(self, value):
            # this is much more complicated in real life
            name, surname = value.split(" ", 1)
            self.name = name
            self.surname = surname

        @fullname.deleter
        def fullname(self):
            del self.name
            del self.surname

    jane = Person("Jane", "Smith")
    print(jane.fullname)

    jane.fullname = "Jane Doe"
    print(jane.fullname)
    print(jane.name)
    print(jane.surname)

Exercise 4
----------

#. Create a class called ``Numbers``, which has a single class attribute called ``MULTIPLIER``, and a constructor which takes the parameters ``x`` and ``y`` (these should all be numbers).

    #. Write a method called ``add`` which returns the sum of the attributes ``x`` and ``y``.
    #. Write a class method called ``multiply``, which takes a single number parameter ``a`` and returns the product of ``a`` and ``MULTIPLIER``.
    #. Write a static method called ``subtract``, which takes two number parameters, ``b`` and ``c``, and returns ``b`` - ``c``.
    #. Write a method called ``value`` which returns a tuple containing the values of ``x`` and ``y``. Make this method into a property, and write a setter and a deleter for manipulating the values of ``x`` and ``y``.

Inspecting an object
====================

We can check what properties are defined on an object using the ``dir`` function::

    class Person:
        def __init__(self, name, surname):
            self.name = name
            self.surname = surname

        def fullname(self):
            return "%s %s" % (self.name, self.surname)

    jane = Person("Jane", "Smith")

    print(dir(jane))

Now we can see our attributes and our method -- but what's all that other stuff?  We will discuss *inheritance* in the next chapter, but for now all you need to know is that any class that you define has ``object`` as its parent class even if you don't explicitly say so -- so your class will have a lot of default attributes and methods that any Python object has.

.. Note:: in Python 2 we have to inherit from ``object`` explicitly, otherwise our class will be almost completely empty except for our own custom properties.  Classes which don't inherit from ``object`` are called "old-style classes", and using them is not recommended.  If we were to write the person class in Python 2 we would write the first line as ``class Person(object):``.

This is why you can just leave out the ``__init__`` method out of your class if you don't have any initialisation to do -- the default that you inherited from ``object`` (which does nothing) will be used instead.  If you do write your own ``__init__`` method, it will *override* the default method.  Sometimes we also call this *overloading*.

Many default methods and attributes that are found in built-in Python objects have names which begin and end in double underscores, like ``__init__`` or ``__str__``.  These names indicate that these properties have a special meaning -- you shouldn't create your own methods or attributes with the same names unless you mean to overload them.  These properties are usually methods, and they are sometimes called *magic methods*.

We can use ``dir`` on any object. You can try to use it on all kinds of objects which we have already seen before, like numbers, lists, strings and functions, to see what built-in properties these objects have in common.

Here are some examples of special object properties:

* ``__init__``: the initialisation method of an object, which is called when the object is created.
* ``__str__``: the string representation method of an object, which is called when you use the ``str`` function to convert that object to a string.
* ``__class__``: an attribute which stores the the class (or type) of an object -- this is what is returned when you use the ``type`` function on the object.
* ``__eq__``: a method which determines whether this object is equal to another.  There are also other methods for determining if it's not equal, less than, etc.. These methods are used in object comparisons, for example when we use the equality operator ``==`` to check if two objects are equal.
* ``__add__`` is a method which allows this object to be added to another object. There are equivalent methods for all the other arithmetic operators.  Not all objects support all arithemtic operations -- numbers have all of these methods defined, but other objects may only have a subset.
* ``__iter__``: a method which returns an iterator over the object -- we will find it on strings, lists and other iterables.  It is executed when we use the ``iter`` function on the object.
* ``__len__``: a method which calculates the length of an object -- we will find it on sequences.  It is executed when we use the ``len`` function of an object.
* ``__dict__``: a dictionary which contains all the instance attributes of an object, with their names as keys.  It can be useful if we want to iterate over all the attributes of an object. ``__dict__`` does not include any methods, class attributes or special default attributes like ``__class__``.

Exercise 5
----------

#. Create an instance of the ``Person`` class from example 2.  Use the ``dir`` function on the instance.  Then use the ``dir`` function on the class.

    #. What happens if you call the ``__str__`` method on the instance? Verify that you get the same result if you call the ``str`` function with the instance as a parameter.
    #. What is the type of the instance?
    #. What is the type of the class?
    #. Write a function which prints out the names and values of all the custom attributes of any object that is passed in as a parameter.

Overriding magic methods
========================

We have already seen how to overload the ``__init__`` method so that we can customise it to initialise our class.  We can also overload other special methods.  For example, the purpose of the ``__str__`` method is to output a useful string representation of our object. but by default if we use the ``str`` function on a person object (which will call the ``__str__`` method), all that we will get is the class name and an ID. That's not very useful!  Let's write a custom ``__str__`` method which shows the values of all of the object's properties::

    import datetime

    class Person:
        def __init__(self, name, surname, birthdate, address, telephone, email):
            self.name = name
            self.surname = surname
            self.birthdate = birthdate

            self.address = address
            self.telephone = telephone
            self.email = email

        def __str__(self):
            return "%s %s, born %s\nAddress: %s\nTelephone: %s\nEmail:%s" % (self.name, self.surname, self.birthdate, self.address, self.telephone, self.email)

    jane = Person(
        "Jane",
        "Doe",
        datetime.date(1992, 3, 12), # year, month, day
        "No. 12 Short Street, Greenville",
        "555 456 0987",
        "jane.doe@example.com"
    )

    print(jane)

Note that when we insert the birthdate object into the output string with ``%s`` it will itself be converted to a string, so we don't need to do it ourselves (unless we want to change the format).

It is also often useful to overload the comparison methods, so that we can use comparison operators on our person objects.  By default, our person objects are only equal if they are the same object, and you can't test whether one person object is greater than another because person objects have no default order.

Suppose that we want our person objects to be equal if all their attributes have the same values, and we want to be able to order them alphabetically by surname and then by first name.  All of the magic comparison methods are independent of each other, so we will need to overload all of them if we want all of them to work -- but fortunately once we have defined equality and one of the basic order methods the rest are easy to do.  Each of these methods takes two parameters -- ``self`` for the current object, and ``other`` for the other object::

    class Person:
        def __init__(self, name, surname):
            self.name = name
            self.surname = surname

        def __eq__(self, other): # does self == other?
            return self.name == other.name and self.surname == other.surname

        def __gt__(self, other): # is self > other?
            if self.surname == other.surname:
                return self.name > other.name
            return self.surname > other.surname

        # now we can define all the other methods in terms of the first two

        def __ne__(self, other): # does self != other?
            return not self == other # this calls self.__eq__(other)

        def __le__(self, other): # is self <= other?
            return not self > other # this calls self.__gt__(other)

        def __lt__(self, other): # is self < other?
            return not (self > other or self == other)

        def __ge__(self, other): # is self >= other?
            return not self < other

Note that ``other`` is not guaranteed to be another person object, and we haven't put in any checks to make sure that it is.  Our method will crash if the other object doesn't have a ``name`` or ``surname`` attribute, but if they are present the comparison will work.  Whether that makes sense or not is something that we will need to think about if we create similar types of objects.

Sometimes it makes sense to exit with an error if the other object is not of the same type as our object, but sometimes we can compare two compatible objects even if they are not of the same type.  For example, it makes sense to compare ``1`` and ``2.5`` because they are both numbers, even though one is an integer and the other is a float.

.. Note:: Python 2 also has a ``__cmp__`` method which was introduced to the language before the individual comparison methods (called *rich comparisons*) described above. It is used if the rich comparisons are not defined.  You should overload it in a way which is consistent with the rich comparison methods, otherwise you may encounter some very strange behaviour.

Exercise 6
----------

#. Write a class for creating completely generic objects: its ``__init__`` function should accept any number of keyword parameters, and set them on the object as attributes with the keys as names.  Write a ``__str__`` method for the class -- the string it returns should include the name of the class and the values of all the object's custom instance attributes.

Answers to exercises
====================

Answer to exercise 1
--------------------

#.

    #. ``Person`` is a class defined in the global scope. It is a global variable.
    #. ``person`` is an instance of the ``Person`` class. It is also a global variable.
    #. ``surname`` is a parameter passed into the ``__init__`` method -- it is a local variable in the scope if the ``__init__`` method.
    #. ``self`` is a parameter passed into each instance method of the class -- it will be replaced by the instance object when the method is called on the object with the ``.`` operator.  It is a new local variable inside the scope of each of the methods -- it just always has the same value, and by convention it is always given the same name to reflect this.
    #. ``age`` is a method of the ``Person`` class. It is a local variable in the scope of the class.
    #. ``age`` (the variable used inside the function) is a local variable inside the scope of the ``age`` method.
    #. ``self.email`` isn't really a separate variable. It's an example of how we can refer to attributes and methods of an object using a variable which refers to the object, the ``.`` operator and the name of the attribute or method. We use the ``self`` variable to refer to an object inside one of the object's own methods -- wherever the variable ``self`` is defined, we can use ``self.email``, ``self.age()``, etc..
    #. ``person.email`` is another example of the same thing. In the global scope, our person instance is referred to by the variable name ``person``.  Wherever ``person`` is defined, we can use ``person.email``, ``person.age()``, etc..

Answer to exercise 2
--------------------

#. Here is an example program::

    import datetime

    class Person:

        def __init__(self, name, surname, birthdate, address, telephone, email):
            self.name = name
            self.surname = surname
            self.birthdate = birthdate

            self.address = address
            self.telephone = telephone
            self.email = email

            # This isn't strictly necessary, but it clearly introduces these attributes
            self._age = None
            self._age_last_recalculated = None

            self._recalculate_age()

        def _recalculate_age(self):
            today = datetime.date.today()
            age = today.year - self.birthdate.year

            if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
                age -= 1

            self._age = age
            self._age_last_recalculated = today

        def age(self):
            if (datetime.date.today() > self._age_last_recalculated):
                self._recalculate_age()

            return self._age

Answer to exercise 3
--------------------

#. ``name`` is always an instance attribute which is set in the constructor, and each class instance can have a different name value.  ``surname`` is always a class attribute, and cannot be overridden in the constructor -- every instance will have a surname value of ``Smith``.  ``profession`` is a class attribute, but it can optionally be overridden by an instance attribute in the constructor.  Each instance will have a profession value of ``smith`` unless the optional ``surname`` parameter is passed into the constructor with a different value.

Answer to exercise 4
--------------------

#. Here is an example program::

    class Numbers:
        MULTIPLIER = 3.5

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def add(self):
            return self.x + self.y

        @classmethod
        def multiply(cls, a):
            return cls.MULTIPLIER * a

        @staticmethod
        def subtract(b, c):
            return b - c

        @property
        def value(self):
            return (self.x, self.y)

        @value.setter
        def value(self, xy_tuple):
            self.x, self.y = xy_tuple

        @value.deleter
        def value(self):
            del self.x
            del self.y

Answer to exercise 5
--------------------

#.

    #. You should see something like ``'<__main__.Person object at 0x7fcb233301d0>'``.
    #. ``<class '__main__.Person'>`` -- ``__main__`` is Python's name for the program you are executing.
    #. ``<class 'type'>`` -- any class has the type ``type``.
    #. Here is an example program::

            def print_object_attrs(any_object):
                for k, v in any_object.__dict__.items():
                    print("%s: %s" % (k, v))

Answer to exercise 6
--------------------

#. Here is an example program::

    class AnyClass:
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)

        def __str__(self):
            attrs = ["%s=%s" % (k, v) for (k, v) in self.__dict__.items()]
            classname = self.__class__.__name__
            return "%s: %s" % (classname, " ".join(attrs))
