# OVERVIEW OF MODULES IN PYTHON

"""
Think of modules as a versatile digital toolbox in the vast world of programming. 
Just as a mechanic reaches into their toolbox to grab a wrench or a screwdriver, a programmer can reach into their
collection of modules for the perfect tool to solve a particular problem.

A module is a file containing Python code. This code can include functions, classes or variables.
These tools are designed to perform specific tasks. For example, the math module is like a specialized toolkit for math operations.

Why use modules? Efficiency, Organization & Reusability

math: for mathematical tasks
datetime: when working with dates and times
os: to interact with your operating system

import math
import datetime
import os

To import only the sqrt function from math you would use the below:
from math import sqrt

If you want to shorten or use a different variable you would use the below:
import datetime as dt
now = dt.datetime.now()
You can now use this nicknamed tool for convenience

What happens when you need a tool that's not in your standard toolbox? This is where the art of creating custom modules comes in.
Advantages of Custom Modules: 
    Precision - it does what you need
    Efficiency - module can be reused in multiple projects saving time
    Understanding - understanding of Python and programming put into practice
"""

# CREATING A CUSTOM MODULE
# 1. Start with a blueprint planning what the module will contain (functions, classes or variables)
# 2. Forge your tool, this is where you turn your blueprint into a reality

# FOR THIS EXAMPLE YOU WOULD CREATE A NEW .PY FILE NAMED geometry.py & THE BELOW CODE WOULD BE THE ONLY THING IN THAT FILE
def area_rectangle(length, width):
    return length * width

def perimeter_rectangle(length, width):
    return 2 * (length,width)

# 3. Temper & Test, test your module by importing it into a Python script & trying out its functions
import geometry
print(geometry.area_rectangle(5, 3))
print(geometry.perimeter_rectangle(5,3))

"""
BEST PRACTICES & COMMON PITFALLS IN PYTHON MODULES

Keep Your Toolbox Tidy: Group your standard library imports, third-party imports, & custom module imports separately,
& always place them at the top of your file.

Use Tools Appropriately: Avoid overloading a module with unrelated functions or variables.

Regular Maintenance - Updating Modules: Stay current with the latest versions of the modules you use, improvements & security patches.

Label Your Custom Tools: Use clear & descriptive names.

Avoid Overloading the Toolbox: Avoid unnecessary memory usage & potential conflicts by importing only what you need.

Misplacing Tools: Be precise with your import statements.

Neglecting to Return Tools: Be cautious about using from module import *.

Ignoring the Manual: Always take the time to understand the modules you are using to avoid misuse. 
"""

