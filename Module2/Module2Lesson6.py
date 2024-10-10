# PYTHON STRINGS

# Here's our original string:
original_string = "Python"

# Now, suppose we want to change the second letter to i to spell Pithon
# If we try to change it directly like this:
# original_string[1] = 'i' (This would raise an error: TypeError)

# Instead, we start a new string
new_string = original_string[0] + 'i' + original_string[2:]

# Now, new_string holds the value Pithon, but original_string is still Python
print(original_string)
print(new_string)

# Indexing & accessing characters
team = "Coders"

# Indexing starts with 0, so to access the first character C:
first_letter = team[0]

# To get the letter d which is the third character, we use index 2:
third_letter = team[2]

print(first_letter)
print(third_letter)

# To get the last character s, we use negative indexing:
last_letter = team[-1]

# And if we want the second to last letter, character r:
second_last_letter = team[-2]

print(last_letter)
print(second_last_letter)

# ITERATING

track = "Marathon"

for char in track:
    print(char)

for char in track:
    print(char, end=' ') # This will print each character followed by a space

# ITERATING / SLICING

field = "Touchdown"

# We want to slice out Touch:
play_one = field[0:5] # It starts at 0 & stops at 5

# We want slice out down, starting from the 5th index to the end:
play_two = field[5:]

# What if we want to start from the third character and get every second character?
play_three = field[2::2]

print("\n") 
print(play_one)
print(play_two)
print(play_three)

game_plan = "Execute play number 9"
# Let's focus on play number 9 and iterate over just that part:
for word in game_plan[8:]:
    print(word, end=' ') # we will print out each character in the slice

# STRING CONCATENATION
# Our strings are the players:
quaterback = "Tom "
receiver = "Jerry"
play = "runs a route to catch the pass from "

# Lets connect the play:
complete_play = quaterback + play + receiver

print("\n") 
print(complete_play)

# STRING FORMATTING
celebration = "{} scores a touchdown and does the {} dance!"

touchdown_celebration = celebration.format("Tom", "moonwalk")

print(touchdown_celebration)

player = "Tom"
action = "touchdown"
celebration_move = "moonwalk"

play_call = f"{player} scored a {action} and does the {celebration_move}"
print(play_call)

# len(): It helps us to quickly ascertain the length of our string, telling us exactly how many characters we’re working with.
# ** LEN DOES NOT START AT 0, IT STARTS AT 1!
field_length = "Football Field"
field_size = len(field_length)
print(f"The length of the string is: {field_size}")

# upper() & lower(): Ensures that all letters in a string match in case. 
chant = "Go Team"
loud_chant = chant.upper()
quiet_chant = chant.lower()

print(loud_chant)
print(quiet_chant)

# replace(): Allows us to substitute one part of our string with another. 
game_plann = "Attack from the left flank"
print(game_plann)

new_game_plan = game_plann.replace("left", "right")
print(new_game_plan)

# strip(): Removes any unwanted whitespace from the beginning & the end.
player_name = " Ronaldo  "
clean_name = player_name.strip()
print(player_name)
print(f"{clean_name} is ready to play!")

# split(): Breaks a string into a list of smaller strings
# join(): Brings a list of strings together into one cohesive unit.
chantt = "Here we go, team, here we go!"
words = chantt.split()
new_chant = " ".join(words)
print(words)
print(new_chant)

# The separator in split()
plays = "pass,run,block,kick"
individual_plays = plays.split(",")
print(plays)
print(individual_plays)
# pass run block kick each get spint into their own individual strings

