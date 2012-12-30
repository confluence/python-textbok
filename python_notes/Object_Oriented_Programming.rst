***************************
Object-oriented programming
***************************

Introduction
============

As you have seen from the earliest code examples in this course, it is not compulsory to organise your code into classes when you program in Python.  You can use functions by themselves, in what is called a *procedural* programming approach.  However, while a procedural style can suffice for writing short, simple programs, an object-oriented programming (OOP) approach becomes more valuable the more your program grows in size and complexity.

The more data and functions comprise your code, the more important it is to arrange them into logical subgroups, making sure that data and functions which are related are grouped together and that data and functions which are not related don't interfere with each other.  Modular code is easier to understand and modify, and lends itself more to reuse -- and code reuse is valuable because it reduces development time.

As a worst-case scenario, imagine a program with a hundred functions and a hundred separate global variables all in the same file.  This would be a very difficult program to maintain.  All the variables could potentially be modified by all the functions even if they shouldn't be, and in order to pick unique names for all the variables, some of which might have a very similar purpose but be used by different functions, we would probably have to resort to poor naming practices.  It would probably be easy to confuse these variables with each other, since it would be difficult to see which functions use which variables.

We could try to make this code more modular even without object orientation.  We could group related variables together into aggregate data structures.  In the past, some other languages, like C++, introduced a ``struct`` type which eventually became indistinguishable from a class, but which initially didn't have any methods -- only attributes.  This allowed programmers to construct compound variables out of many individual variables, and was the first step towards object orientation.  In Python, we often use dictionaries for ad-hoc grouping of related data.

We could also split up the functions and data into separate *namespaces* instead of having them all defined inside the same *global namespace*.  This often coincides with splitting the code physically into multiple files.  In Python we do this by splitting code up into *modules*.

The main additional advantage of object orientation, as we saw in the previous chapter, is that it combines data with the functions which act upon that data in a single structure.  This makes it easy for us to find related parts of our code, since they are physically defined in close proximity to one another, and also makes it easier for us to write our code in such a way that the data inside each object is accessed as much as possible only through that object's methods.  We will discuss this principle, which we call *encapsulation*, in the next section.

Some people believe that OOP is a more intuitive programming style to learn, because people find it easy to reason about objects and relationships between them.  OOP is thus sometimes considered to be a superior approach because it allows new programmers to become proficient more quickly.

Basic OOP principles
--------------------

The most important principle of object orientation is *encapsulation*: the idea that data inside the object should only be accessed through a public *interface* -- that is, the object's methods.

The ``age`` function we saw in the previous chapter is a good example of this philosophy.  If we want to use the data stored in an object to perform an action or calculate a derived value, we define a method associated with the object which does this. Then whenever we want to perform this action we call the method on the object. We consider it bad practice to retrieve the information from inside the object and write separate code to perform the action outside of the object.

Encapsulation is a good idea for several reasons:

* the functionality is defined *in one place* and not in multiple places.
* it is defined in a logical place -- the place where the data is kept.
* data inside our object is not modified unexpectedly by external code in a completely different part of our program.
* when we use a method, we only need to know what result the method will produce -- we don't need to know details about the object's internals in order to use it.  We could switch to using another object which is completely different on the inside, and not have to change any code because both objects have the same interface.

We can say that the object "knows how" to do things with its own data, and it's a bad idea for us to access its internals and do things with the data ourselves.  If an object doesn't have an interface method which does what we want to do, we should add a new method or update an existing one.

Some languages have features which allow us to enforce encapsulation strictly.  In Java or C++, we can define access permissions on object attributes, and make it illegal for them to be accessed from outside the object's methods.  In Java it is also considered good practice to write setters and getters for all attributes, even if the getter simply retrieves the attribute and the setter just assigns it the value of the parameter which you pass in.

In Python, encapsulation is not enforced by the language, but there is a convention that we can use to indicate that a property is intended to be private and is not part of the object's public interface: we begin its name with an underscore.

