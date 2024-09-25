"""
In the realm of Python, variables are like shape-shifting creatures. 
They can take on different values, & when used as indices, they offer a dynamic way to access items in a list. 

The len() function is like a magical spell that counts the number of items in your string (or list). 
When you cast this spell on the hobbies list using len(hobbies), it returns the total number of hobbies.
"""

hobbies = ["reading", "painting", "writing"]
total_hobbies = len(hobbies)
print(total_hobbies)

"""
Variable Elements: Like a map showing a variable that can point to any item based on its value.
Variable Indexing: You can store this position in a variable & use it to unveil the hobby.
Dynamic Access with Variables: By changing the value of the position variable, you can access different hobbies without altering the core spell.
"""

print(hobbies)

position = 1 # The whispers speak of the second position

mystery_hobby = hobbies[position] # This unveils "painting"
print(mystery_hobby)

# Index mathematical/logical expressions: //
middle_index = len(hobbies) // 2
middle_hobby = hobbies[middle_index]
print(middle_hobby)

