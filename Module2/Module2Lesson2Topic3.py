# EXAMPLE 1
is_raining = True
is_cold = False

if is_raining and is_cold:
    print("Wear a waterproof jacket & a scarf!")
elif is_raining:
    print("Don't forget your umbrella")
else:
    print("Looks like a clear day, dress as you wish!")

# EXAMPLE 2
income = 5000 #monthly income
expenses = 4500 # monthly expenses

savings = income - expenses

if savings > 1000:
    print("Great job! You saved a lot this month!")
elif savings <= 0:
    print("Looks like you've spent all or more that you earned!")
else:
    print("Every little bit counts! Keep saving!")

# EXAMPLE 3
is_student = True
is_senior = False

if is_student:
    print("You get a 50% student discount")
elif is_senior:
    print("Seniors enjoy a 40% discount!")
else:
    print("Regular entry fee applies")

# EXAMPLE 4
is_sunny = True
have_money = False

if is_sunny and have_money:
    print("Great day for a walk in the park!")
else:
    print("Maybe consider indoor activites or saving for a sunny day outing!")

# EXAMPLE 5
is_friendly = False
has_quest = True

if not is_friendly:
    print("Be cautious! This character might not be helpful!")
elif has_quest:
    print("This character has a quest for you!")
else:
    print("Just a regular villager passing by.")

# EXAMPLE 6
wants_veggies = True
likes_spice = False

if wants_veggies and likes_spice:
    print("How about a spicy veggie wrap?")
elif wants_veggies:
    print("Try our classic veggie burger!")
else:
    print("Check out our grill menu!")