It is also customary to set and get simple attribute values directly, and only write setter and getter methods for values which require some kind of calculation.  In the last chapter we learned how to use the property decorator to replace a simple attribute with a method without changing the object's interface.

Relationships between objects
-----------------------------

In the next section we will look at different ways that classes can be related to each other.  In Python, there are two main types of relationships between classes: *composition* and *inheritance*.

Composition
===========

Composition is a way of *aggregating* objects together by making some objects attributes of other objects.  We saw in the previous chapter how we can make a ``datetime.date`` object an attribute of our ``Person`` object, and use it to store a person's birthdate.  We can say that a person *has a* birthdate -- if we can express a relationship between two classes using the phrase *has-a*, it is a composition relationship.

Relationships like this can be one-to-one, one-to-many or many-to-many, and they can be unidirectional or bidirectional, depending on the specifics of the the roles which the objects fulfil.

According to some formal definitions the term *composition* implies that the two objects are quite strongly linked -- one object can be thought of as *belonging* exclusively to the other object.  If the owner object ceases to exist, the owned object will probably cease to exist as well.  If the link between two objects is weaker, and neither object has exclusive ownership of the other, it can also be called *aggregation*.

Here are four classes which show several examples of aggregation and composition::

    class Student:
        def __init__(self, name, student_number)
            self.name = name
            self.student_number = student_number
            self.classes = []

        def enrol(self, course_running):
            self.classes.append(course_running)
            course_running.add_student(self)


    class Department:
        def __init__(self, name, department_code):
            self.name = name
            self.department_code = department_code
            self.courses = {}

        def.add_course(self, description, course_code, credits):
            self.courses[course_code] = Course(description, course_code, credits, department)
            return self.courses[course_code]


    class Course:
        def __init__(self, description, course_code, credits, department):
            self.description = description
            self.course_code = course_code
            self.credits = credits
            self.department = department
            self.department.add_course(self)

            self.runnings = []

        def add_running(self, year):
            self.runnings.append(CourseRunning(self, year))
            return self.runnings[-1]


    class CourseRunning:
        def __init__(self, course, year):
            self.course = course
            self.year = year
            self.students = []

        def add_student(self, student):
            self.students.append(student)


    maths_dept = Department("Mathematics and Applied Mathematics", "MAM")
    mam1000w = maths_dept.add_course("Mathematics 1000", "MAM1000W", 1)
    mam1000w_2013 = mam1000w.add_running(2013)

    bob = Student("Bob", "Smith")
    bob.enrol(mam1000w_2013)

Why are there two classes which both describe a course?  This is an example of the way that translation of real-life concepts into objects in your code may not always be as straightforward as it appears.  Would it have made sense to have a single course object which has both description, code and department attributes and a list of students?

There are two distinct concepts, both of which can be called a "course",  that we need to represent: one is the theoretical *idea* of a course, which is offered by a department every year and always has the same name and code, and the other is the course as it is run *in a particular year*, each time with a different group of enrolled students.  We have represented these two concepts by two separate classes which are linked to each other.  ``Course`` is the theoretical description of a course, and ``CourseRunning`` is the concrete instance of a course.

We have defined several relationships between these classes:

* A student can be enrolled in several courses (``CourseRunning`` objects), and a course (``CourseRunning``) can have multiple students enrolled in it in a particular year, so this is a many-to-many relationship.  A student knows about all his or her courses, and a course has a record of all enrolled students, so this is a bidirectional relationship.  These objects aren't very strongly coupled -- a student can exist independently of a course, and a course can exist independently of a student.

* A department offers multiple courses (``Course`` objects), but in our implementation a course can only have a single department -- this is a one-to-many relationship.  It is also bidirectional.  Furthermore, these objects are more strongly coupled -- you can say that a department *owns* a course.  The course cannot exist without the department.

* A similar relationship exists between a course and its "runnings": it is also bidirectional, one-to-many and strongly coupled -- it wouldn't make sense for "MAM1000W run in 2013" to exist on its own in the absence of "MAM1000W".

