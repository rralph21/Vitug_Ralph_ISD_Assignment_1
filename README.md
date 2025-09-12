# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author
Ralph Vitug

## Assignment
Assignment 1 : In this assignment, knowledge gained in Module 01 will be leveraged to develop classes to support a larger system.
As well as knowledge from Fundamentals class will be leveraged.

## Encapsulation
In this assignment, encapsulation was achieved by making data private and only allowing controlled or limited access through public method(accessor) and properties. In the BankAccount class, attributes such as account_number, client_number and balance are private, meaning access from the outside world is restricted. @property(declared as a stereotype on UML provided) allowed controlled or limited access, which let other parts of the assignment read the values without the capability to modify them. Only changes were allowed through methods like deposit, withdraw, and update balance, as well as exceptions that ensured values are numeric(integer, float), positive and within limits.