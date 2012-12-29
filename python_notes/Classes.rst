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

    class Person():

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

    print(dir(person))

We start the class definition with the ``class`` keyword, followed by the class name, round brackets and a colon.  We would list any parent classes in between the brackets, but this class doesn't have any, so the brackets are empty.

Inside the class body, we define two functions -- these are our objects's methods.  We have defined to methods -- the first is called ``__init__``, which is a special method.  When we call the class object, a new instance of the class is created, and the ``__init__`` method on this new object is immediately executed with all the parameters that we passed to the class object.  The purpose of this method is thus to set up a new object using data that we have provided.  ``__init__`` is sometimes called the object's *constructor*.

.. Todo:: is that technically correct?  What is the difference between construction and initialisation?

The second method is a custom method which calculates the age of our person using the birthdate and the current date.

You may have noticed that both of these method definitions have ``self`` as the first parameter, and we use this variable inside the method bodies -- but we don't appear to pass this parameter in.  This is because whenever we call a method on an object, *the object itself* is automatically passed in as the first parameter.  This gives us a way to access the object's properties from inside the object's methods.

In some languages this parameter is *implicit* -- that is, it is not visible in the function signature -- and we access it with a special keyword.  In Python it is explicitly exposed.  It doesn't have to be called ``self``, but this is a very strongly followed convention.

Now you should be able to see that our ``__init__`` function creates attributes on the object and sets them to the values we have passed in as parameters.  We use the same names for the attributes and the parameters, but this is not compulsory.

The ``age`` function doesn't take any parameters except ``self`` -- it only uses information stored in the object's attributes, and the current date (which it retrieves using the ``datetime`` module).

Note that the ``birthdate`` attribute is itself an object. The ``date`` class is defined in the ``datetime`` module, and we create a new instance of this class to use as the birthdate parameter when we create an instance of the ``Person`` class. We don't have to assign it to an intermediate variable before using it as a parameter to ``Person``; we can just create it when we call ``Person``, just like we create the string literals for the other parameters.

Instance attributes
===================

It is important to note that the attributes set on the object in the ``__init__`` function do not form an exhaustive list of all the attributes that our object is ever allowed to have.

In some languages you must provide a list of the object's attributes in the class definition, placeholders are created for these allowed attributes when the object is created, and you may not add new attributes to the object later.  In Python, you can add new attributes, and even new methods, to an object on the fly.  In fact, there is nothing special about the ``__init__`` function when it comes to setting attributes.  We could store a cached age value on the object from inside the ``age`` function::

    def age(self):
        if hasattr(self, "_age"):
            return self._age

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

Initialising all our attributes in ``__init__``, even if we just set them to empty values, makes our code less error-prone. It also makes it easier to read an understand -- we can see at a glance what attributes our object has.

An ``__init__`` method doesn't have to take any parameters (except ``self``) and it can be completely absent (in which case the default, which does nothing, will be used).

Class attributes
================

All the attributes which are defined on a ``Person`` instance are *instance attributes* -- they are added to the instance when the ``__init__`` method is executed.  We can, however, also define attributes which are set on the *class*.  These attributes will be shared by all instances of that class.  In many ways they behave just like instance attributes, but there are some caveats that you should be aware of.

We define class attributes in the body of a class, at the same indentation level as method definitions (one level up from the insides of methods)::

    class Person():

        TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

        def __init__(self, title, name, surname):
            if title not in self.TITLES:
                raise ValueError("%s is not a valid title." % title)

            self.title = title
            self.name = name
            self.surname = surname

As you can see, we access the class attribute ``TITLES`` just like we would access an instance attribute -- it is made available as a property on the instance object, which we access inside the method through the ``self`` variable.

All the ``Person`` objects we create will share the same ``TITLES`` class attribute.

Class attributes are often used to define constants which are closely associated with a particular class.  They can also sometimes be used to provide default attribute values::

    class Person():
        deceased = False

        def mark_as_deceased(self):
            self.deceased = True

When we set an attribute on an instance which has the same name as a class attribute, we are *overriding* the class attribute with an instance attribute, which will take precedence over it. If we create two ``Person`` objects and call the ``mark_as_deceased`` method on one of them, we will not affect the other one.  We should, however, be careful when a class attribute is of a mutable type -- because if we modify it in-place, we *will* affect all objects of that class at the same time. Remember that all instances share the same class attributes.

    class Person():
        pets = []

        def add_pet(self, pet):
            self.pets.append(pet)

    jane = Person()
    bob = Person()

    jane.add_pet("cat")
    print(jane.pets)
    print(bob.pets) # oops!

What we *should* do in cases like this is initialise the mutable attribute *as an instance attribute*, inside ``__init__``.  Then every instance will have its own separate copy::

    class Person():

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

    class Person():
        TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

        def __init__(self, title, name, surname, allowed_titles=TITLES):
            if title not in allowed_titles:
                raise ValueError("%s is not a valid title." % title)

            self.title = title
            self.name = name
            self.surname = surname

Class decorators
================

In the previous chapter we learned about decorators -- functions which are used to modify the behaviour of other functions.  There are some built-in decorators which are often used in class definitions.

``@classmethod``
----------------

``@staticmethod``
-----------------

``@attribute``
--------------

* e.g. apply to age


* special decorators: class methods, static methods, attributes
* dir; special attributes and methods
(after dir, briefly mention inheritance in next chapter and that all classes inherit from object)
* overriding special methods (str, iter, comparisons, etc..)

(stuff about inheritance, etc. goes into chapter about OO?)