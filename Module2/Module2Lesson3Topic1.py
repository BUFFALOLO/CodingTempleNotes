""" Think of it as a digital shopping basket where you can toss in items of all sorts, from numbers to words, and even other baskets.
You can start by defining a list with square brackets [] & placing the items inside, separated by commas. 
When you print the list it shows all the items in the order they were added.
"""
potions = ["Healing", "Invisibility", "Strength"]
print(potions)

"""
Alternatively, you can initialize an empty list & add items to it later. 
Lists are dynamic, meaning you can easily add, remove, or modify elements without needing to declare the list size beforehand.
"""
empty_list = []

"""
Lists are ordered collections, where each element has a specific position, called an index. 
This means that every item in the list can be accessed by its index, starting from 0 for the first item, 1 for the second and so on. 
This makes it easy to retrieve, update or manipulate specific elements within the list.
"""
print(potions[0])
print(potions[1])
print(potions[2])

favorite_potion = potions[1]
print(favorite_potion)

last_potion = potions[-1] # This will fetch you "Strength"
print(last_potion)

eclectic_list = [42, "unicorn", 3.14, "apple", "banana", "cherry"]
print(eclectic_list)

# Add an item to the list
eclectic_list.append("starry night")
print(eclectic_list)

# Remove an item from the list
eclectic_list.remove(42)
print(eclectic_list)

# Duplicate Items: A list can have duplicate items, which are simply items with the same value appearing more than once.
flowers = ["rose", "lily", "rose", "daisy", "lily"]
print(flowers)

#Counting Duplicates: If you want to know how many times a particular item appears in the list you can use the count() method. 
# This method takes the item as an argument and returns the number of times it appears in the list.
rose_count = flowers.count("rose")
print(rose_count)

#Removing Duplicates: Removing items from a list that contains duplicates can be tricky. 
# If you use the remove() method to delete an item, it will only remove the first occurrence of that item. 
# If there are more duplicates, they will remain in the list. **Only the first “lily” vanishes, leaving one behind.**
flowers.remove("lily") 
print(flowers)