What words like "exist" and "owns" actually mean for our code can vary.  An object which "owns" another object could be responsible for creating that object when it requires it and destroying it when it is no longer needed -- but these words can also be used to describe a logical relationship between concepts which is not necessarily literally implemented in that way in the code.

.. Todo:: maybe make a UML diagram for this (yuck). There should be a sphinx plugin.

Inheritance
===========

*Inheritance* is a way of arranging objects in a hierarchy from the most general to the most specific.  An object which *inherits* from another object is considered to be a *subtype* of that object.  As we saw in the previous chapter, all objects in Python inherit from ``object``.  We can say that a string, an integer or a ``Person`` instance *is an* ``object`` instance.  When we can describe the relationship between two objects using the phrase *is-a*, that relationship is inheritance.

We also often say that a class is a *subclass* or *child class* of a class from which it inherits, or that the other class is its *superclass* or *parent class*.  We can refer to the most generic class at the base of a hierarchy as a *base class*.

Inheritance can help us to represent objects which have some differences and some similarities in the way they work.  We can put all the functionality that the objects have in common in a base class, and then define one or more subclasses with their own custom functionality.

Inheritance is also a way of reusing existing code easily.  If we already have a class which does *almost* what we want, we can create a subclass in which we partially override some of its behaviour, or perhaps add some new functionality.

Here is a simple example of inheritance::

    class Person:
        def __init__(self, name, surname, number):
            self.name = name
            self.surname = surname
            self.number = number


    class Student(Person):
        UNDERGRADUATE, POSTGRADUATE = range(2)

        def __init__(self, student_type, *args, **kwargs):
            self.student_type = student_type
            self.classes = []
            super(Student, self).__init__(*args, **kwargs)

        def enrol(self, course):
            self.classes.append(course)


    class StaffMember(Person):
        PERMANENT, TEMPORARY = range(2)

        def __init__(self, employment_type, *args, **kwargs)
            self.employment_type = employment_type
            super(StaffMember, self).__init__(*args, **kwargs)


    class Lecturer(StaffMember):
        def __init__(self, *args, **kwargs):
            self.courses_taught = []
            super(Lecturer, self).__init__(*args, **kwargs)

        def assign_teaching(self, course):
            self.courses_taught.append(course)


    jane = Student(Student.POSTGRADUATE, "Jane", "Smith", "SMTJNX045")
    jane.enrol(a_postgrad_course)

    bob = Lecturer(StaffMember.PERMANENT, "Bob". "Jones", "123456789")
    bob.assign_teaching(an_undergrad_course)

Our base class is ``Person``, which represents any person associated with a university.  We create a subclass to represent students and one to represent staff members, and then a subclass of ``StaffMember`` for people who teach courses (as opposed to staff members who have administrative positions.)

We represent both student numbers and staff numbers by a single attribute, ``number``, which we define in the base class, because it makes sense for us to treat them as a unified form of identification for any person.  We use different attributes for the kind of student (undergraduate or postgraduate) that someone is and whether a staff member is a permanent or a temporary employee, because these are different sets of options.

We have also added a method to ``Student`` for enrolling a student in a course, and a method to ``Lecturer`` for assigning a course to be taught by a lecturer.

The ``__init__`` method of the base class initialises all the instance variables that are common to all subclasses.  In each subclass we *override* the ``__init__`` method so that we can use it to initialise that class's attributes -- but we want the parent class's attributes to be initialised as well, so we need to call the parent's ``__init__`` method from ours.  To find the right method, we use the ``super`` function -- when we pass in the current class and object as parameters, it will return a proxy object with the correct ``__init__`` method, which we can then call.

In each of our overridden ``__init__`` methods we use those of the method's parameters which are specific to our class inside the method, and then pass the remaining parameters to the parent class's ``__init__`` method.  A common convention is to add the specific parameters for each successive subclass to the *beginning* of the parameter list, and define all the other parameters using ``*args`` and ``**kwargs`` -- then the subclass doesn't need to know the details about the parent class's parameters.  Because of this, if we add a new parameter to the superclass's ``__init__``, we will only need to add it to all the places where we create that class or one of its subclasses -- we won't also have to update all the child class definitions to include the new parameter.

