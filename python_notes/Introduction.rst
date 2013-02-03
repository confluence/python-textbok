************
Introduction
************

The usefulness of computers is partly a result of their versatility in
solving various problems and performing tasks. To be able to take
advantage of the speed and power of computers, one needs to know how
to program. This module is about computer programming and how it can
be used to solve problems or perform useful tasks.

Our language of choice is Python -- a recent language which has been
found to be powerful, relatively easy to learn, and able to provide a
platform to advanced programming. In this module you will learn how to
analyse a problem and develop an effective solution for it using the
Python programming language.


What is a computer?
===================

A computer is a general-purpose device which behaves according to the
sets of instructions and data with which it is provided.  Computers
execute instructions to process data.  Each computer has at its core a
central processing unit (CPU) -- modern CPUs are built as a single
microprocessor chip.

Computer instructions
---------------------

A computer accepts a series of instructions as input, processes them one by one, and usually displays some kind of output to show what it has done.  This is similar to the way people follow instructions or recipes.  However, while people can understand complex instructions in natural languages (like English), computers can only understand very simple instructions which can be expressed in computer languages -- restricted, formally specified languages which are much more limited than natural languages.

While some languages (like Python) can be used to express more high-level instructions than others (like assembly), there are still considerable limits.  A computer can easily interpret an instruction like "add these two numbers together", but not a more complicated request like "balance my chequebook".  Such a request would have to be broken down into many smaller step-by-step instructions which are simpler.  Lists of instructions which tell the computer how to perform complex tasks are known as *programs*.

Here are some examples of simple computer instructions:

* *arithmetic*: adding, subtracting, multiplying or dividing numbers.
* *comparison*: comparing two numbers to see which is greater, or whether they are equal. These are often called *logical operations*.
* *branching*: jumping to another instruction in the program, and continuing from there.

Modern computers can execute many millions of these instructions in a second.

Components of a computer
------------------------

A computer contains four major types of components:

* *input*: anything that allows a computer to *receive* information from a user. This includes keyboards, mice, scanners and microphones.
* *processing*: the components of the computer which *process* information.  The main processing component of a computer is the *central processing unit*, or CPU, but in a modern computer there are likely to be other processing units too. For example, many graphics cards come with *graphics processing units*, or GPUs, which were once only used to process graphics but today can also be used for general-purpose programs.
* *memory*: components where information is *stored*.  This includes both *primary memory* (what we colloquially know as "memory") and *secondary memory* (what we know as *storage devices*, e.g. hard drives, CDs or flash disks).
* *output*: anything that the computer uses to *display* information to the user. This includes monitors, speakers and printers.

To understand how these components fit together, consider how a vending machine works.  A vending machine is not, strictly speaking, a computer, but it can be broken down into very similar components:

* *input*: to use a vending machine, you put money into it and make a selection. The coin slots and selection buttons are the vending machine's input devices.
* *processing*: when you make your selection, the vending machine goes through several steps: verifying that it has received enough money, computing change, and making sure the selected item is in stock. The part of the machine that performs all these steps can be thought of as the processor.
* *output*: the vending machine deposits your purchase and your change in compartments from which you can retrieve them. It also has a simple electronic display which can show letters and numbers, and uses this to give you all kinds of feedback.
* *memory*: to perform the processing steps, the vending machine needs to keep track of information such as what items are in stock, their prices and the available change. This information must be stored somewhere.

The CPU
-------

The CPU is the most important part of a computer because of its instruction-processing functionality. The other parts of the computer follow the commands of the CPU. Two important characteristics of a CPU are:

* the *clock speed*: the CPU contains a clock which produces a regular signal. All the low-level operations (switches) that the CPU performs in order to process instructions are synchronised to this signal.  The faster the clock, the faster the CPU can (in theory) operate -- but there are other limitations.  Today's typical clock speed is in excess of 1GHz or 1 000 000 000 switches per second.

* the *instruction set*: this is the set of instructions (more accurately, the machine language instructions) that the CPU understands.  Different kinds of CPUs understand different sets of instructions: for example, Intel IA-32 and x86-64, IBM PowerPC or ARM.

