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
==================

History of computers
====================

Programming a computer
======================

Programming languages
=====================


Summary
=======

A computer is simply a machine that follows a list of instructions -
also known as programs. At the lowest-level, each instruction is
simple eg. adding two numbers.

A computer consists of four major parts - input devices, CPU, memory
and output devices. The computer can be regarded as an information
processing machine, taking in information from input devices,
processing it with the CPU and then displaying the result on an output
device. While processing, the computer can save the information for
later use in the memory.

There are two kinds of memory - primary and secondary memory. Primary
memory is closely linked to the CPU and is volatile. It is much faster
than secondary memory but this comes at a price. Secondary memory is
separate from the CPU and does not lose its content when the computer
is switched off. Primary memory also stores contents in addressable
cells that can each hold a single value, in contrast to secondary
memory, which stores information in files.

At the lowest level, computers understand machine language with
assembly language one level up. Each assembler instruction corresponds
to a machine instruction, but it allows humans to easily read it. An
assembler is needed to translate assembly language into machine
language.

High-level languages were developed to make it easier for human to
read and understand. A compiler is needed to convert programs written
in these languages to machine language. High-level languages can be
grouped into four types. Procedural languages include BASIC, C, COBOL,
FORTRAN and Pascal. An example of a functional language is Lisp, while
Prolog is a common logic language. C++ is a hybrid language - a
combination of procedural and object-oriented , while Java and
Smalltalk are object-oriented languages.

Computer systems can be grouped into four types. A single-user
personal computer is one that can be used by a single user at a
time. Many people can share the use of a computer via terminals in a
time-share system. A batch computer is very efficient but not
interactive. A network is a group of linked computers.

Computers have evolved exponentially over time - from expensive large
room-sized machine to today's affordable and compact units.
