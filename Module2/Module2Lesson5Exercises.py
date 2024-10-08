# 1: The Username Validator
"""
In the digital age, usernames are cruical for identity on various platforms
Your task is to write a program that checks if a username is neither too short nor too long, adhering to specific length criteria
    Prompt the user to enter a username
    Check if the username is between 5 & 15 characters long
    If the username meets the criteria, print a confirmation message
    If it does not meet the criteria, print a message indicating the username length requirements
    Provide the user iwth the optoin to try a different username or exit the program
"""
while True:
    username = input("Enter your desired username: ")

    if 5<= len(username) <=15:
        print("Username is valid")
    else:
        print("Username must be between 5 and 15 characters")

    continue_input = input("Do you want to try another username? (yes/no) ").lower()
    if continue_input != "yes":
        break

# 2: The Precise Price Tagger
"""
In retail applications, both online and in-store, displaying prices in a clear and precises manner is essential for customer satisfaction
Your task is to write a program that takes a price as input and rounds it to two decimal places, making it more user-friendly
    Prompt the user to enter a price
    Use the round() function to round the price to two decimal places
    Display the rounded price in a format that is easy for customers to understand
    Provide the user with the option to enter a new price or exit the program
"""
while True:

    price_input = float(input("Enter the price: "))
    rounded_price = round(price_input, 2)
    print(f"Rounded Price: ${rounded_price}")

    new_price = input("Would you like to enter in a new price? (yes/no) ").lower()
    if new_price != "yes":
        break

# 3: Global Temperature Translator
"""
You are creating a feature for a travel app that allows users to view the temperature in both Celsius and Farenheit so they can easily understand the weather forecast
    Create a list of temperatures in Celsius that you want to convert
    Loop through the list, and for each temperature in Celsius, conver it to Farenheit
    Print out both the Celcius and Farenheit temperatures using f-strings for formatted output
"""
celsius_temperatures = [10, 20, 25, 30, 35]

for celsius in celsius_temperatures:
    farenheit = (celsius * 9/5) + 32
    print(f"{celsius}C is equivalent to {farenheit}F")

# 4. The Goldilocks Room Selector
"""
Goldilocks wants to find the warmest and coolest rooms in her house based on the current temperature readings
She has a list of temperatures for each room and needs a quick way to determine which rooms are the warmest and coldest
    Create a list of temperatures and rooms for each room in the house
    Determine the warmest and coldest temperatures using the max() and min() function
    Identify the rooms with these temperatures and print out the results using string formatting
"""
room_temperatures = [22, 24, 19, 21]
room_names = ["living room", "kitchen", "bedroom", "bathroom"]

warmest_temp = max(room_temperatures)
coolest_temp = min(room_temperatures)

warmest_room_index = room_temperatures.index(warmest_temp)
coolest_room_index = room_temperatures.index(coolest_temp)

warmest_room = room_names[warmest_room_index]
coolest_room = room_names[coolest_room_index]

print(f"The {warmest_room} is the warmest room at {warmest_temp} C")
print(f"The {coolest_room} is the coolest room at {coolest_temp} C")

# 5. The E-Commerce Cart
"""
In an e-commerce application, its important to provide customers with a clear and concise summary of their shopping cart before they proceed to checkout
Your task is to write a script that uses strong concatenation to create a summary of the items in a shopping cart, including product names, prices & stock availability
    Define variables for a few products, their prices and their stock availablity
    Use string concatenation to build a summary of the cart
    Include product names, prices and stock status (In Stock or Out of Stock) in the summary
    Display the cart summary to the user
"""
product_1 = "Wireless Mouse"
product_2 = "Gaming Keyboard"
product_3 = "USB-C Adapter"

price_1 = "$25"
price_2 = "$50"
price_3 = "$10"

in_stock_1 = True
in_stock_2 = False
in_stock_3 = True

cart_summary = "Your Cart Items:\n"
cart_summary += "- " + product_1 + ":" + price_1 + (" (In Stock)") if in_stock_1 else " (Out of Stock)" + "\n"
cart_summary += "- " + product_2 + ":" + price_2 + (" (In Stock)") if in_stock_2 else " (Out of Stock)" + "\n"
cart_summary += "- " + product_3 + ":" + price_3 + (" (In Stock)") if in_stock_3 else " (Out of Stock)" + "\n"

print(cart_summary)

# 6. The Interactive Story Chooser
"""
You are creating an interactive story where the reader can choose their own adventure
At each stage of the story, the reader is presented with a choice that determines the direction of the narrative
Your task is to write a script that guides the reader through the first decision point of the story
    Present the reader with a brief introduction to the story and a choice to make
    Capture the reader's choice by using the input() function
    Depending on the choice, display the outcome of their decision
    Use a list to store possible choices and outcomes
"""
print("You wake up in a mysterious Forest. Two paths lie before you.")

choices = ["left", "right"]
outcomes = ["You encounter a friendly elf who offers you a map.",
            "You stumble upon a sleeping dragon"]

