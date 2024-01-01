# Brief overview of OOP and its benefits.
Object-Oriented Programming is a programming paradigm that revolves around the concept of "objects.". It is believed that everything in python is an object. An object is a self-contained unit that represents a real-world entity or concept. OOP has four key concepts:
** Inheritance
** Encapsulation
** Abstraction
** Polymorphism

# Introduction to classes and objects.
Classes:
A class is a blueprint or template for creating objects. It defines the properties (attributes) and behaviors (methods) that the objects created from the class will have.

Objects:
An object is simple an instance of a class,with specific values assigned to its attributes.

- Explanation of inheritance in Python.
Inheritance is a core concept in Object-Oriented Programming (OOP) that allows a new class (called the derived class, child class, or subclass) to inherit attributes and methods from an existing class (called the base class, parent class, or superclass). This enables the reuse and extension of code, promoting a hierarchical structure in your codebase.

Analogy:
Analogous to the way children inherit traits and characteristics from their parents, a derived class inherits properties and behaviors from its parent class.

Major Benefit:
The primary advantage of inheritance is to enhance code reusability. Instead of duplicating code in multiple classes, you can create a common base class and have multiple derived classes inherit from it.

Important Notes about Derived Classes:

Adding Own Attributes and Behaviors:
Derived classes can have their own attributes and behaviors, in addition to those inherited from the base class.

Method Redefinition in Derived Classes:
You can redefine or modify a method from the base class in the derived class. This is known as method overriding.

Method Overriding:
Method overriding allows a derived class to provide a specific implementation for a method that is already defined in its base class. This helps customize the behavior of the method in the context of the derived class.

super() Function:
The super() function is used to call a method from the base class. It allows you to invoke the method of the superclass within the derived class, facilitating code reuse and ensuring that both the base and derived class implementations are executed.