A CPU has several important subcomponents:

* the *arithmetic/logic unit* (ALU) performs arithmetic and comparison operations.
* the *control unit* determines which instruction to execute next.
* *registers* form a high-speed storage area for temporary results.

Memory
------

A computer stores information in its memory for later reference. There are two types of memory: primary and secondary.

*Primary memory* is connected directly to the CPU (or other processing units) and is usually referred to as RAM (random-access memory). Most primary memory loses its contents when the computer is switched off (i.e. it is *volatile*).

.. Todo:: diagram?

We can imagine primary memory as a long sequence of memory cells: each cell can be addressed by its memory address. These addresses start at zero for the first cell and each subsequent cell's address is one more than the one preceding it. Each cell can hold only a single number, but the CPU can replace the content with a new number at any time. The content can be retrieved without being erased from the cell.

*Secondary memory* is cheaper than primary memory, and can thus be made available in much larger sizes. Although it is much slower, it is non-volatile -- that is, its contents are preserved even after the computer is switched off. Examples of this type of memory include hard disks and flash disks.

A computer's operating system provides high-level interfaces to secondary memory.  These interfaces allow us to refer to clusters of related information called *files* which are arranged in a hierarchy of directories.  Both the interfaces and the hierarchies are often referred to as *filesystems*.

We can think of directories as boxes (which may contain other boxes). Although it's easy to visualise the contents of a hard drive or flash disk using this metaphor, it is important to note that it is only a metaphor -- at a lower level, a hard drive has a series of memory addresses just like RAM, and all the data is ultimately stored in this simple structure. Parts of the same file are not necessarily stored in adjacent memory addresses.

Types of computers
------------------

Historically, computers have been categorised into specialised subtypes. The distinction is not always so clear-cut with modern computers, which can perform a greater variety of functions and often occupy multiple roles:

* *single-user personal computers*: these computers are designed for home use by a single person at a time. They are small enough to fit on a desk -- something which was novel when they were first introduced.  Modern personal computers are powerful enough to be used for many functions which were previously performed by more specialised computers.

* *batch computer systems*: most computers are *interactive* -- when the user issues some kind of instruction, something happens in response right away.  Some computers were designed to process large batches of instructions non-interactively -- that is, large amounts of work was scheduled to be done without the possibility of further input from the user while it was being done.  This allowed the computers to use their resources more efficiently.

  Some large companies may still use old-fashioned computer systems like this to perform highly repetitive tasks like payroll or accounting.  Most interactive computer systems can be used to perform non-interactive batch operations.  These operations are often scheduled during off-hours, when they are unlikely to compete with users for resources.

* *time-share computer systems*: these computer systems were an improvement over batch processing systems which allowed multiple users to access the same central computer remotely at the same time. The central computer was typically located in an air-conditioned room which was physically far away from the users.  The users connected to the central computer through *terminals* which had little processing power of their own -- they usually had only a mouse and a keyboard.

  Unlike a batch-processing computer, a time-share computer could switch between different users' program state, polling different terminals to check whether there was any new input from a particular user. As computer speeds improved, this switching happened so rapidly that it appeared that all the users' work was being performed simultaneously.

  Today multiple users can connect to a central computer using an ordinary computer network.  The role of the central computer can be played by an ordinary personal computer (although often one with much better hardware) which performs a specialised role.  Most modern computers have the ability to switch between multiple running programs quickly enough that they appear to be running simultaneously.  The role of the terminal is usually performed by the user's normal personal computer.

  There are also powerful *supercomputers* whose specialised hardware allows them to exceed greatly the computing power of any personal computer.  Users are given access to such computers when they need to solve a problem that requires the use of a lot of computing resources.

* *computer networks*: these are multiple computers connected to each other with digital or analog cables or wirelessly, which are able to communicate with each other.  Today almost all computers can be connected to a network.  In most networks there are specialised computers called *servers* which provide services to other computers on the network (which are called *clients*).  For example, a storage server is likely to have many fast, high-capacity disk drives so that it can provide storage and back-up services to the whole network.  A print server might be optimised for managing print jobs.  Using servers keeps costs down by allowing users to share resources efficiently, while keeping the maintenance in one area.

  The Internet is a very large international computer network. Many computers on the Internet are servers.  When you use a web browser, you send requests to web servers which respond by sending you webpages.

