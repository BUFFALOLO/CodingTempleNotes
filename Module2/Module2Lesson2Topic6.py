x, y = 5, 10
print("x is greater") if x > y else print("y is greater")

# EXAMPLE 1
weather = "sunny"
activity = "beach" if weather == "sunny" else "indoor games"
print(activity)

# EXAMPLE 2
hour_of_day = 7 # Using an integer to represent the hour in 24-hour formant
energy_level = 3 # Using an integer on a scale of 1 to 5, where 5 is very energetic

beverage = "coffee" if (6 <= hour_of_day < 12) and energy_level <4 else "tea"
print(beverage)

# EXAMPLE 3
exercise_energy_level = 4.5 # Using a float on a scale of 1.0 to 5.0, where 5.0 is very entergetic
time_available = 30.5 # Using a float to represent minutes available for workout
short_on_time = time_available < 45.0

workout = "intense cardio" if energy_level > 4.0 and not short_on_time else "light yoga"
print(workout)

# EXAMPLE 4
current_hour = 15 # Using an integer to represent the hour in 24-hour format
hunger_level = 7 # Using an integer on a scale of 1 to 10, where 10 is extremely hungry

meal = "snack" if current_hour < 17 and hunger_level <5 else "full meal"
print(meal)

# EXAMPLE 5
loves_beach = True
budget = 1500 # Initial budget in dollars
high_budget = budget >= 2000

destination = "beach resort" if loves_beach and not high_budget else "luxury mountain resort" 
budget -= 500 if destination == "beach resort" else 1000

print(destination)
print("Remaining budget:", budget)

# EXAMPLE 6
topic_difficulty = "hard"
available_hours = 3.5 
understanding_level = 6

study_method = "deep dive" if topic_difficulty == "hard" and available_hours > 2.5 else "quick review"
bonus_hours = 1.5 if understanding_level < 5 else 0.5
available_hours += bonus_hours

print(study_method)
print("Total study hours:", available_hours)
