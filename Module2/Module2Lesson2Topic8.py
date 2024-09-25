"""
You are developing a feature for a movie streaming platform that suggests a movie genre to users based on their current mood & that days weather.
The platform has the following recommendation:
    If the use is feeling "happy" and the weather is "sunny", recommend a "Comedy".
    If the user is feeling "happy" but the weather is not "sunny", recommend a "Romantic" movie.
    If the user is feeling "sad", recommend a "Drama".
    For any other mood, recommend an "Adventure" movie.

Write a Python program that:
    1. Asks the user about their current mood (happy/sad)
    2. Asks the user about the days weather (sunny/rainy)
    3. Determines the movie genre based on the above criteria
    4. Displays the recommended movie genre to the user
"""

mood = input("What is your mood today? ")
weather = (input("What is the temperature today (sunny/rainy) ? "))

if mood == "happy":
    if weather == "sunny":
        print("Comedy")
    else:
        print("Romantic")
elif mood == "sad":
    print("Drama")
else:
    print("Adventure")

"""
You are programming a smart wardrobe assistant that suggests outfits to users based on the day's temperature and the type of event they are attending.
The platform has the following recommendation:
    If the temperature is below 59 degrees fahrenheit and the event is "formal", suggest a "warm formal suit".
    If the temperature is below 59 degrees fahrenheit but the event is "casual", suggest a "cozy sweater & jeans".
    If the temperature is above 59 degrres fahrenheit and the event is "formal", suggest a "light formal suit".
    For any other combination, suggest a "tshirt & shorts".

Write a Python program that:
    1. Asks the user about the day's temperature in fahrenheit.
    2. Asks the user about the type of event they are attending (formal/casual)
    3. Determines the outfit based on the above criteria.
    4. Displays the recommended outfit to the user.

HINT: Use nested if statement to determine the outfit based on the day's temperature and the type of event.
"""

temperature = float(input("What is the temperature today (in fahrenheit)? "))
event_type = input("What type of event are you attending (formal / casual)? ")

if temperature < 59:
    if event_type == "formal":
        print("Wear a warm formal suit")
    else:
        print("Wear a cozy sweater & jeans")
elif temperature >= 59:
    if event_type == "formal":
        print("Wear a light formal suit")
    else:
        print("Wear a tshirt & shorts")

"""
A school offers various discounts to its students based on their academic performance & participation in extracurricular activites.
The discount criteria are as follows:
    Students with a grade of "A" & who are also part of the school's sports team gets a 20% discount
    Students with a grade of "A" but not on the sports team get a 10% discount
    Students with a grade of "B" and who are part of the school's drama club get a 15% discount

Write a Python program that:
    Asks the user for their grade (A/B/C)
    Asks if they are part of the sports team (yes/no)
    Asks if they are part of the drama club (yes/no)
    Determines the discount percentage based on the above criteria
    Displays the discount percentage to the user

HINT: Use nested if statements to determine the discount percentage based on the student's grade & activities
"""

grade = input("What is your grade (A/B/C)? ")
sports = input("Are you part of the sports team (yes/no)? ")
drama = input("Are you part of the drama club (yes/no)? ")

if grade == "A":
    if sports == "yes":
        print("You get a 20 percent discount")
    else:
        print("You get a 10 percent discount")
elif grade == "B":
    if drama == "yes":
        print("You get a 15 percent discount")
    else:
        print("No discount for you")
else:
    print("No discount for you")

"""
The portal has games that are only suitable for players aged 18 & above. You need to ensure that players meet the age requirements before they can access games
Requirements:
    If the player's age is 18 or above, display "You can drive!"
    If the player's age is below 18 display "Not yet!"

Write a Python program that:
    Asks users for their age
    Determines if the user is old enough to access the games based on the above criteria
    Displays the appropriate message to the user

HINT: Use nested if statements to determine the message based on the user's age
"""

age = int(input("What is your age? "))

if age >= 18:
    print("You can drive!")
elif age < 18:
    print("Not yet!")
else:
    print("But what is your age?!")

"""
The cafe wants to suggest dishes based on whether a customer prefers vegetarian or non-vegetarian meals & whether they want a sugar-free option
The menu has the following critera:
    If the customer prefers a vegetarian mean and wants it sugar free, suggest "Fruit Salad"
    If the customer prefers a vegetarian meal but doesn't want it sugar free, suggest "Veg Cake"
    If the customer prefers a non-vegetarian meal & wants it sugar free, suggest "Sugar free ice cream"
    Any other combination, suggest "chocolate brownie"

Write a Python program that:
    Asks the user about their meal type preference (veg/non-veg)
    Asks the user about their dietary preference (sugar-free/regular)
    Determines the dish based on the above criteria
    Displays the recommended dish to the user
"""






