# 1. For Loop Festival Planner: Utilize for loops to iterate over multiple lists & organize event details without using functions.
"""
Use a for loop to iterate over the booth types.
For each booth type, print the type of booth, the schedule time, and the item needed.
Ensure that each booth type is matched with the correct schedule time & item needed from the lists provided.
"""
booth_type = ["Food", "Games", "Music", "Crafts"]
schedule_times = ["10:00 AM", "1:00 PM", "3:00 PM", "5:00 PM"]
items_needed = ["Grill", "Tickets", "Instruments", "Paint"]

for i in range(len(booth_type)):
    booth = booth_type[i]
    time = schedule_times[i]
    item = items_needed[i]
    print(f"{booth} Booth - Schedule: {time}, Item Needed: {item}")

# 2. Classroom Seat Assignment: Use for loops with the range function to assign seats in a classroom setting.
"""
30 students & 5 rows in the classroom
Each row can seat an equal number of students
Use a for loop with the range function to assign & print a seat number for each student
Seat numbres should start at 1 & increase sequentially
"""
total_students = 30
rows = 5

students_per_row = total_students // rows
for row in range(1, rows + 1):
    for seat in range(1, students_per_row + 1):
        seat_number = (row-1) * students_per_row + seat
        print(f"Row {row} - Seat {seat}: Student {seat_number}")

# 3. Shopping Cart Total Calculation: Apply for loops to calculate the total cost of items in a shopping cart.
"""
List of item prices
Use a for loop to iterate through the list of prices
Calculate the total cost by adding up the prices of all the items
Print the total cost at the end
"""
item_prices = [2.99, 5.49, 3.25, 13.99, 4.75]

total_cost = 0

for price in item_prices:
    total_cost += price

print(f"The total cost of the shopping cart is: ${total_cost:.2f}")

# 4. Multiplication Table Generator: Apply nested for loops to generate a multiplication table.
"""
Ask the user for the size of the multiplication table they wish to generate
Use nested for loops to claculate the product of each pair of numbers
Display the multiplication table in a formatted manner
"""
table_size = int(input("Enter the size of the multiplication table: "))

for row in range(1, table_size + 1):
    for col in range(1, table_size, + 1):
        product = row * col
        print(f"{product} \t", end="")
    print()

# 5. Inventory Management: Use lists, for loops, and if statements to manage inventory items.
"""
Create a list of items in the inventory with their current quantities
Use a for loop to iterate over each item
Use an if statement to check if the quantity of an item is below the reorder threshold
Print out the names of the items that need to be reordered
"""
inventory = [
    ["Apples", 5],
    ["Bananas", 2],
    ["Oranges", 0],
    ["Milk", 1],
    ["Eggs", 12] 
]

reorder_threshold = 3

for item in inventory:
    name, quantity = item
    if quantity < reorder_threshold:
        print(f"{name} needs to be reordered")

# 6. Treasure Hunt: Use lists, for loops, and the break statement to stop a process once a certain condition is met.
caves = [False, False, True, False, False]

for index, cave in enumerate(caves):
    # Check if the cave has the treasure
    if cave:
        print(f"Treasure found in cave {index + 1}!")
        break
    else:
        print("The treasure was not in this cave")

# 7. Email Cleanup: Use lists, for loops, and the continue statement to skip over certain iterations within a loop.
emails = ["user1@exmaple.com", None, "user2@example.com", "user3@example.com", None]

valid_emails = []

for email in emails:
    print("Checking emails")
    if email is None:
        print(f"email {email} is not valid")
        continue
    input()
    print("Adding to valid_emails list....")
    valid_emails.append(email)

print(valid_emails)

# 1: The Countdown Timer
"""
You are programming a countdown timer for a game that starts from a specific number & it counts down to 0. 
You need to display each number as the timer counts down.
    Initialize a variable with the starting number of the countdown
    Use a while loop to keep the countdown going as long as the timer is greater than zero
    Inside the loop, decrease the timer by 1 & then print the current value of the timer
    Once the countdown reaches 0, print a message indicating that the time is up

HINT: Remember to decrement the timer variable inside the loop to avoid creating an infinite loop.
"""
timer = 10

while timer > 0:
    print(timer)
    timer -= 1 #timer = 10 - 9 --> timer = 9, repeat until it hits 0

print("Time is up!")

# 2: The Patient Queue
"""
You are developing a system for a clinic's receptionist desk that tracks the number of patients waiting & calls them 1 by 1 until no one is left in the queue.
    Initialize a variable with the total number of patients in the queue
    Use a while loop to simulate calling each patient until the queue is empty
    Inside the loop, decremenet the number of patients as each 1 is called
    Print a message each time a patient is called & when the queue is empty
HINT: Make sure to decrease the number of patients in the queue to reflect that a patient has been called
"""
patients = 5

while patients > 0:
    print(f"Patient number {patients} please come in.")
    patients -= 1 

