***************************
Object-oriented programming
***************************

* moved this from previous chapter; needs some revision:

The ``age`` function is a good example of the philosophy of object-oriented programming.  If we want to use the data stored in an object to perform some kind of action or calculate some kind of derived value, we define a method associated with the object which does this. Then whenever we want to perform this action we call the method on the object. We do not retrieve the information from inside the object and write separate code to perform the action outside of the object.  This means that the functionality is defined *in one place* and not multiple places, and it is defined in a logical place -- the place where the data is kept.  We say that the object "knows how" to do things with its own data, and it's a bad idea for us to