History of computers
====================

Today's computers are electronic. Earlier computers were mostly mechanical and electro-mechanical. Over time, computers have advanced exponentially -- from expensive machines which took up entire rooms to today's affordable and compact units.

The oldest mechanical calculating aid is the abacus. It was invented in Babylon over 3000 years ago and was also used by the Chinese. It can be used for addition, subtraction, multiplication and division. More recently, in 1642, Blaise Pascal invented the first mechanical calculator. Pascal's machine was able to do addition and subtraction. In 1671, Gottfried von Leibnitz extended Pascal's machine to handle multiplication, division and square roots.

In 1801, Joseph-Marie Jacquard invented a loom which read a tape of punched cards. It was able to weave cloth according to instructions on the cards. This was the first machine that could be reprogrammed.

Towards the middle of the 1800s, Charles Babbage designed the Difference Engine, which was supposed to compute and print mathematical tables. However, it was never completed because he became engrossed in the design of his Analytical Engine. It was designed to follow instructions in a program and thus able to handle any computation.  Babbage's machine was also going to make use of punched cards, but unfortunately the English government stopped funding the project and the machine was never completed. It is doubtful that the machine could have worked, since it required metalworking skills beyond what was possible at the time.

Ada Lovelace assisted Babbage in some of his work. In 1942, she translated one of Babbage's papers on the Analytical Engine from French to English and in the margins she wrote examples of how to use the machine -- in effect becoming the first programmer ever.

American Herman Hollerith invented a method of using punched cards for automated data processing. His machines were employed by the US government to tabulate the 1890 census. Hollerith's firm later merged with three others to form International Business Machines (IBM). The punched card system remained in use well into the 1960s.

In 1944, Howard Aiken and his team completed the Mark I computer - the world's first automatic computer. It operated with electro-mechanical switches and was able to multiply two numbers in six seconds. In 1946, John W. Mauchly and J. Presper Eckert designed the first general-purpose electronic computer called ENIAC (E)lectronic (N)umerical (I)ntegrator (A)nd (C)omputer. It was hundreds of times faster than any electro-mechanical computing devices and could be programmed by the plugging of wires into holes along its outside.

Since the 1950s, computer systems have been available commercially. They have since become known by generation numbers.

First-generation computers (1950s)
----------------------------------

Marking the first generation of computers, Sperry-Rand introduced a commercial electronic computer, the UNIVAC I. Other companies soon followed suit, but these computers were bulky and unreliable by today's standards. For electronic switchings, they used vacuum tubes which generated a lot of heat and often burnt out. Most programs were written in machine language and made use of punched cards for data storage.

Second-generation computers (late 50s to mid-60s)
-------------------------------------------------

In the late 1950s, second generation computers were produced using transistors instead of vacuum tubes, which made them more reliable. Higher-level programming languages like FORTRAN, Algol and COBOL were developed at about this time, and many programmers began to use them instead of assembly or machine languages. This made programs more independent of specific computer systems. Manufacturers also provided larger amounts of primary memory and also introduced magnetic tapes for long-term data storage.

Third-generation computers (mid-60s to early 70s)
-------------------------------------------------

In 1964, IBM introduced its System/360 line of computers -- with every machine in the line able to run the same programs, but at different speeds. This generation of computers started to employ integrated circuits containing many transistors. Most ran in batch mode, with a few running in time-share mode.

Fourth-generation computers (early 70s and onwards)
---------------------------------------------------

From the early 1970s, computer designers have been concentrating on making smaller and smaller computer parts. Today, computers are assembled using very large-scale integration (VLSI) integrated circuits, each containing millions of transistors on single chips. This process has resulted in cheaper and more reliable computers. In the late 1960s and early 1970s, medium-sized organisations including colleges and universities began to use computers. Small businesses followed suit by the early 1980s. In this period, most were time-shared systems. Today's computers are usually single-user or multiple-user personal computers, with many connected to larger networks such as the Internet.

