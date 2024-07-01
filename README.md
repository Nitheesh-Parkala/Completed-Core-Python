# Day-4
## Overview
This repository contains a simple Python class example for a Fan. This example is intended to help beginners understand the basics of class creation, initialization, and method definition in Python.

## Features
The Fan class in this example includes:

Initialization of attributes (brand, color, cost)
Two methods (on, rotate) that perform simple actions
## Class Explanation
__init__ Method
The __init__ method is a special method in Python classes. It is called the constructor and is automatically invoked when an instance of the class is created. In this example, the __init__ method initializes three attributes of the Fan class:

brand: Represents the brand of the fan, set to "Usha".
color: Represents the color of the fan, set to "White".
cost: Represents the cost of the fan, set to 2000.
## Methods
The class contains two methods:

on Method: This method prints a message indicating that the fan is on.
rotate Method: This method prints a message indicating that the fan is rotating.
Creating an Instance
An instance of the Fan class is created using the following line:

## Creating an Instance
An instance of the Fan class is created using the following line:
f = Fan()
This line calls the __init__ method and initializes the attributes for the new instance f.

## Accessing Attributes
The attributes of the instance f can be accessed and printed using the print function:
print(f.brand)  # Prints the brand of the fan
print(f.color)  # Prints the color of the fan
print(f.cost)   # Prints the cost of the fan

## Learning Objectives
This example aims to teach beginners the following concepts:

How to define a class in Python.
How to use the __init__ method to initialize class attributes.
How to define and call methods within a class.
How to create an instance of a class and access its attributes.
By studying and running this code, beginners can gain a fundamental understanding of object-oriented programming in Python.