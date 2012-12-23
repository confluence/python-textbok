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

* note that date is an object

(after dir, briefly mention inheritance in next chapter and that all classes inherit from object)

* special decorators: class methods, static methods, attributes
* dir; special attributes and methods
* overriding special methods (str, iter, comparisons, etc..)

(stuff about inheritance, etc. goes into chapter about OO?)