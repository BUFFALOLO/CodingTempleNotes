flavors = ["vanilla", "chocolate", "blueberry", "mango", "salted caramel"]
for flavor in flavors:
    print("Mmm,,,I just sampled" + flavor + "!")

"""
for: marks the start of the loop in your code.
flavor: This is a variable that takes the value of each item in the iterable (in this case, each ice cream flavor). You can name this variable anything you like.
in: This keyword is used to iterate over the list of flavors.
flavors: is our list of ice cream flavors in this example. In technical terms, it's what we call an iterable object - a collection of items we can loop through.
Colon (:): Indicated the end of the for loop header & the start of the loop body
Indentation: The indented line, print(“Mmm…I just sampled” + flavor + “!”), 
is like expressing your enjoyment after tasting each flavor. In Python, the indentation defined the scope of the loop. 
Every line that's indented under the for statement is part of the loop’s body & will be executed in each iteration.

Each iteration of the loop takes the next flavor in the list flavors, assigns it to the variable flavor, & executes the indented code block 
(printing your enjoyment of the flavor). Once all flavors are “tasted”, the loop ends. 
"""

"""
range() function helps you to:
    Generate a sequence of numbers.
    Specify the start, stop & even the step size.
    Control your loops "tasting" sequence
"""

for i in range(3):
    print ("Trying out flavor number " + str(i+1) + ": " + flavors[i])

# Nested loops are fantastic for creating combinations or working with multi-layered data.
flavors = ["vanilla", "chocolate", "blueberry", "mango", "salted caramel"]
toppings = ["spinkles", "chocolate", "whipped cream", "cherry"]

for flavor in flavors:
    for topping in toppings:
        print("Let's try a scoop of " + flavor + " with some " + topping + "on top! ")

# Sometimes, you need to tweak your tasting journey. That’s where break, continue, and pass come into play. They’re like special moves in your coding game.

ice_cream_flavors = ["chocolate", "vanilla", "cookie dough", "strawberry"]

for flavor in ice_cream_flavors:
    if flavor == "cookie dough":
        print("My favorite! No need to taste further")
        break
    print("Trying " + flavor + " flavor.")

ice_cream_flavor = ["chocolate", "vanilla", "cookie dough", "strawberry"]

for flavor in ice_cream_flavor:
    if flavor == "strawberry":
        continue
    print("Enjoying a scoop of " + flavor + "!")

ice_cream_flavors2 = ["chocolate", "vanilla", "cookie dough", "strawberry", "rocky road"]

for flavor in ice_cream_flavors2:
    if flavor == "rocky road":
        pass
    print("Sampling " + flavor + " now")

marshmallows = 0
while marshmallows < 5:
    marshmallows += 1
    print("Added a marshmallow! Not there are " + str(marshmallows) + " marshmallows!")

"""
Where you place the increment (marshmallows += 1) in your loop can really change the flavor of your code
	At the beginning: it instantly updates, ensuring your loop mirrors the current state with each marshmallow addition.
	At the end: It delays updates, useful but can be tricky, possibly causing off-by-one errors.
marshmallows = 0
while marshmallows < 5:
    print("Added a marshmallow! Not there are " + str(marshmallows) + " marshmallows!")
        marshmallows += 1    
"""

# Non-starters & infinite refills
# The Non-Started Loop: if your while loop condition is never initially true, its an unused path

# Initialize a varible
temperature = 100

# Set up a while loop with a condition that is never true
while temperature < 0:
    # This block of code will not execute because the initial temperature is 100, which is not less than 0
    temperature -= 1
    print("The temperature is now: ", temperature)

# Since the loop body never executes, this print statement will run immediately
print("The temperature was never below 0 to begin with")

# The Infinite Loop: While it has its perks, without a "stop" signal (like a break statement), it can result in a program that won't quit
while True:
    user_input = input("Say stop to end the refill: ")
    if user_input.lower() == "stop":
        break
    else:
        print("Here's more coffee!")

import random

for _ in range(10):
    dice_roll = random.randint(1, 6)
    print("You rolled a " + str(dice_roll) + "!")

playlist = ["song1", "song2", "song3", "song4", "song5"]
random.shuffle(playlist)

for song in playlist:
    print(song)

snacks = ["apple", "banana", "carrot stick", "doughnut", "chocolate bar"]
picked_snack = ''

while picked_snack != "chocolate bar":
    picked_snack = random.choice(snacks)
    print("You got a " + picked_snack + ".")
    if picked_snack != "chocolate bar":
        print("Let's pick again!")
    else:
        print("Yay! chocolate bar wins!")

