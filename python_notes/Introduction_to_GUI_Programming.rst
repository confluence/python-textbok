************************************************
Introduction to GUI programming with ``tkinter``
************************************************

We have previously seen how to write text-only programs which have a *command-line interface*, or CLI.  Now we will briefly look at creating a program with a *graphical user interface*, or GUI.  In this chapter we will use ``tkinter``, a module in the Python standard library which serves as an interface to Tk, a simple *toolkit*. There are many other toolkits available, but they often vary across platforms.  If you learn the basics of ``tkinter``, you should see many similarities should you try to use a different toolkit.

We will see how to make a simple GUI which handles user input and output.  GUIs often use a form of OO programming which we call *event-driven*: the program responds to *events*, which are actions that a user takes.

.. Note:: in some Linux distributions, like Ubuntu and Debian, the ``tkinter`` module is packaged separately to the rest of Python, and must be installed separately.

Event-driven programming
------------------------

Anything that happens in a user interface is an *event*.  We say that an event is *fired* whenever the user does something -- for example, clicks on a button or types a keyboard shortcut.  Some events could also be triggered by occurrences which are not controlled by the user -- for example, a background task might complete, or a network connection might be established or lost.

Our application needs to monitor all the events that we find interesting, and respond to them in some way if they occur.  To do this, we usually associate certain functions with particular events.  We call a function which performs an action in response to an event an *event handler* -- we *bind* handlers to events.

``tkinter`` basics
------------------

``tkinter`` provides us with a variety of common GUI elements which we can use to build our interface -- such as buttons, menus and various kinds of entry fields and display areas.  We call these elements *widgets*.  We are going to construct a *tree* of widgets for our GUI -- each widget will have a parent widget, all the way up to the *root window* of our application.  For example, a button or a text field needs to be *inside* some kind of containing window.

The widget classes provide us with a lot of default functionality.  They have methods for configuring the GUI's appearance -- for example, arranging the elements according to some kind of *layout* -- and for handling various kinds of user-driven events.  Once we have constructed the backbone of our GUI, we will need to customise it by integrating it with our internal application class.

Our first GUI will be a window with a label and two buttons::

    from tkinter import Tk, Label, Button

    class MyFirstGUI:
        def __init__(self, master):
            self.master = master
            master.title("A simple GUI")

            self.label = Label(master, text="This is our first GUI!")
            self.label.pack()

            self.greet_button = Button(master, text="Greet", command=self.greet)
            self.greet_button.pack()

            self.close_button = Button(master, text="Close", command=master.quit)
            self.close_button.pack()

        def greet(self):
            print("Greetings!")

    root = Tk()
    my_gui = MyFirstGUI(root)
    root.mainloop()

Try executing this code for yourself.  You should be able to see a window with a title, a text label and two buttons -- one which prints a message in the console, and one which closes the window.  The window should have all the normal properties of any other window you encounter in your window manager -- you are probably able to drag it around by the titlebar, resize it by dragging the frame, and maximise, minimise or close it using buttons on the titlebar.

.. Note:: The *window manager* is the part of your operating system which handles windows.  All the widgets inside a window, like buttons and other controls, may look different in every GUI toolkit, but the way that the window frames and title bars look and behave is determined by your window manager and should always stay the same.

We are using three widgets: ``Tk`` is the class which we use to create the *root* window -- the main window of our application.  Our application should only have one root, but it is possible for us to create other windows which are separate from the main window.

``Button`` and ``Label`` should be self-explanatory.  Each of them has a parent widget, which we pass in as the first parameter to the constructor -- we have put the label and both buttons inside the main window, so they are the main window's children in the tree.  We use the ``pack`` method on each widget to position it inside its parent -- we will learn about different kinds of layout later.

All three of these widgets can display text (we could also make them display images).  The label is a static element -- it doesn't *do* anything by default; it just displays something.  Buttons, however, are designed to cause something to happen when they are clicked.  We have used the ``command`` keyword parameter when constructing each button to specify the function which should handle each button's click events -- both of these functions are object methods.

We didn't have to write any code to make the buttons fire click events or to bind the methods to them explicitly.  That functionality is already built into the button objects -- we only had to provide the handlers.  We also didn't have to write our own function for closing the window, because there is already one defined as a method on the window object.  We did, however, write our own method for printing a message to the console.

There are many ways in which we could organise our application class. In this example, our class doesn't inherit from any ``tkinter`` objects -- we use *composition* to associate our tree of widgets with our class.  We could also use *inheritance* to extend one of the widgets in the tree with our custom functions.

.. Todo:: take screenshots of windows

There are many different widget classes built into ``tkinter`` -- they should be familiar to you from other GUIs:

* A ``Frame`` is a container widget which is placed inside a window, which can have its own border and background -- it is used to group related widgets together in an application's layout.
* ``Toplevel`` is a container widget which is displayed as a separate window.
* ``Canvas`` is a widget for drawing graphics.  In advanced usage, it can also be used to create custom widgets -- because we can draw anything we like inside it, and make it interactive.
* ``Text`` displays formatted text, which can be editable and can have embedded images.
* A ``Button`` usually maps directly onto a user action -- when the user clicks on a button, something should happen.
* A ``Label`` is a simple widget which displays a short piece of text or an image, but usually isn't interactive.
* A ``Message`` is similar to a ``Label``, but is designed for longer bodies of text which need to be wrapped.
* A ``Scrollbar`` allows the user to scroll through content which is too large to be visible all at once.
* ``Checkbutton``, ``Radiobutton``, ``Listbox``, ``Entry`` and ``Scale`` are different kinds of input widgets -- they allow the user to enter information into the program.
* ``Menu`` and ``Menubutton`` are used to create pull-down menus.

Appearance
----------

* different kinds of layout
* fonts and colours

Custom events
-------------

* how to bind actions to new kinds of events

Putting it all together
-----------------------

* translate calculator example