More about inheritance, and when to avoid it
============================================

Multiple inheritance
--------------------

The previous example might seem like a good way to represent students and staff members at first glance, but if we started to extend this system we would soon encounter some complications.  At a real university, the divisions between staff and students and administrative and teaching staff are not always clear-cut.  A student who tutors a course is also a kind of temporary staff member.  A staff member can enrol in a course.  A staff member can have *both* an administrative role in the department *and* a teaching position.

In Python it is possible for a class to inherit from multiple other classes.  We could, for example, create a class called ``Tutor``, which inherits from both ``Student`` and ``StaffMember``.  Multiple inheritance isn't too difficult to understand if a class inherits from multiple classes which have completely different properties, but things get complicated if two parent classes implement the same method or attribute.

If classes ``B`` and ``C`` inherit from ``A`` and class ``D`` inherits from ``B`` and ``C``, and both ``B`` and ``C`` have a method ``do_something``, which ``do_something`` will ``D`` inherit?  This ambiguity is known as the *diamond problem*, and different languages resolve it in different ways.  In our ``Tutor`` class we would encounter this problem with the ``__init__`` method.

Fortunately the ``super`` function knows how to deal gracefully with multiple inheritance. If we use it inside the ``Tutor`` class's ``__init__`` method, all of the parent classes' ``__init__`` methods should be called in a sensible order.  We would then end up with a class which has all the attributes and methods found in both ``Student`` and ``StaffMember``.

Mix-ins
-------

If we use multiple inheritance, it is often a good idea for us to design our classes in a way which avoids the kind of ambiguity described above.  One way of doing this is to split up optional functionality into *mix-ins*.  A Mix-in is a class which is not intended to stand on its own -- it exists to add extra functionality to another class through multiple inheritance.  For example, let us try to rewrite the example above so that each set of related things that a person can do at a university is written as a mix-in::

    class Person:
        def __init__(self, name, surname, number):
            self.name = name
            self.surname = surname
            self.number = number


    class LearnerMixin:
        def __init__(self):
            self.classes = []

        def enrol(self, course):
            self.classes.append(course)


    class TeacherMixin:
        def __init__(self):
            self.courses_taught = []

        def assign_teaching(self, course):
            self.courses_taught.append(course)


    class Tutor(Person, LearnerMixin, TeacherMixin):
        def __init__(self, *args, *kwargs):
            super(Tutor, self).__init__(*args, *kwargs)

    jane = Tutor("Jane", "Smith", "SMTJNX045")
    jane.enrol(a_postgrad_course)
    jane.assign_teaching(an_undergrad_course)