Programming a computer
======================

Algorithms
----------

An algorithm is a series of steps which must be followed in order for some task to be completed or for some problem to be solved.  You have probably used an algorithm before -- for example, you may have assembled a model toy by following instructions or cooked using a recipe. The steps in a set of instructions or a recipe form a kind of algorithm. They tell you how to transform components or ingredients into toys or cookies. The ingredients act as an input to the algorithm. The algorithm transforms the ingredients into the final output.

Recipes as algorithms (the structured approach to programming)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In a typical recipe, there is a list of ingredients and a list of steps. The recipes do not usually say who is performing the steps, but implies that you (the cook) should perform them. Many algorithms are written in this way, implying that the CPU of the computer is the *actor* of these instructions. This approach is referred to as the structured approach to programming and it works reasonably well for simple programs. However, it can become more complex when you are trying to solve a real world problem where it is rare for one actor to be in control of everything. The object-oriented approach to programming is an attempt to simulate the real world by including several actors in the algorithm.

Play scripts as algorithms (the object-oriented approach to programming)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A script of a play is a good analogy to the object-oriented (OO) approach. Actors and scenes are listed at the beginning (like the ingredients of a recipe). In a scene, the script lists the instructions for each actor to speak and act. Each actor is free to interpret these instructions (subject to the director's approval) in a way he or she sees appropriate. In the OO programming approach, multiple objects act together to accomplish a goal. The algorithm, like a play script, directs each object to perform particular steps in the correct order.

Programming languages
---------------------

To make use of an algorithm in a computer, we must first convert it to a program. We do this by using a programming language (a very formal language with strict rules about spelling and grammar) which the computer is able to convert unambiguously into computer instructions, or *machine language*.  In this course we will be using the Python programming language, but there are many other languages which we will outline later in the chapter.

The reason that we do not write computer instructions directly is that they are difficult for humans to read and understand. For example, these are the computer instructions (in the Intel 8086 machine language, a subset of the Intel Pentium machine language) required to add 17 and 20::

    1011 0000 0001 0001
    0000 0100 0001 0100
    1010 0010 0100 1000 0000 0000

The first line tells the computer to copy 17 into the AL register: the first four characters (1011) tell the computer to copy information into a register, the next four characters (0000) tell the computer to use register named AL, and the last eight digits (0001 0001, which is 17 in binary) specify the number to be copied.

As you can see, it is quite hard to write a program in machine language.  In the 1940s, the programmers of the first computers had to do this because there were no other options!  To simplify the programming process, *assembly language* was introduced.

Each assembly instruction corresponds to one machine language instruction, but it is more easily understood by humans, as can be seen in the equivalent addition program in the 8086 assembly language:

.. code-block:: nasm

    MOV AL, 17D
    ADD AL, 20D
    MOV [SUM], AL

Programs written in assembly language cannot be understood by the computer directly, so a translation step is needed. This is done using an assembler, whose job it is to translate from assembly language to machine language.

Although assembly language was a great improvement over machine language, it can still be quite cryptic, and it is so low-level that the simplest task requires many instructions.  *High-level languages* were developed to make programming even easier.

In a high-level language, an instruction may correspond to several machine language instructions, which makes programs easier to read and write.  This is the Python equivalent of the code above::

  sum = 17 + 20

Compilers, interpreters and the Python programming language
-----------------------------------------------------------

Programs written in high-level languages must also be translated into machine language before a computer can execute them.  Some programming languages translate the whole program at once and store the result in another file which is then executed. Some languages translate and execute programs line-by-line.  We call these languages *compiled* languages and *interpreted* languages, respectively.  Python is an interpreted language.

A compiled language comes with a *compiler*, which is a program which *compiles* source files to executable binary files.  An interpreted language comes with an *interpreter*, which *interprets* source files and executes them.  Interpretation can be less efficient than compilation, so interpreted languages have a reputation for being slow.

Programs which need to use a lot of computer resources, and which therefore need to be as efficient as possible, are often written in a language like C.  C is a compiled language which is in many ways lower-level than Python -- for example, a C programmer needs to handle a lot of memory management explicitly; something a Python programmer seldom needs to worry about.

This fine-grained control allows for a lot of optimisation, but can be time-consuming and error-prone.  For applications which are not resource-intensive, a language like Python allows programs to be developed more easily and rapidly, and the speed difference on a modern computer is usually negligible.

Developing a Python program
---------------------------

Suppose that we want to develop a program to display an average of a series of numbers. The first step is to understand the problem, but first we need to know more about the program:

* How will it get the numbers? Let's assume that the user will type them in using the keyboard.
* How will it know how many numbers to get? Let's assume that the user will enter 0 to signify the end of the list.
* Where should it display results? It should print them on the screen.

The second step is to come up with the algorithm. You can do this by trying to solve the problem yourself and noting the steps that you took. Try this. You are likely to end up with an instruction list which looks something like this:

#. Set running total to 0.
#. Set running count to 0.
#. Repeat these steps:

   * Read a value.
   * Check if value is 0 (stop this loop if so).
   * Add value to running total.
   * Add 1 to running count.

#. Compute the average by dividing the running total by the count.
#. Display the average.

The next step of development is to test the algorithm. You can do this by trying the algorithm on different lists of numbers and see if you can get a correct result from it. For simple algorithms such as this, you can do the test on paper or using a calculator. Try this with a simple list of numbers, like 1, 2, 3, 4 and 5. Then try a more complex list. You might get a feeling that this algorithm works for all cases. However, there is a case that the converted program might not be able to handle. Try a list which only contains 0. The average of a list with a single 0 in it is 0, but what does the algorithm tell you the answer is? Can you modify the algorithm to take care of this?

We now look at the four steps in developing a program in more detail.

Understanding the problem
^^^^^^^^^^^^^^^^^^^^^^^^^

Before you start writing a program, you should thoroughly understand the problem that you are trying to solve:

* When you start, think about the problem on your own without touching the keyboard. Figure out exactly what you need the algorithm to do.

* If the program is for someone else, it might be helpful to speak to those who will be using the program, to find out exactly what is needed. There might be missing information or constraints such as speed, robustness or ease of use.

* Think about what type of input and output the program will need to have, and how it will be entered and displayed.

* It can be useful to plan the program on paper by writing down lists of requirements or sketching a few diagrams. This can help you to gather your thoughts and spot any potential error or missing information.

Coming up with an algorithm
^^^^^^^^^^^^^^^^^^^^^^^^^^^

We have previously described an algorithm as a series of steps, but there are a few more formal requirements:

* It must be a *finite* series of steps: a never-ending list of steps is not an algorithm. A computer has finite resources (like memory) and cannot handle infinite lists of steps.

* It must be *unambiguous*: each step must be an unambiguous instruction.  For example, you cannot have a step which says "multiply x by either 1 or -1". If you have an instruction like this, you have to specify exactly how the choice should be made -- for example, "if y is less than 0, multiply x by 1, otherwise multiply x by -1".

* It must be *effective*: The algorithm must do what it is supposed to do.

* It must *terminate*: The algorithm must not go on forever. Note that this is different to the requirement that it be finite. Consider the following finite list of instructions:

    #. Set x to 1
    #. Set y to 2
    #. Repeat the following steps:
       #. Add x and y to get z
       #. Display z on screen
    #. Display the word 'Done'

  If you try to follow these instructions, you will get stuck on step 3 forever -- therefore, this list is not an algorithm.

Writing the program
^^^^^^^^^^^^^^^^^^^

Once you have an algorithm, you can translate it into Python.  Some parts of the algorithm may be straightforward to translate, but others may need to be expressed slightly differently in Python than they would be in a natural language.  Sometimes you can use the language's features to rewrite a program more cleanly or efficiently.  This will become easier the more experience you gain with Python.

You should take care to avoid errors by thinking through your program as you write it, section by section. This is called *desk checking*.  In later chapters we will also discuss other tools for checking your code, for example programs which automatically check the code for certain kinds of errors.

Testing the program
^^^^^^^^^^^^^^^^^^^

After thoroughly desk checking the program as you write, you should run it and test it with several different input values. Later in this module we will see how to write automated tests -- programs that you write to test your programs. Automated tests make it easy to run the same tests repeatedly to make sure that your program still works.

Programming languages
=====================

There are hundreds of different programming languages.  Some are particularly suited to certain tasks, while others are considered to be general-purpose.  Programs can be categorised into four major groups -- *procedural*, *functional*, *logic* and *object-oriented* languages -- but some languages contain features characteristic of more than one group.

Procedural languages
--------------------

Procedural (also known as imperative) languages form the largest group of languages. A program written in a procedural language consists of a list of statements, which the computer follows in order. Different parts of the program communicate with one another using variables. A variable is actually a named location in primary memory. The value stored in a variable can usually be changed throughout the program's execution. In some other programming language paradigms (such as logic languages), variables act more like variables used in mathematics and their values may not be changed.

BASIC is an example of a procedural programming language. It has a very simple syntax (originally only 14 statement types). Here is some BASIC code for adding 17 and 20:

.. code-block:: vbnet

    10 REM THIS BASIC PROGRAM CALCULATES THE SUM OF
    20 REM 17 AND 20, THEN DISPLAYS THE RESULT.
    30 LET RESULT = 17 + 20
    40 PRINT "The sum of 17 and 20 is ", RESULT
    50 END


In the early 1990s, Microsoft's Visual Basic extended the BASIC language to a development system for Microsoft Windows.

COBOL (COmmon Business Oriented Language) has commonly been used in business. It was designed for ease of data movement. Here's the addition program written in COBOL:

.. code-block:: cobol

    IDENTIFICATION DIVISION.
    PROGRAM-ID.      ADDING.
    DATE-WRITTEN.    JUL 11,1997.
    DATE-COMPILED.   JUL 12,1997.
    *    THIS COBOL PROGRAM CALCULATE THE SUM
    *    OF 17 AND 20. IT THEN DISPLAYS THE RESULT.
    ENVIRONMENT DIVISION.
    CONFIGURATION SECTION.
    SOURCE-COMPUTER. IBM-370.
    OBJECT-COMPUTER. IBM-370.
    DATA DIVISION.
    WORKING-STORAGE SECTION.
    77  TOTAL          PICTURE 99.
    PROCEDURE DIVISION.
      ADD 17, 20 GIVING TOTAL.
      DISPLAY 'THE SUM OF 17 AND 20 IS ', TOTAL UPON CONSOLE.
      STOP RUN.
    END PROGRAM

FORTRAN (FORmula TRANslator) was popular with scientists and engineers, but many have switched to C and C++. It was the first high-level language. Here's the addition program written in FORTRAN:

.. code-block:: fortran

         PROGRAM ADDNUMS
    C    THIS FORTRAN PROGRAM FINDS THE TOTAL OF
    C    17 AND 20, THEN DISPLAYS THE RESULT.

         INTEGER RESULT
         RESULT = 17 + 20
         WRITE (*, 10) RESULT
      10 FORMAT ('THE SUM OF 17 AND 20 IS ', I2)
         STOP
         END

Many programmers use C to write system-level code (operating systems, compilers). Here's the addition program code written in C:

.. code-block:: c

    /* This C program calculates the sum of 17 and 20.
    It then displays the result. */

    #include <stdio.h>

    void main(void)
    {
        int result;
        result = 17 + 20;
        printf("The sum of 17 and 20 is %d\n", result);
    }

Pascal (named after Blaise Pascal) used to be a popular introductory programming language until the early 1990s, but many schools have switched to C++ or Java. Here is the addition program written in Pascal:

.. code-block:: pascal

    PROGRAM
    AddNums (Input, Output);
    { This Pascal program calculate the sum of 17 and 20. It then displays the result }

    BEGIN
       Result := 17 + 20;
       writeLn ('The sum of 17 and 20 is ', Result)
    END

Functional and logic languages
------------------------------

A functional language is based on mathematical functions. It usually consists of functions and function calls. In the language's pure form, variables do not exist: instead, parts of program communicate through the use of function parameters. One of the most popular functional languages is Common Lisp, which is widely used in the artificial intelligence field, especially in the US. Other functional languages include ML and Miranda. Here's the addition program written using a functional style, in Common Lisp:

.. code-block:: common-lisp

    ;; This Lisp program calculates the
    ;; sum of 20 and 17. It then displays the result.
    (format t "The sum of 20 and 17 is ~D~%" (+ 20 17))

A logic language is based on formal rules of logic and inference. An example of such a language is Prolog. Prolog's variables cannot be changed once they are set, which is typical of a logic language. Here's the addition program written in Prolog:

.. code-block:: prolog

    /* This Prolog program calculates the sum of 17 and 20. It then
    /* displays the result. */

    run :- Result is 17 + 20,
        write("The sum of 17 and 20 is ", Result),
        nl.

The above program does not show the deductive power of Prolog. Prolog programs can consist of a set of known facts, plus rules for inferring new facts from existing ones. In the example below, the first seven lines list facts about the kind of drink certain people like. The last line is a rule of inference which says that Matt likes a drink only when both Mike and Mary like that drink:

.. code-block:: prolog

    /* Shows Prolog's inference ability */
    likes(dave, cola).
    likes(dave, orange_juice).
    likes(mary, lemonade).
    likes(mary, orange_juice).
    likes(mike, sparkling_water).
    likes(mike, orange_juice).
    likes(matt, Drink) :- likes(mary, Drink), likes(mike, Drink).

A Prolog program answers a query. For example, we might want to know what food Mary likes -- we can query this:

.. code-block:: prolog

    likes(mary, Drink).

To which Prolog will output possible answers, like:

.. code-block:: prolog

    Drink = lemonade
    Drink = orange_juice

To demonstrate the rule of inference, we can ask for the food that Matt likes. The system can find the solution by checking what Mary and Mike like:

.. code-block:: prolog

    likes(matt, Drink)

    Drink = orange_juice

Object-oriented languages
-------------------------

More recently, computer scientists have embraced a new programming approach -- object-oriented (OO) programming. In this approach, programmers model each real-world entity as an object, with each object having its own set of values and behaviours. This makes an object an active entity, whereas a variable in a procedural language is passive.

Simula (Simulation Language), invented in 1967, was the first language to take the object-oriented approach. However, Smalltalk (early 1980s) was the first purely object-oriented language -- everything in the language is an object. C++ is a hybrid OO language in that it has the procedural aspects of C. A C++ program can be completely procedural, completely OO or a hybrid. Most OO languages make use of variables in a similar fashion to procedural languages.

Here's the addition code written in C++; note the similarity to the earlier program written in C:

.. code-block:: cpp

    // This C++ program finds the result of adding 17 and 20.
    // It then displays the result.
    #include <iostream>

    int main(void)
    {
        int result = 17 + 20;
        std::cout << "The sum of 17 and 20 is " << result << std::endl;

        return 0;
    }

Java was introduced in 1995 by Sun Microsystems, who were purchased by Oracle Corporation during 2009-2010. It is an OO language but not as pure as Smalltalk. For example, in Java primitive values (numbers and characters) are not objects -- they are values. In Smalltalk, everything is an object. Initially it was designed for use in appliances, but the first released version was designed for use on the Internet.  Java syntax is quite similar to C and C++, but functions cannot be defined outside of objects.  Here is the addition code written in Java:

.. code-block:: java

    // This is a Java program to calculate the sum of
    // 17 and 20. It then displays the result.
    public class Add {
        public static void main(String[] args) {
            int result;
            result = 17 + 20;
            System.out.println("sum of 17 && 20 is " + result);
        }
    }

Python is a general-purpose interpreted language which was originally created in the late 1980s, but only became widely used in the 2000s after the release of version 2.0.  It is known for its clear, simple syntax and its dynamic typing -- the same variables in Python can be reused to store values of different types; something which would not be allowed in a statically-typed language like C or Java.  Everything in Python is an object, but Python can be used to write code in multiple styles -- procedural, object-oriented or even functional.  Here is the addition code written in Python::

    # This Python program adds 17 and 20 and prints the result.
    result = 17 + 20
    print("The sum of 17 and 20 is %d." % result)
