***************************
Object-oriented programming
***************************

* note that OO is not compulsory in Python, suggest that it is a good idea for sufficiently complex programs

* basic oo concept: encapsulation -- object manages own internals; access through an interface; no messing with internals from outside.

* moved this from previous chapter; needs some revision:

The ``age`` function is a good example of the philosophy of object-oriented programming.  If we want to use the data stored in an object to perform some kind of action or calculate some kind of derived value, we define a method associated with the object which does this. Then whenever we want to perform this action we call the method on the object. We do not retrieve the information from inside the object and write separate code to perform the action outside of the object.  This means that the functionality is defined *in one place* and not multiple places, and it is defined in a logical place -- the place where the data is kept.  We say that the object "knows how" to do things with its own data, and it's a bad idea for us to

* Interclass relationships
    ** Introduce this as a more theoretical examination of how classes can be related to each other
    ** rewrite this so that it's actually understandable

* Inheritance
    ** all the important basic things about inheritance
    ** admonition not to overuse inheritance; discussion of alternatives

* "Abstract classes" except call the section something else because there aren't any