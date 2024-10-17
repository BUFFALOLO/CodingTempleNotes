"""
1. E-Commerce Product Catalog
Objective: To develop proficiency in using Python dictionaries, lists, conditional statement, loops, functions, string manipulation & exception handling in a practical e-commerce context.
Problem Statement: Build a Python program to manage an e-commerce product catalog efficiently. 
The program should facilitate adding new product categories, adding products, displaying all available categories, & conducting product searches within the catalog
    Initialize a dictionary to represent your product
    Implement functions to:
        Add a new product category
        Add a product to an existing category
        Display all product categories with their respective products
        Search for a product across all categories
    Include error handling for situations such as adding a product to an unlisted category
    Ensure that the product search is case-sensitive
    Design the program to handle multiple additions & searches
HINTS:
Start by pre-populating your catalog dictionary with some categories & products
Utilize the lower() & upper() methods on strings for case-insensitive comparison
In your serach function, check for the product's presence in every category
Leverage try and except blocks to gracefully handle any KeyError instances
"""
def add_category(catalog, category):
    if category not in catalog:
        catalog[category] = []
        print(f"Category '{category}' added.")
    else:
        print(f" Category '{category}' already exists.")

def add_product(catalog, category, product):
    try:
        if product not in catalog[category]:
            catalog[category].append(product)
            print(f"Product '{product}' added to '{category}'.")
        else:
            print(f"Product '{product}' already exists in '{category}'.")
    except KeyError:
        print(f"Category '{category}' does not exist.")

def display_categories(catalog):
    for category, products in catalog.items():
        print(f"{category}: {','.join(products)}")

def search_product(catalog, product):
    found = False
    for category, products in catalog.items():
        if product.lower() in [p.lower() for p in products]:
            found = True
            print(f"Product '{product}' was found.")
            break
    if not found:
        print(f"Product '{product}' not found.")

catalog = {
    "Electronics": ["Laptop", "Smartphone"],
    "Books": ["Fiction", "Non-Fiction"]
}

add_category(catalog, "Clothing")
add_product(catalog, "Electronics", "Camera")
display_categories(catalog)
search_product(catalog, "laptop")

"""
2. The Simple Order Validator
Objective: Develop your Python programming skills by creating a program that validates user input for product orders. 
This exercise will focus on handling user input, validating it, & using try/except blocks to handle exceptions.
Problem Statement: An online bookstore is processing orders for a popular novel. They need a simply system to ensure that customers enter a valid qty when placing their orders.
    Prompt the user to enter the qty of books they wish to order
    Validate the input to ensure it is a positive integer
    If the input is valid, confirm the order by printing a message
    If the input is invalid (not an integer or a negative number), display an error message & prompt the user again
    Use a try/except block to catch non-numeric inputs
HINTS
Use a while loop to keep asking for input until a valid qty is entered
Utilize the int() function to convert the input to an integer & catch ValueError for non-numeric inputs
"""
def validate_order():
    while True:
        try:
            quantity = int(input("Enter the qunatity of books you want to order: "))
            if quantity > 0:
                print(f"Thank you! You have ordered {quantity} books!")
                break
            else:
                print("Invalid quantity. Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a number.")

validate_order()

"""
3. The Safe Calculator
Objective: Hone your Python error handling skills by creating a program that validates user input for a simple calculator app. 
This exercise will focus on using try-except blocks to ensure that the program only processes numerical inputs & handles exceptions gracefully.
Problem Statement: In a terminal-based calculator app, its crucial to ensure that the user inputs are valid numbers before any arithmetic operation is performed.
Your task is to enhance the app's robustness by implementing input validation that prevents the program from crashing when a user enters non-numeric data.
    Write a function safe_addition that prompts the user for two numbers & returns their sum. It should handle any ValueError exceptions that arise from non-numeric input
    Use a loop to allow the user to try entering the numbers again if they make an input error
    Print the result of the addition if the inputs are valid numbers
    Provide the user with the option to perform another addition or exit the program
HINTS
Use the try block to attempt to convert the user input to floats
Use the except block to catch ValueError & prompt the user to enter the numbers again.
"""
def safe_addition():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1 + num2
        except ValueError:
            print("Please enter only numbers. Try again")

while True:
    result = safe_addition() 
    print(f"The sum is: {result}")

    continue_input = input("Would you like to perform another addition? (yes/no): ").lower()
    if continue_input != 'yes':
        break

