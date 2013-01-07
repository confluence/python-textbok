************************************************
Introduction to GUI programming with ``tkinter``
************************************************

We have previously seen how to write text-only programs which have a *command-line interface*, or CLI.  Now we will briefly look at creating a program with a *graphical user interface*, or GUI.  In this chapter we will use ``tkinter``, a simple *toolkit* which is in the Python standard library. There are many other toolkits available, but they often vary across platforms.  If you learn the basics of ``tkinter``, you should see many similarities should you try to use a different toolkit.

We will see how to make a simple GUI which handles user input and output.  GUIs often use a form of OO programming which we call *event-driven*: the program responds to *events*, which are actions that a user takes.

.. Note:: in some Linux distributions, like Ubuntu and Debian, the ``tkinter`` module is packaged separately to the rest of Python, and must be installed separately.

Event-driven programming
------------------------

In this programming paradigm, *signals* are sent between different objects.  Some objects *send* signals -- we can also call this *firing an event*.  Other objects *listen* for signals, and respond in some way when they pick one up.  In a GUI interface, the object which fires an event is usually a GUI component -- for example, a button fires an event when it is clicked.

Each event-firing object can be monitored by more than one listener, and a listener may be listening for more than one event, and may have a different action ready for each one.  The listening object should have a method which is invoked in response to each event -- we call such a method an *event handler*.

We will not call event handlers ourselves in our code -- they will be called automatically in response to events fired by the GUI component.  We will make extensive use of inheritance in this code -- our GUI objects will be derived from the default ``tkinter`` objects, which already have a lot of the backbone of a typical GUI's functionality defined.  We will customise them to interact with our own internal objects.

``tkinter`` basics
------------------

