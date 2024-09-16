"""
Python Cafe Naming Conventions (just a demonstration, there is no output from this code!)
"""

# Snake Case for variables
cup_of_coffee = "Espresso"
cup_of_tea = "Green Tea"

# Camel Case for funcations
def orderCoffee():
    return "One coffee coming right up!"

def orderTea():
    return "A cup of tea for your thoughts!"

# Pascal Case for classess
class CoffeeMug:
    def __init__(self, size="medium"):
        self.size = size

# UPPERCASE for constants
TABLES = 10

# UPPER SNAKE CASE for constants with multiple words
MAX_SEATING_CAPACITY = 40

# Python Cafe where Coffee and coffee are 2 different things
Coffee = "Strong dark roast"
coffee = "Light cold brew"

print("Welcome to Python Cafe!")

print("\nIn Python: ")
print("'Coffee' holds: " + Coffee)
print("'coffee' holds: " + coffee)

favorite_ice_cream = "chocolate"
print(favorite_ice_cream)    

amount = 100
print(type(amount))

user_print = input("Enter a number: ")
print(type(user_print))
# This will be a str type even if the user enters 11 rather then eleven because the input function always returns strings

# Casting to Integers - When you need whole numbers
num = "123"
print(type(num))

num2 = int(num)
print(type(num2))

# Casting to Float - When you need decimal numbers
num3 = "123.456"
print(type(num3))

num4 = float(num3)
print(type(num4))

# Casting to Strings - When you need words
num5 = 123
print(type(num5))

num6 = str(num5)
print(type(num6))

# Constants are always ALL CAPS
PI = 3.14159
print(PI)