print(f"Do you go left or right?")
decision = input().lower()

if decision not in choices:
    print("Confused, you decide to wait for a clearer sign of which path to take.")
elif decision == 'left':
    outcome_index = choices.index('left')
    print(outcomes[outcome_index])
else:
    outcome_index = choices.index('right')
    print(outcomes[outcome_index])

# 7: The Customized List Printer
"""
You are tasked with creating a program that prints out a shopping list
However, the user wants the list to be printed in a specific format, with customer separators between items and a custom ending to signify the end of the list
    Create a list of shopping items
    Ask the user for their preferred separator (e.g. coma, slash, dash)
    Ask the user for their preferred ending phrase (e.g. End of list, that's all)
    Use a loop to print each item with the user's preferred separator and end the list with their chosen ending
"""
shopping_list = ["apples", "banana", "bread", "milk", "juice"]

seperator = input("Please enter your preferred item seperator (eg., ',', '/', '-'): ")
ending = input("Please enter your preferred ending phrase (e.g., End of List, That's all): ")

print("Your shopping list: ", end="\n\n")
for item in shopping_list:
    if item == shopping_list[-1]:
        print(item)
    else:
        print(item, end=seperator + " ")
print("\n\n" + ending)

# 8: The Dynamic Type Quiz Game
"""
You are tasked with developing a quiz game that challenges players to answer questions that require answers in different data types
The game should prompt the user for an answer, conver the answer to the required type, and verify its correctness
    Create separate lists for questions, correct answers, & the required answer types
    Use a loop to iterate over the questions and present them to the user one by one
    For each question, prompt the user for their answer and convert it to the required type using the corresponding type conversion function
    Compare the user's converted answer to the correct answer and provide immediate feedback
    Keep a count of the number of correct answers and display the user's score at the end of the game
"""
questions = [
    "What is 10 plus 4?",
    "Enter a decimal number between 1 and 2",
    "What is the string representation of the number 20?",
    "Is Python a programming language? (True/False)"
]

correct_answers = [14, 1.5, "20", True]
answer_types = [int, float, str, bool]
score = 0

for i in range(len(questions)):
    user_answer = input(questions[i] + " ")
    try:
        if answer_types[i] == bool:
            converted_answer = user_answer.lower() in ['true', 't', '1', 'yes', 'y']
        else:
            converted_answer = answer_types[i](user_answer)

        if converted_answer == correct_answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Wrong answer")
    except ValueError:
        print("Invalid input type.")

print(f"Your final score is {score}/{len(questions)}.")

# 9: The Type Inspection Challenge
"""
You are creating a program that categorizes elements in a list based on their data type
The program should iterate over a mixed-type list, identify the data type of each element & sort the elements into separate lists according to their type
    Create a mixed-type list with various data types(e.g. integers, floats, strings, booleans)
    Initialize separate listws to hold elements of each data type
    Use a loop to iterate over the mixed-type list
    For each element, use isinstance() or type() to determine the elements type
    Append the element to the corresponding list based on its type
    Use shorthand if statements to streamline the type checking logic
    Print out the categorized lists after processing the entire mixed type list
"""
mixed_lists = [10, 3.14, 'Python', False, 42, 'Code', 2.718, True]

integers = []
floats = []
strings = []
booleans = []

for element in mixed_lists:
    if isinstance(element, int) and not isinstance(element, bool):
        integers.append(element)
    elif isinstance(element, float):
        floats.append(element)
    elif isinstance(element, str):
        strings.append(element)
    elif isinstance(element, bool):
        booleans.append(element)
    else:
        print(f"Unknown type: {type(element)}")

print(f"Integers: {integers}")
print(f"Floats: {floats}")
print(f"Strings: {strings}")
print(f"Booleans: {booleans}")

# 10: The Match Function Marathon
"""
You are working on a data analysis project that required you to process a list of floating-point numbers
Your task is to calculate the sum of all numbers, find the square root of each number, and then round them up or down to the nearest integer
Additionally, you need to identify which numbers are above teha verage after rounding
    Create a list of floating point numbers
    Calculate the sum of the numbers using the sum() function and print the result
    Use a loop to iterate over each number in the list
    Inside the loop, calculate the square root of each number using the sqrt() function & then determine whether to round up or down using ceil() or floor() from the math module
    Use nested if statements to compare each rounded number with the average of the list and print whether it is above or below the average
    Ensure that the output is clean and informative
""" 
import math
numbers = [2.5, 3.6, 4.7, 5.8, 6.9]

total_sum = sum(numbers)
print(f"The sum of the numbers is: {total_sum}")

average = total_sum / len(numbers)

for number in numbers:
    sqrt_number = math.sqrt(number)
    rounded_number = round(sqrt_number)
    if rounded_number < sqrt_number:
        rounded_number = math.ceil(sqrt_number)
    else:
        rounded_number = math.floor(sqrt_number)

    if rounded_number > average:
        print(f"{rounded_number} is above the average")
    else:
        print(f"{rounded_number} is below the average")