# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author
Ralph Vitug

## Assignment
Assignment 1 : In this assignment, knowledge gained in Module 01 will be leveraged to develop classes to support a larger system.
As well as knowledge from Fundamentals class will be leveraged.

Assignment 2: Added chequing, investment and savings accounts. This assignment will highlight Abstraction, Inheritance and Polymorphism.

Assignment 3: Strategy pattern and Obeserver pattern where service charge became an abstract class that the rest of the charges from 
different accounts inherits and delivered their own method (polymorphism). Observer pattern is the method that updates clients whenever
there is an unsual activity.

Assignment 4: Graphical user interface (GUI) and PySide6: Event-Driven Programmin paradigm is organized around detection, handling and 
responding to events. Event-Driven Components are ; Event, Event Hanlder, Signal, Slot and Event loops.

## Encapsulation
In this assignment, encapsulation was achieved by making data private and only allowing controlled or limited access through public method(accessor) and properties. In the BankAccount class, attributes such as account_number, client_number and balance are private, meaning access from the outside world is restricted. @property(declared as a stereotype on UML provided) allowed controlled or limited access, which let other parts of the assignment read the values without the capability to modify them. Only changes were allowed through methods like deposit, withdraw, and update balance, as well as exceptions that ensured values are numeric(integer, float), positive and within limits.

## Polymorphism
In Assignment 2, polymorphism in the BankAccount sublasses means they all use the same get_service_charges method name, but each one calculates the charges in its own way. Just like in the activity where, Shapes used the same calculate_perimeter and calculate_are method name, but each one calculates differently depending if its triangle or rectangle.
It significantly reduced redundancy of codes, specially with different types of accounts.

## Strategy Pattern
In Assignment 3, Strategy pattern is used to handle different ways of calculating service charges for various
types of bank account. Instead of putting all the calculation rules inside the BankAccount class, each account
type uses its own strategy. Like the analogy given in class, "Calculator" it has different methods.
Strategy Pattern significantly reduced redundancy in coding.

## Observer Pattern
In Assignment 3, Observer Pattern is used to create a communication link between Subject (BankAccount)
and Client (Observer). When an important activity happens to a bank account, the client is notified.

## Event-Driven Programming Paradigm

In Assignment 3, Event-Driven Programming paradigm is used by reacting to user
actions through a network of connected signals and slots. Insteat of executing code in a fixed sequence, the program waits for events, such as button clicks, text changes or table selections, and responds by calling the appropriate handler methods.