print("There are no more patients in the queue.")

# 3: The Battery Charger w/ Efficiency Check
"""
You are programming a smart battery charger that not only charges a battery but also performs efficiency checks at certain milestones
The battery starts at 0% & charges in increments. If the battery reaches 50% efficiency, it charges faster. If it reaches 80%, it slows down to prevent overcharging
    Initialize a variable to represent the battery charge level
    Use a while loop to charge the battery in increments
    Inside the loop, us if statements to check the charge level
    If the charge level is 50%, increase the charging increments
    If the charge level is 80%, decrease the charging increments
    Print the battery level at each increment & a message when the battery if fully charged

HINT: You will need to adjust the increment value within the while loop based on the charge level
"""
battery = 0
increment = 10

while battery < 100:
    battery += increment
    print(f"Battery is now at {battery}%")

    if battery == 50:
        print("Efficiency check: Increasing charge rate.")
        increment = 15
    elif battery == 80:
        print("Efficiency check: Reducing charge rate to prevent overcharging.")
        increment = 5

print("The battery is now fully charged.")

# 4: The Smart Coffee Machine
"""
You are programming a smart coffee machine that dispenses different types of coffeee until the resevoir is empty
The machine has a list of coffee types it can dispense, and it should offer each type in order until it runs out of water.
    Initialize a variable to represent the coffee resevoir level    
    Create a list of coffee types that the machine can dispense
    Use a while loop to dispense cofee until the resevoir is empty
    Inside the loop, use an if statement to check if there are still coffee types available
    Dispense each type of coffee and then remove it from the list
    Print the type of coffee dispensed & the remaining coffee types in the list
    Print a message when the coffee resevoir is empty

HINT: You will need to use list methods to remove coffee types once they are dispensed
"""
coffee_resevoir = 10
coffee_types = ["Espresso", "Cappucino", "Latte", "Americano", "Mocha"]

while coffee_resevoir > 0:
    if coffee_types:
        current_coffee = coffee_types.pop(0)
        print(f"Dispensing {current_coffee}")

        coffee_resevoir -= 1
        print(f"Coffee types left: {coffee_types}")
    else:
        print("No more coffee types available")
        break

print("The coffee resevoir is empty")

# 5: The Intelligent Elevator System
"""
You are designing an intelligent elevator system. The elevator has a list of floors where passengers have requested stops.
Write a while loop that starts from the top floor & stops at each requested floor until it reaches the ground level.
    Initialize a variable for the starting floor
    Create a list of floors where passengers have requested stops
    Use a while loop to move the elevator down floor by floor
    Inside the loop, use the membership operator to check if the current floor is in the list of requested stops
    If the current floor is a requested stop, print a message & remove that floor from the list
    Continue moving down until the ground floor is reached
    Print a message each time the elevator moves down a floor & when it reaches the ground floor

HINT: You will need to use list methods to remove floors from the list once they are visited
"""
current_floor = 5
requested_stops = [1, 3, 4]

while current_floor >0:
    if current_floor in requested_stops:
        print(f"Stopping at floor {current_floor}")
        requested_stops.remove(current_floor)
    
    current_floor -= 1
    print(f"Descending to floor {current_floor}.")

# 6: The Smart Traffic Light
"""
Create a list of colors representing the traffic light sequence
Initialize a counter for the green light
Use an infinite while loop to cycle through the traffic light colors
Inside the loop, use the count method to track the number of times green appears
Break the loop when the green light has appeared a specific number of times
Print a message each time the light changes & when the loop breaks for maintenance
"""
traffic_lights = ["red", "yellow", "green", "yellow"]
green_count = 0

while True:
    for color in traffic_lights:
        print(f"The traffic light is now {color}")
        if color == "green":
            green_count += 1
            if green_count == 3:
                print("Maintenance time! The cycle will stop")
                break
    
    if green_count == 3:
        break

# 7: The Skipping Rope Challenge
"""
Initialize a countdown variable with the starting number
Create an empty list to store the numbers you land on
Write a while loop that counts down from the starting number
Use a continue statement to skip every other number
Append the numbers you land on to the list
Use list slicing to display the final list of numbers
"""
count = 10
landed_numbers = []

while count > 0:
    count -= 1
    if count %2 == 1:
        continue
    landed_numbers.append(count)

print("Numbers landed on: ", landed_numbers[::-1])

# 1: Lucky Draw
"""
Import the random module to use its choice selection capabilities
Create a list of participant names, including "Alex"
Use a while loop to repeatedly draw a name randomly from the list of participants
The loop should only terminate when "Alex" is drawn
Ensure that the loop does not produce any output until "Alex" is drawn
"""
import random

participants = ["John", "Lila", "Sarah", "Alex", "Max"]

while 'Alex' not in random.choices(participants, k=1):
    pass

print("Congratulations, Alex! You've won the lucky draw!")

