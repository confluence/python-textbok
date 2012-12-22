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

Here is a

* why? grouping attributes and methods
* constructors and creating an instance
* special decorators: class methods, static methods, attributes
* dir; special attributes and methods
* overriding special methods (str, iter, comparisons, etc..)

(stuff about inheritance, etc. goes into chapter about OO?)