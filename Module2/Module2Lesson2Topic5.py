temperature = 20
if temperature < 25:
    print("It's a bit chilly!")
    if temperature < 15:
        print("Actually, you might need a coat!")

# EXAMPLE 1
age = 17
if age >= 18:
    if age >= 21:
        print("You can dive, vote and also drink!")
    else: print("You can drive & vote!")
else:
    print("You're too young to drive or vote!")

# EXAMPLE 2
day = "Saturday"
time = "Morning"

if day == "Saturday":
    if time == "Morning":
        print("Time for cartoons")
    elif time == "Evening":
        print("Maybe a movie night?")
    else:
        print("Relax and enjoy your day! ")

# EXAMPLE 3
genre = "Fantasy"
author = "J.K. Rowling"
if genre == "Fantasy":
    if author == "J.K. Rowling":
        print("Ah, an adventure at Hogwarts!")
    elif author == "R.R. Tokien":
        print("Time to visit Middle-Earth!")
    else:
         print("Fantasy is a journey to another world!")

# EXAMPLE 4
fruit = "Apple"
is_ripe = True
has_spots = False

if fruit == "Apple":
    if is_ripe and not has_spots:
        print("Perfect for a juicy bite")
    elif not is_ripe and not has_spots:
        print("Let it ripen a bit more")
    else:
        print("Might be best for applie pie")
elif fruit == "Banana":
    if is_ripe and not has_spots:
        print("Ready to eat")
    elif not is_ripe:
        print("Still a bit green")
    else:
        print("Perfect for banana bread")
else:
    print("Not sure about this fruit's ripeness")

# EXAMPLE 5
movie = "Inception"
release_year = 2010
duration_minutes = 148

if movie == "Inception":
    if 2000 <= release_year <= 2020 and duration_minutes > 120:
        print("A moden classic with a runtime of over 2 hours!")
    elif release_year < 2000:
        print("A gemt from the past")
    else:
        print("A recent masterpiece")
elif movie == "Titantic":
    if release_year == 1997 and duration_minutes > 100:
        print("A romantic epic that spans over 3 hours")
    else:
        print("A timeless lovestory")
else:
    print("Enjoy the movie!")

# EXAMPLE 6
product = "Kindle Paperwhite"
average_rating = 4.7 # This is a float
number_of_reviews = 25000

if product == "Kindle Paperwhite":
    if average_rating >= 4.5 and number_of_reviews > 10000:
        print("A highly recommended product with numerous positive reviews")
    elif average_rating >= 4.0 and number_of_reviews > 5000:
        print("A well-received product with a good number of reviews")
    elif average_rating < 4.0:
        print("The product has mixed reviews. Consider reading detailed reviews before purchasing")
    else:
        print("The product has a high rating but lacks a significant number of reviews.")

elif product == "Amazon Echo":
    if average_rating >= 4.5 and number_of_reviews > 10000:
        print("A top-rated smart speaker with a vast number positive reviews")
    elif average_rating >= 4.0 and number_of_reviews > 5000:
        print("A popular smart device with many satisfied customers")
    elif average_rating < 4.0:
        print("The smart-speaker has varied reviews. It might be worth checking other models")
    else:
        print("The Echo has a commendable rating, but more reviews would provide better clarity")

elif product == "Amazon Fire Stick":
    if average_rating >= 4.5 and number_of_reviews > 10000:
        print("A must have for streaming enthusiasts with overwhelming positive feedback")
    elif average_rating >= 4.0 and number_of_reviews > 5000:
        print("A favorite among many for streaming, with a good number of reviews")
    elif average_rating < 4.0:
        print("The First Stick has mixed feedback. Consider other streaming options or newer models")
    else:
        print("The Fire Stick seems promising, but more reviews could offer a clearer picture")

else:
    print("Please check the product's detailes reviews and ratings. ")