# 2: Random Walk
"""
Import the random module to utilize its random selection feature
Define a list of directions that the entity can take
Use a for loop to simulate 10 steps
In each iteration, randomly select a direction & simulate taking a step in that direction
Print out the direction of each step
"""
import random

directions = ["North", "South", "East", "West"]

for step in range(10):
    step_direction = random.choice(directions)
    print(f"Step {step + 1}: The entity moves 10 steps to the {step_direction}")

# 3: Dice Roll Synchronicity
"""
Import the random module to generate random dice rolls
Use a while loop to keep rolling the dice until the same numbers appears on both
In each iteration, simulate rolling 2 dice
Check if the 2 dice have the same number. If they do, exit the loop
Print out the result of each roll & a message when both dice match
"""
import random

while True:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f"Dice 1: {dice1}, Dice 2: {dice2}")
    if dice1 == dice2:
        print(f"Both dice landed on {dice1}")
        break

# 4: Quick Master Shuffle
"""
Import the random module to shuffle the list of questions
Use the random.shuffle() method to randomize the order of the quiz questions
Use a for loop to iterate through the shuffled list & present each question
Print out each question to the user
"""
import random

questions = ["What is the capital of France?", "What is 2+2?", "Who wrote Macbeth?", "What is the boiling point of water?", "Whos it the best NFL team?"]

random.shuffle(questions)

for question in questions:
    print(question)

# 5: Classroom Role Call
"""
Import the random module to use the sampling function
Use the random.sample() method to randomly select 5 names from the list of students
Print out the names of the selected students as part of the attendance checks
"""
import random
students = ["Alice", "Bob", "Charlie", "Diane", "Ethan", "Fiona", "George"]

selected_students = random.sample(students, 5)

for student in selected_students:
    print(f"Is {student} present")

# 6: Secure Password Creation
"""
Import the random & string modules
Combine uppercase letters, lowercase letters, digits, & puncuation to create a pool of characters
Use a loop to randomly select 8 characters from the pool to form a password
Print out the generated password
"""
import random
import string

characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(characters) for _ in range(8))

print(f"Generated Password: {password}")

# 7: Dynamic Color Generation
"""
Import the random module
Create a loop that will run a specified number of times to generate random color values
In each iteration, generate 3 seperate numbers ranging from 0 to 255, representing the Red, Green & Blue (RGB) components of a color
Print out the generated EGB color value in readable format
"""
import random
num_colors = 10

for _ in range(num_colors):
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    print(f"Generated RGB Color: ({red} {green} {blue})")

# 1: Honoring the High Achievers
"""
Create a list of student names
Use slicing to select the top three students
Use a for loop to iterate through the sliced list
Print each name with a congratultory message
"""
students = ["Alice", "Bob", "Charlie", "David", "Eve"]
top_students = students[:3]

for student in top_students:
    print(f"Congratulations, {student}! You are among the top performers!")

# 2: Diverse Inventory Check
"""
Loop through the inventory list using a while loop & index numbers
Use if statements to check the data type of each item
Print a message for each item, depending on its data type
"""
inventory = ["Apples", 120, "Orange", 80, True, "Bananas", 150, False]
index = 0

while index <len(inventory):
    item = inventory[index]

    if type(item) == str:
        print(f"Item: {item}")
    elif type(item) == int:
        print(f"Quantity: {item}")
    elif type(item) == bool:
        status = "on sale" if item else "not on sale"
        print(f"Sale status: {status}")

    index += 1

# 3: Square Numbers Showcase
"""
Use list comprehension to generate the squares of numbers from 1 to 10
Each element in the new list should be the square of an integer from the original range
"""
squares = [number**2 for number in range (1,11)]
print(squares)

# 4: Even Num
"""
Start with a list of numbers from 1 to 20
Use list comprehension to filter out the even numbers
Remember that an even number is divisible by 2 with no remainder
"""
numbers = list(range(1, 21))
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

# 5: Ingredient Preparation
"""
Begin with a full list of ingredients
Use slicing to select the first half of the list
The length of the list can be found using the len() function & you can divite it by 2 to find the midpoint
"""
ingredients = ["salt", "pepper", "paprika", "garlic", "onion", "beef", "tomato", "basil"]

needed_ingredients = ingredients[:len(ingredients)//2]
print(needed_ingredients)

# 6: Editorial Review
"""
Start with the full list of article titles
Use slicing with negative indices to select the last 3 titles in reverse order
Remember that in Python, negative indices count from the end of the list
"""
articles = ["Article1", "Article2", "Article3", "Article4", "Article5"]

recent_articles = articles[-1:-4:-1]
print(recent_articles)

# 7: Scoring System Design
"""
Use a list comprehension to iterate through numbers 1 to 30
Include a condition within the list comprehension to select only the multiple of 3
Store the resuling list in a variable
"""
multiples_of_three = [number for number in range(1, 31) if number % 3 ==0]
print(multiples_of_three)