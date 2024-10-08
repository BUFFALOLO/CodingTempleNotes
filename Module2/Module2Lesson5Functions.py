# DEFINING FUNCTIONS
def greet_user():
    print("Hello, user!")

greet_user()

# Parameters = Represent values that you’ll provide later when you call the function. 
def cook_pasta(sauce_type):
    print(f"Cooking pasta with {sauce_type} sauce!")

cook_pasta("marinara")

# Multiple parameters are separated by commas.

def make_sandwich(bread_type, filling):
    print(f"Making a {filling} sandwich with {bread_type} bread!")

make_sandwich("whole grain", "turkey")

# Default Parameter Values: You can set a default value for a parameter, ensuring that even if you don’t specify something the function has a go-to choice.
def brew_coffee(size="medium"):
    print(f"Brewing a {size} coffee!")

brew_coffee()
brew_coffee("large")

# Passing Lists to Python Functions: You’ve got a function, let’s call it prepare_snacks, & you want it to handle a whole list of snack preferences at once. You can pass the entire list to the function and let it do the heavy lifting for you.
def prepare_snacks(snack_list):
    for snack in snack_list:
        print(f"Preparing {snack}...Done!")

# List of snack for movie night
movie_snacks = ['popcorn', 'chocolate', 'fruit', 'nachos']

# Call the function with the list

prepare_snacks(movie_snacks)

# Arbitrary Arguments: When uncertain about the number of arguments a function should take, you employ arbitrary arguments.
# *args = allows the function to accept any number of position arguments. With *args , any number of extra arguments can be tacked on to your current formal parameters (including zero extra arguments). 
# Using the *, the variable that we associate with the * becomes iterable meaning you can do things like iterate over it.
def make_ice_cream(*flavors):
    for flavor in flavors:
        print(f"Scooping {flavor} ice cream!")
make_ice_cream("vanilla", "chocolate", "strawberry")

# **kwargs = enables the function to accept any number of keyword arguments. A keyword argument is where you provide a name to the variable as you pass it into the function. 
# It's like a dictionary mapping each keyword to its value, this creates a flexible structure with no fixed order when iterating over **kwargs.

def make_sammy(**ingredients):
    for item, quantity in ingredients.items():
        print(f"Adding {quantity} of {item} to the sandwich.")

make_sammy(tomatoes ="3 slices", lettuce="2 leaves", mayo="1 spread")

# Return Values: Using return values in function is like sending a letter to a friend & eagerly awaiting a reply. 
# Just as you give something to the function & receive something in return, it’s the function saying, “Hey, I’ve done the job, & here's what I found”.
# A return statement will end a function
# When a function returns a value, you can “catch” that value & store it in a variable.

def add_numbers(a, b):
    return a + b # This isn't the same as a print statement.

add_numbers(1, 4)

def add_number(c, d):
    return c + d

result = add_number(5, 3)
print(result)

# A function can have multiple return statements, but it will exit as soon as it hits the first one. This is useful when you have conditions in your functions.
def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
result = check_even(5)
print(result)

# Returning Multiple Values - Sometimes, one return value just isn’t enough. Python allows you to return multiple values in the form of a tuple.
def get_details():
    name = "Alex"
    age = 30
    return name, age

person_name, person_age = get_details()
print(person_name, person_age)

# Local Scope - When you define a variable inside a function, it's like placing an item in one of the rooms on a specific floor. 
# This variable is only known in that room (function) and is called a local variable. 
def greet():
    message = "Hello World"
    print(message)

greet()

# Global Scope - Variables defined outside all functions, in the main body of your script, are like items placed in the hallway of a floor. 
# These are called global variables.
name = "Alice"

def say_hello():
    print(f"Hello, {name}!")

say_hello()

# If a local variable shares the same name as a global variable, the function will always prioritize its local items over the global items. 
# Sometimes, from within a function, you might want to change an item in the global variable. Python provides the global keyword for this. 
counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)

# Pass statements with functions
def calculate_interest():
    pass # TODO: IMPLREMENT INTEREST CALCULATION

def upcoming_feature():
    pass # PLACEHOLDER FOR A FUTURE FEATURE

def unfinished_logic():
    pass # STUB FOR INCOMPLETE LOGIC

# USING FUNCTIONS
calculate_interest()
upcoming_feature()
unfinished_logic()