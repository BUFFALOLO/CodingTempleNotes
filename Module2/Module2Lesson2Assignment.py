
# 1. THE ADVENTURE GAME
#       Task 1 - Code Correction: # You are provided with a Python script that is supposed to guide a user through an adventure game, but it has some errors. Identify & fix them.
#       Task 2 - Setting the Scene: Based on your corrected code from Task 1, expand the game. If the user chooses "cave", ask them if they want to "light a torch" or "proceed in the dark", and provide outcomes for each decision.
#       Task 3 - Default Path: If the user makes an invalid choice at any point, incorporate a pass statement to handle it. HINT: How can an else statement be of use here?
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")
    into_cave = input("light a torch or proceed in the dark? ")
    if into_cave == "light a torch":
        print("Open the treasure!")
    elif into_cave == "proceed in the dark":
        print("Crawl around to find the treasure")
else:
    pass

# 2. QUICK DECISONS - THE EVENT PLANNER
#       Task 1 - Code Correction: You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.
#       Task 2 - Venue Selection: Based on the corrected code from Task 1, further enhance your code to recommend additional things like "audio system" or "projector" based on the number of attendees.
#       Task 3 - Catering Choices: Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
fun = "audio system" if attendees > 50 else "projector"
print(fun)
food = input("Would you like vegetarian food (yes/no)? ")
if food == "yes":
    print("Veggie Delight Caterers are recommended")
else:
    print("Gourmet Meals Caterers are recommended")