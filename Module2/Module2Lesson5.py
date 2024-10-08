# Functions are a set of instructions that you can “call” upon whenever needed, without having to rewrite the whole thing every time.
age = 25
name = "Alice"
hobby = "painting"

print("Hello, Coding Temple") # Printing Simple Text
print(age) # Printing Variables
print(3.14) # Printing Numbers
print(name, "loves", hobby) # Printing Multiple Items

# SPECIAL CHARACTERS IN PRINT STATEMENT: Newline = \n | Tab = \t | Backslash = \\
print("Hello, \nWorld!")
print("Hello, \tWorld!")
print("This is a backslash: \\")
print('She said, \'Hello!\'')
print("He replied, \"Hi there!\"")

# String Concatenation - Beware of Spaces: When using the + operator, spaces aren’t automatically added between strings, so you’ll need to include them yourself. 
greeting = "Hello"
name = "John"

print(greeting + ", " + name + "!")

age = 30
print(name + " is " + str(age) + " years old.")

# Separators & Endings: Ever wanted to deliver a message with a specific style? print( ) lets you do just that with sep and end parameters. 
print("apple", "banana", "cherry", sep="-")
print("This is just the beginning...", end="")
print(" and here's the continuation.")
print("apple", "banana", "cherry", sep="-", end="...yum!")

# String Formatting with Placeholders
name = "Ella"
print("Her name is %s." % name)

age = 25
print("She is {} years old." .format(age))

hobby = "writing"
print("Ella loves {hobby}.")

pi = 3.141592653589793
print(f"The value of PI to 3 decimal places is {pi:.2f}.")

# Getting User Input: Regardless of what the user types, it ALWAYS returns as a STRING, a sequence of characters that could be words, numbers, or anything else you can type out.
# If you need a number or another data type, you'll have to convert it.
name = input("What is your name? ")
print(f"Hello, {name}!")

age = int(input("How old are you? "))
print(f"Next year, you'll be {age + 1} years old.")

# Using Input for Decisions
answer = input("Do you like Python? (yes/no) ")
if answer == "yes":
    print("That's great to hear!")
else:
    print("Oh, why not?")

# TYPE CONVERTERS - str() | float() | int() | bool()
number_string = "123"
number = int(number_string)

decimal_string = "3.14"
pi = float(decimal_string)

age = 25
age_string = str(age)

is_empty = bool("")

print(number + 1)
print(pi + 2)
print("I am " + age_string + " years old")
print(is_empty)

# type( ) = reveals if it is a str, int, float, bool
# len( ) = how long a string is or how many items are hiding in a list
# isinstance( ) = checks if something is really what it claims to be

mystery_variable = "Sherlock"
clue_list = ["candlestick", "footprint", "hankerchief"]
alleged_title = 1234

print("Type of mystery_variable: ", type(mystery_variable))
print("Number of clues found: ", len(clue_list))
print("Is the title genuine? ", isinstance(alleged_title, int))

# Mathematical Functions
import math

scores = [1, 5, 10, 8, 4, 2]
angle = 10

print(abs(-2023), round(3.14159, 2), sum([1, 2, 3, 4, 5]))
print(min(scores), max(scores), pow(2, 3), divmod(10,3))
print(math.sqrt(16), math.ceil(2.1), math.floor(2.9))
print(math.exp(1), math.log(10))
print(math.sin(angle), math.cos(angle), math.tan(angle))
print(math.radians(100), math.degrees(math.pi))