Now Tutor inherits from one "main" class, ``Person``, and two mix-ins which are not related to ``Person``.  Each mix-in is responsible for providing a specific piece of optional functionality.  Our mix-ins still have ``__init__`` methods, because each one has to initialise a list of courses (we saw in the previous chapter that we can't do this with a class attribute).  Many mix-ins just provide additional methods and don't initialise anything. This sometimes means that they depend on other properties which already exist in the class which inherits from them.

We could extend this example with more mix-ins which represent the ability to pay fees, the ability to get paid for services, and so on -- we could then create a relatively flat hierarchy of classes for different kinds of people which inherit from ``Person`` and some number of mix-ins.

Abstract classes and interfaces
-------------------------------

In some languages it is possible to create a class which can't be instantiated.  That means that we can't use this class directly to create an object -- we can only inherit from the class, and use the subclasses to create objects.

Why would we want to do this?  Sometimes we want to specify a set of properties that an object needs to have in order to be suitable for some task -- for example, we may have written a function which expects one of its parameters to be an object with certain methods that our function will need to use.  We can create a class which serves as a *template* for suitable objects by defining a list of methods that these objects must implement.  This class is not intended to be instantiated because all our method definitions are empty -- all the *insides* of the methods must be implemented in a subclass.

The abstract class is thus an *interface* definition -- some languages also have a type of structure called an interface, which is very similar.  We say that a class *implements* an interface if it inherits from the class which specifies that interface.

In Python we can't prevent anyone from instantiating a class, but we can create something similar to an abstract class by using ``NotImplementedError`` inside our method definitions.  For example, here are some "abstract" classes which can be used as templates for shapes::

    class 2DShape:
        def area(self):
            raise NotImplementedError()

    class 3DShape:
        def volume(self):
            raise NotImplementedError()

Any two-dimensional shape has an area, and any three-dimensional shape has a volume.  The formulae for working out area and volume differ depending on what shape we have, and objects for different shapes may have completely different attributes.

If an object inherits from ``2DShape``, it will gain that class's default ``area`` method -- but the default method raises an error which makes it clear to the user that a custom method must be defined in the child object::

    class Square(2DShape):
        def __init__(self, width):
            self.width = width

        def area(self):
            return self.width ** 2

.. Todo:: add an exercise for creating an exception hierarchy

Why not inheritance?
====================

Inheritance can be a useful technique, but it can also be an unnecessary complication.  As we have already discussed, multiple inheritance can cause a lot of ambiguity and confusion, and hierarchies which use multiple inheritance should be designed carefully to minimise this.

A deep hierarchy with many layers of subclasses may be difficult to read and understand.  In our first inheritance example, to understand how the ``Lecturer`` class works we have to read through *three* different classes instead of one.  If our classes are long and split into several different files, it can be hard to figure out which subclass is responsible for a particular piece of behaviour.  You should avoid creating hierarchies which are more than one or two classes deep.

In some statically typed languages inheritance is very popular because it allows the programmer to work around some of the restrictions of static typing.  If a lecturer and a student are both a kind of person, we can write a function which accepts a parameter of type ``Person`` and have it work on both lecturer and student objects because they both inherit from ``Person``.  This is known as *polymorphism*.

In Python inheritance is not compulsory for polymorphism, because Python is not statically typed.  A function can work on both lecturer and student objects if they both have the appropriate attributes and methods even if these objects *don't* share a parent class, and are completely unrelated.  When you check parameters yourself, you are encouraged not to check an object's type directly, but instead to check for the presence of the methods and attributes that your function needs to use -- that way you are not forcing the parameter objects into an inheritance hierarchy when this is unnecessary.

Replacing inheritance with composition
--------------------------------------

Sometimes we can replace inheritance with composition and achieve a similar result -- this approach is sometimes considered preferable.  In the mix-in example, we split up the possible behaviours of a person into logical groups.  Instead of implementing these sets of behaviours as mix-ins and having our class inherit from them, we can add them as *attributes* to the ``Person`` class::


    class Learner:
        def __init__(self):
            self.classes = []

        def enrol(self, course):
            self.classes.append(course)


    class Teacher:
        def __init__(self):
            self.courses_taught = []

        def assign_teaching(self, course):
            self.courses_taught.append(course)


    class Person:
        def __init__(self, name, surname, number, learner=None, teacher=None):
            self.name = name
            self.surname = surname
            self.number = number

            self.learner = learner
            self.teacher = teacher

    jane = Person("Jane", "Smith", "SMTJNX045", Learner(), Teacher())
    jane.learner.enrol(a_postgrad_course)
    jane.teacher.assign_teaching(an_undergrad_course)

Now instead of calling the ``enrol`` and ``assign_teaching`` methods on our person object directly, we *delegate* to the object's ``learner`` and ``teacher`` attributes.  We could also implement additional methods in the ``Person`` class which hide the delegation, and perhaps raise an error message if an optional attribute does not exist::

    class Person:
        def __init__(self, name, surname, number, learner=None, teacher=None):
            self.name = name
            self.surname = surname
            self.number = number

            self.learner = learner
            self.teacher = teacher

        def enrol(self, course):
            if not hasattr(self, "learner"):
                raise NotImplementedError()

            self.learner.enrol(course)

        def assign_teaching(self, course):
            if not hasattr(self, "teacher"):
                raise NotImplementedError()

            self.teacher.assign_teaching(course)
