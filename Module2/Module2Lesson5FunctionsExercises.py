# 1: The Smart Home Morning Routine 
"""
You are programming a smart home system to perform a series of actions as part of a morning routine
The system should greet you, inform you of the weather, remind you of your first calendar event & tell you if you have unread emails
    Define a function called morning_routine() that takes no arguments
    Inside the function, print Good Morning to simulate a greeting
    Create a list of weather conditions for the week
    Use a loop to iterate over the weather list & use an if statement to check if the current day's weather is rainy, if it is pring a reminder to take an umbrella
    Create a list of calendar events for the week
    Use a loop to find todays event & print it as a reminder
    Create a variable to store the number of unread emails
    Use an if statement to check if there are any unread emails & print the number if there are
    Call the morning_routine() function to execute the morning routine
HINT: You can use the datetime module to get the current day of the week if you want to match the weather & events to the actual day
"""
import datetime

def morning_routine():
    print("Good Morning!")

    weather_conditions = ['Rainy', 'Cloudy', 'Rainy', 'Sunny', 'Cloudy', 'Windy']

    today_weather = weather_conditions[datetime.datetime.today().weekday()]

    if today_weather == 'Rainy':
        print("Don't forget your umbrella, its rainy today")

    calendar_events = ['Gym', 'Lunch with Bob', 'Dentist Appointment', 'Gym', 'Lunch with Sarah', 'Grocery Shopping']
    today_event = calendar_events[datetime.datetime.today().weekday()]
    print(f"Todays Event: {today_event}.")

    unread_emails = 5
    if unread_emails > 0:
        print(f"You have {unread_emails} unread emails.")

morning_routine()

# 2: The Versatile Coffee Machine
"""
You have a cofee machine that can make various types of coffee. You want to program it to prepare your coffee based on your selection.
    Define a function called make_coffee() that takes on parameter coffee_type with a default value of espresso
    Inside the function, print the message indicating the type of coffee being made
    Create a list of coffee types the machine can make
    Use a loop to iterate over the list of coffee types
    Inside the loop, use an if statement to check if the coffee type is cappucino, if it is, print a special message indicating that its a favorite
    Call the make_coffee() function with different arguments to simulate making different types of coffee
    Ensure that calling make_coffee() without arguments defaults to making an espresso
"""
def make_coffee(coffee_type="espresso"):
    print(f"Making a cup of {coffee_type}!")
    
coffee_types = ['espresso', 'latte', 'cappucino', 'mocha', 'americano', 'decaf']

for type in coffee_types:
    make_coffee(type)
    if type == 'cappucino':
        print("Ah, cappucino, a personal favorite")

make_coffee()

# 3: The Dynamic Playlist DJ 
"""
You are developing a feature for a music app that allows users to create a custom playlist and play the songs in sequence
    Define a function called play_songs() that takes on parameter song_list
    Inside the function, use a loop to iterate over song_list
    For each song in the list, print a message indicating that the song is now playing
    Before calling the functoin, prompt the user to enter the number of songs they want to add to the playlist
    Use a loop and input() to accept song names from the user, based on the number they provided, & store them in a list
    Call the play_songs() function with the user-created list of songs as an argument
"""
def play_songs(song_list):
    for song in song_list:
        print(f"Now playing: {song}")

num_songs = int(input("How many songs would you like to add to the playlist? "))

user_playlist = []
    
for i in range(num_songs):
    song_name = input(f"Enter song {i+1}: ")
    user_playlist.append(song_name)

play_songs(user_playlist)

# 4: The Group Expense Tracker 
"""
You are creating a program to track expenses for a group of friends on a trip
The program will calculate the total expenses and identify the highest spender
    Define a function called track_expenses() that takes a variable number of numerical arguments representing individual expenses
    Inside the function, calculate the sum of the expenses & print the total
    Also, determine the highest expense and print the person associated with it
    Outside the function, use a while loop to prompt each user to enter their expense until they are done
    Use input() to accept the expense amount from each user & store these into a list
    After collecting all expenses, call the track_expenses() function with the list of expenses as arguments using the splat operator (*)
"""
def track_expenses(*expenses):
    total_expenses = sum(expenses)
    print(f"The total expenses are: {total_expenses}")

    highest_expense = max(expenses)
    spender = expenses.index(highest_expense)+1
    print(f"Person {spender} is the highest spender with an expense of {highest_expense}")

group_expenses = []

while True:
    expense_input = input("Enter an expense amount or 'done' to finish: ")

    if expense_input.lower() == 'done':
        break
    else:
        expense = float(expense_input)
        group_expenses.append(expense)

track_expenses(*group_expenses)

# 5: The Product Inventory Manager 
"""
You are developing a feature for an e-commerce app that allows the store manager to view and update the inventory of products
    Define a list called products that contains the initial inventory of product names
    Create a function called manage_inventory() that will display the current inventory, allow the manager to add new products & remove products that are out of stock
    Inside the function, use a loop to display options for the manager: view inventtory, add product, remove product, and exit
    Use list slicing and the len() function to display the first 5 products in the inventory when viewing
    Allow the manager to add a product by entering its name, which will be appended to the product list
    Allow the manager to remove a product by entering its name. Ensure the product exists in the list before attempting to remove it
    Use the input() function to collect the managers choices & product names
"""
products = ['t-shirt', 'jeans', 'jacket', 'sunglasses', 'hat', 'watch']

