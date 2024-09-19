# Exercise 1: Traffic Light Simulator
# Write a program that prompts the user to input the color of a traffic light (red, yellow, green) & outputs the action a driver should take
light_color = input("What color is the traffic light? ")

if light_color == "red":
    print("STOP! DO NOT GO!")
elif light_color == "yellow":
    print("SLOW DOWN! The light will be turning red! SLOW DOWN!")
elif light_color == "green":
    print("Keep on rolling, rolling, rolling!")
else:
    print("Please enter red, yellow or green!")

# Exercise 2: Movie Age Restriction
# Given a movie's rating (G, PG, PG-13, R) and the age of the person, inform the user if the can watch the movie based on their age.
persons_age = int(input("Enter your age: "))
rating = input("Enter the movie rating (G, PG, PG-13, R): ")

if rating == "G":
    print("You can watch the movie!")
elif rating == "PG" and persons_age >= 7:
    print("You can watch the movie!")
elif rating == "PG-13" and persons_age >= 13:
    print("You can watch the movie!")
elif rating == "R" and persons_age >= 17:
    print("You can watch the movie!")
else:
    print("You cannot watch the movie")

# Exercise 3: Weather Suggestion
# Based on the temperature entered by the user, suggest an outfit to wear. Be creative!
temperature = float(input("Enter the current temperature: "))

if temperature >= 20:
    print("It is VERY cold, bundle up!!")
elif 20 <= temperature <50:
    print("It is a little chilly. Make sure to wear a light coat")
elif 51 <= temperature <= 70:
    print("It might be good to wear a t-shirt & some long pants")
else:
    print("It feels great! This is T-Shirt weather!")

# Exercise 4: Grading System
# Convert numeric grades to letter grades. Assume grades are between 0-100 (Research academic grades values)
grade = float(input("Enter your grade (0-100): "))

if grade >= 90:
    print("Your letter grade is A.")
elif grade >= 80:
    print("Your letter grade is B.")
elif grade >= 70:
    print("Your letter grade is C.")
elif grade >= 60:
    print("Your letter grade is D.")
else:
    print("Your letter grade is F.")

# Exercise 5: Fitness Advice
# Ask the user how many minutes they exercise daily & provide health advice
exercise = int(input("How many minutes have you exercised? "))

if exercise < 30:
    print("You should consider exercising more for better health.")
elif 30 <= exercise <= 60:
    print("Great job! Keep up the good work")
else:
    print("You are a exercise superstar!")

# Exercise 6: Coffee Recommendation
# Recommend a type of coffee based on user preferences about sweetness and milk
likes_sweet = input("Do you like your coffee sweet (yes/no)? ")
likes_milk = input("Do you prefer milk in your coffee (yes/no)? ")

if likes_sweet == "yes" and likes_milk == "yes":
    print("How about a pumpkin spice latte?")
elif likes_sweet == "no" and likes_milk == "yes":
    print("An Americano with a dash of milk sounds good for you")
elif likes_sweet == "yes" and likes_milk == "no":
    print("Try a cold brew with two sugars")
else:
    print("Black coffee it is!")

# Exercise 7: Library Book Return
# Create a program for a library to calculate fines for overdue books. The library has the following fine structure:
# $1 per day for books that are up to 5 days overdue
# $2 per day for books that are 6 - 10 days overdue
# $5 per day for books that are 10 plus days overdue
# 1. Ask the user for the number of days a book is overdue
# 2. Calculates the fine based on the above criteria
# 3. Displays the fine amount to the user
# HINT: Use nested if-elif-else statements to determine the fine amount based on the number of days the book is overdue

days_late = int(input("How many days is the book overdue? "))
fine = 0

if days_late <= 5:
    fine = days_late * 1
elif days_late <=10:
    fine = days_late * 2
else:
    fine = days_late * 5

print(f"Your fine is ${fine}.")
