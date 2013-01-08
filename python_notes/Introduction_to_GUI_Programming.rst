************************************************
Introduction to GUI programming with ``tkinter``
************************************************

We have previously seen how to write text-only programs which have a *command-line interface*, or CLI.  Now we will briefly look at creating a program with a *graphical user interface*, or GUI.  In this chapter we will use ``tkinter``, a module in the Python standard library which serves as an interface to Tk, a simple *toolkit*. There are many other toolkits available, but they often vary across platforms.  If you learn the basics of ``tkinter``, you should see many similarities should you try to use a different toolkit.

We will see how to make a simple GUI which handles user input and output.  GUIs often use a form of OO programming which we call *event-driven*: the program responds to *events*, which are actions that a user takes.

.. Note:: in some Linux distributions, like Ubuntu and Debian, the ``tkinter`` module is packaged separately to the rest of Python, and must be installed separately.

Event-driven programming
------------------------

In this programming paradigm, *signals* are sent between different objects.  Some objects *send* signals -- we can also call this *firing an event*.  Other objects *listen* for signals, and respond in some way when they pick one up.  In a GUI interface, the object which fires an event is usually a GUI component -- for example, a button fires an event when it is clicked.

Each event-firing object can be monitored by more than one listener, and a listener may be listening for more than one event, and may have a different action ready for each one.  The listening object should have a method which is invoked in response to each event -- we call such a method an *event handler*.

``tkinter`` basics
------------------

``tkinter`` provides us with a variety of common GUI elements which we can use to build our interface -- such as buttons, menus and various kinds of entry fields and display areas.  We call these elements *widgets*.  We are going to construct a *tree* of widgets for our GUI -- each widget will have a parent widget, all the way up to the *root window* of our application.  For example, a button or a text field needs to be *inside* some kind of containing window.

The widget classes provide us with a lot of default functionality.  They have methods for configuring the GUI's appearance -- for example, arranging the elements according to some kind of *layout* -- and for handling various kinds of user-driven events.  Once we have constructed the backbone of our GUI, we will need to customise it by integrating it with our internal application class.