def manage_inventory():
    while True:
        print("\nInventory Management System")
        print("1. View Inventory")
        print("2. Add Product")
        print("3. Remove Product")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nCurrent Inventory:")
            for product in products[:5]:
                print(product)
            if len(products) > 5:
                print("...and more")
        elif choice == "2":
            new_product = input("Enter the name of the new product: ")
            products.append(new_product)
            print(f"{new_product} has been added to the inventory")
        elif choice == "3":
            product_to_remove = input("Enter the name of the product to remove: ")
            if product_to_remove in products:
                products.remove(product_to_remove)
                print(f"{product_to_remove} has been removed from the inventory")
            else:
                print(f"{product_to_remove} was not found in the inventory")
        elif choice == "4":
            print("Exiting Inventory Management System")
            break
        else:
            print("Invalid choice. Please try again")

manage_inventory()

# 6: The Payment Splitter 
"""
In a group of friends, expenses are often shared
Your task is to create a function that calculates how much each person must pay or be reimbursed after a shared expense
    Define a function called split_payment that takes a list of expenses & the number of friends as arguments
    The function should calculate the total expenses & the individual share
    Return both the total & the indifivudal share from the function
    Outside the function use a loop to allow the user to input th cost of each expense & add it to a list
    After all expenses are entered, call the spli_payment function with the list of expenses & the number of friends
    Display the total expenses & how much each person must pay or be reimbursed
"""
def split_payment(expenses, number_of_friends):
    total_expenses = sum(expenses)
    individual_share = total_expenses / number_of_friends
    return total_expenses, individual_share

expenses = []

number_of_friends = int(input("Enter the number of friends: "))

while True:
    expense = input("Enter an expense of 'done' to finish: ")
    if expense.lower() == 'done':
        break
    expenses.append(float(expense))

total, share = split_payment(expenses, number_of_friends)
print(f"\nTotal expenses: ${total:.2f}")
print(f"Each person must pay: ${share:.2f}")

# 7: The Phonebook Manager 
"""
You need to manage contacts in a phonebook
Your task is to create functions that can add a new contact & display all contacts, ensuring that you correctly handle variable scope
    Define a global list called phonebok to store contacts as separate lists for names and numbers
    Define a function called add_contact that takes a name & number as arguments & adds them to the phonebook list
    Define a function called display_contacts that prints all the contacts in the phonebook
    Use a loop to allow the user to choose between adding a contact or displaying all contacts
    Ensure that the phonebook list is not reinitialized within the funcions, preserving its global scope
"""
phonebook_names = []
phonebook_numbers = []

def add_contact(name, number):
    global phonebook_names
    global phonebook_numbers
    phonebook_names.append(name)
    phonebook_numbers.append(number)

def display_contacts():
    global phonebook_names
    global phonebook_numbers
    for i in range(len(phonebook_names)):
        print(f" Name: {phonebook_names[i]}, Number: {phonebook_numbers[i]}")

while True:
    action = input("Choose an action [A]dd contact, [D]isplay contacts, [Q]uit: ")
    if action == 'A':
        name = input("Enter the contacts name: ")
        number = input("Enter the contacts phone number: ")
        add_contact(name, number)
    elif action == 'B':
        display_contacts()
    elif action == 'Q':
        break
    else:
        print("Invalid action, please choose again")

# 8: The HR Assistant 
"""
You are tasked with managing employee records for a small company
Your job is to create functions that can add new employee details, calculate average age & display all employees
    Define a global list called employees to store employee details, where each employee is represented as a list with elements [name, age, department]
    Define a function called add_employee that takes name, age, and department as arguments and adds them as a list to the employees list
    Define a function called calculate_average_age that computes and returns the average age of all employees
    Define a function called display_employees that prints all the employee details in a formatted manner
    Use a loop to allow the user to choose between adding an employee, calculating the average age, or displaying all employees
    Ensure that the employees list is not reinitialized within the functins, maintaining its global scope
"""
employees = []

def add_employee(name, age, department):
    global employees
    employees.append([name, age, department])

def calculate_average_age():
    global employees
    total_age = sum(employee[1] for employee in employees)
    return total_age / len(employees) if employees else 0

def display_employees():
    global employees
    for employee in employees:
        print(f"Name: {employee[0]}, Age: {employee[1]}, Department: {employee[2]}")

while True:
    action = input("Choose an action [A]dd, [C]alculate average age, [D]isplay employees, [Q]uit: ").upper()
    if action == "A":
        name = input("Enter the employees name: ")
        age = int(input("Enter the employees age: "))
        department = input("Enter the employees department: ")
        add_employee(name, age, department)
    elif action == "C":
        average_age = calculate_average_age()
        print(f"The average age of employees is: {average_age:.2f}")
    elif action == "D":
        display_employees()
    elif action == "Q":
        break
    else:
        print("Invalid action. Please try again")