"""
4. The Resilient Divider
Objective: Develop your Python exception handling skills by creating a program that safely performs division operations.
This exercise will focus on using try-except blocks to handle ZeroDivisionError exceptions & provide user-friendly feedback
Problem Statement: In a data analysis context, dividing by zero can often occur & lead to program crashes. 
Your task is to create a function that performs division but returns a specific message instead of crashing when a division by zero is attempted.
    Write a function safe_divide that takes 2 parameters, a & b, & returns the result of a/n.
    Implement error handling to catch ZeroDivisionError exceptions within the function
    If division by zero occurs, the function should return a message indicating that division by zero is not allowed
    Test the function with user input & print the result or error message
HINTS
Use the try block to attempt to convert the user input to floats
Use the except block to catch ValueError & prompt the user to enter the numbers again
"""
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero is not allowed."

while True:
    try:
        numerator = float(input("Enter the numerator: "))
        denomiator = float(input("Enter the denomiator: "))
        result = safe_divide(numerator, denomiator)
        print(f"The result of division is: {result}")
    except ValueError:
        print("Please enter only numbers.")

    continue_input = input("Would you like to perform another division? (yes/no): ").lower()
    if continue_input != 'yes':
        break

"""
5. The Login Gatekeeper
Objective: Enhance your Python skills in creaing custom exceptions by developing a login system that validates username criteria. 
This exercise will focus on defining a custom exception & using it to enforce username standards
Problem Statement: In software application, it's crucial to ensure that user credentials meet certain security standards.
Your task is to create a function that checks whether a username meets the required criteria & raises a custom exception if it does not.
    Define a custom exception class name UsernameError that inherits from the base Exception class
    Write a function check_username that takes a single parameter, username, & checks if it meets the criteria (ex: at lease 6 characters long)
    If the username does not meet the criteria, raise a UsernameError with an appropriate error message
    Prompt the user to input a username & use a try-except block to catch the UsernameError & display the error message
HINTS
Use the raise keyword to raise the custom exception with a message when the username is too short
In the except block, catch the UsernameError & print the message to inform the user
"""
class UsernameError(Exception):
    def __init__(self, message):
        self.message = message

def check_username(username):
    if len(username) < 6:
        raise UsernameError("Username must be at least 6 characters long.")
    
while True:
    username_input = input("Please enter your username: ")
    try:
        check_username(username_input)
        print("Username is valid.")
        break
    except UsernameError:
        print(f"Error: {UsernameError.message}")

    try_again_input = input("Would you like to try a different username? (yes/no): ")
    if try_again_input != 'yes':
        break

"""
6: The Data Sanitizer
Objective: Refine your Python exception handling skills by writing a program that processes & sanitizes a list of data entries.
This exercise will ofcus on converting strings to integers & handling exceptions for non-convertible values
Problem Statement: In data processing applications, it's common to encounter a mix of valid & invalid data entries.
Your task is to write a program that attempts to convert a list of string values to integers, gracefully handling any values that cannot be converted
    Create a list of strings where some represent integer values & others are non-numeric
    Iterate over the list & attempt to convert each string to an integer
    If a string cannot be converted to an integer, catch the ValueError & print a warning message
    Store the successfully converted integers in a new list called parsed_data
HINTS
Use the raise keyword to raise the custom exception with a message when the username is too short
In the except block, catch the UsernameError & print the message to inform the user
"""
data_entries = ["100", "200", "three", "400", "5ive"]
parsed_data = []

for entry in data_entries:
    try:
        parsed_data.append(int(entry))
    except ValueError:
        print(f"Warning: '{entry}' is not a valid integer & will be skipped")

print(f"Parsed Data: {parsed_data}")

"""
7: The Server's Graceful Exit
Objective: Enhance your Python exception handling & resource management skills by ensuring a server-like application can exit gracefully under any circumstance
Problem Statement: In server applications, unexpected exceptions can occur, & it's crucial to handle these gracefully to prevent data loss & ensure necessary cleanup is performed.
Your task is to simulate a server's main operation loop & implement a mechanism that guarantees a graceful shutdown, even if an error occurs
    Simulate a server's main loop with a placeholder comment
    Use a try-except-finally block to handle any potential exceptions during the servers runtime.
    In the except block, catch a general excpetion & print an error message
    In the finally block, perform cleanup operations & print a shutdown message
HINTS
The finally block is executed after try & except blocks, regardless of whether an exception is raised or not
Use the finally block to include any code that you want to execute regardless of exceptions, such as closing files or releasing resources
"""
try:
    print("Server is running....")
    # simulate an error
    raise Exception("Unexpected error!")
except Exception as e:
    print(f"An error occures: {e}!")
finally:
    print("Performing cleanup operations.....")
    print("Shutting down server gracefully")

"""
8: User Input Validation with Fallback
Objective: Practice using the try-except-else block in Python to validate user input against a list of allowed values.
Problem Statement: In user-driven applications, it's common to require input that matches specific criteria.
Your task is to write a program that prompts the user for their favorite fruite from a predefined list. 
If the input is not in the list, the program should handle the situation gracefully & ask for input again
    Create a list of fruits that are allowed inputs
    Prompt the user to enter their favorite fruit
    Use a try-except-else block to validate the input
    If the input is not in the list, raise a ValueError & handle it by asking for input again
    If the input is valid, print a confirmation message
HINTS
The else block can be used to execute code when the try block doesn't raise an exception
Use a loop to keep asking for input until a valid fruit is entered
"""
allowed_fruits = ["apple", "banana", "cherry", "strawberry", "blueberry"]
while True:
    try:
        favorite_fruit = input("Enter your favorite fruit: ").lower()
        if favorite_fruit not in allowed_fruits:
            raise ValueError("Fruit not in the list")
    except ValueError as ve:
        print(ve)
        print("Please choose a fruit from the list.")
    else:
        print(f"Great choice! Your favorite fruit is {favorite_fruit}.")
        break

"""
9. Multi-Scenario Input Handling
Objective: Learn to handle multiple types of exceptions that may arise from user in put in a software application.
Problem Statement: In a software application that processes user data, it's essential to anticipate & handle different kinds of erroneous input.
Your task is to write a program that asks users for their age & ensures that the input is both a number & within a reasonable range.
    Prompt the use to enter their age
    Use a try-except block to handle the following scenarios
        The input is not a number (ValueError)
        The number is not within ht range of 0 to 120 (ValueError)
    If an exception is raised, provide a specific error message for the type of exception & ask for the input again
    If the input is valid, print a confirmation message
HINTS
Use int() to convert the input to an integer & catch any ValueError exceptions
Check the age range within the try block & raise a ValueError with a custom message if the age is out of range
"""
while True:
    try:
        user_age = input("Enter your age: ")
        age = int(user_age)
        if age <0 or age > 120:
            raise ValueError("Age must be between 0 and 120.")
    except ValueError as ve:
        if "invalid literal" in str(ve):
            print("That's not a number. Please enter your age using digits")
        else:
            print(ve)
    else:
        print(f"Thank you. Your age is recorded as {age}")
        break

"""
10. Robust Calculator Input Handling
Objective: To practice handling different types of exceptions in user input, specifically focusing on ValueError & TypeError, & ensuring the program concludes gracefully using a finally block
Problem Statement: You are developing a calculator app that can perform basic arithmetic operations. 
The app should robustly handle user input, ensuring that only numerical values are accepted & operations are performed correctly.
    Ask the user to enter a mathematical expressionAsk the user to enter 2 numbers
    Ask the user to choose an operation (addition, subtraction, multiplication or division)
    Perform the operation & display the end result
    Use a try-except block to handle ValueError & TypeError exceptions
    No matter what happens, thank the use for using the calculator in a finally block
HINTS
Use float() to convert the input strings to numbers
Use an if-elif-else structure to perform chosen operation
In the except blocks, handle ValueError for non-numeric  input & TypeError for incorrect operations (like division by zero)
Use the finally block to print a thank you message
"""
def get_numper(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That's not a valid number. Please try again.")

def get_operation():
    operations = ['+', '-', '*', '/']
    while True:
        op = input("Choose an operation (+, -, *, /): ")
        if op in operations:
            return op
        print("Invalid operation. Please choose +, -, *, /.")

num1 = get_number("Enter the first number: ")
num1 = get_number("Enter the second number: ")
operation = get_operation()

try:
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    print(f"The result is {result}.")
except TypeError:
    print("An unexpected type error occured")
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Thank you for using the calculator!")

"""
11. Nested Try Blocks in Data Entry
Objective: To practice using nested try blocks to handle different types of exceptions, specifically focusing on ValueError & TypeError, & to use the else block for code that should only run if no exceptions were raised.
Problem Statement: You are creating a data entry module for a software application where users can add numerical data to a list.
The module should validate the input & handle errors when users enter invalid data or attempt incorrect operations.
    Initialize an empty list to store numerical entries
    Prompt the user to enter a number or done to finish
    Use a nested try block to handle the following:
        Convert the input to a float & append it to the list
        If the user enters done, break out of the loop
    Use an else block to confirm the entry has been added
    Handle ValueError for non-numeric input & TypeError for any type-related errors during conversion
    Use a finally block within the nested try to inform the user that they can continue entering data
    After the loop, print the list of entered numbers
HINT
Use a while loop to continously prompt the user for input
Use float() to attempt to convert the input to a number
Use an else block after the try block to print a confirmation message
"""
def data_entry():
    data_list = []
    while True:
        user_input = input("Enter a number or type 'done' to finish: ")
        if user_input.lower() == 'done':
            break

        try:
            try:
                number = float(user_input)
            except ValueError:
                print("That's not a number. Please enter a valid number")
                continue
            else:
                data_list.append(number)
        except TypeError:
            print("An unexpected type error occured.")
        finally:
            print("You can enter another number or type 'done' to finish. ")

    print("Data entered:", data_list)