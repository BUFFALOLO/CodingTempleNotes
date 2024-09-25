hobbies = ["reading", "painting", "cycling"]
print(hobbies)

hobbies.append("singing")
print(hobbies)

# Inserting Items: If you need to add an item at a specific position in the list, use the insert() method. 
# This method takes two arguments: the index where you want to add the item & the item itself.
hobbies.insert(1, "dancing")
print(hobbies)

# Changing an Item in a List: If you want to change an existing item in a list, you simply assign a new value to its specific index.
# If you want to change reading into writing
hobbies[0] = "writing"
print(hobbies)

# Removing by Value: If you know the exact item you want to remove, you can use the remove() method. 
# This method finds the first occurrence of the specified value & removes it from the list.
hobbies.remove("cycling")
print(hobbies)

# Popping Items: The pop() method is used to remove items by their position or index. 
# If you don’t provide an index, pop() will remove the last item in the list by default. You can also specify an index to remove a specific item.
last_hobby = hobbies.pop()
print(last_hobby)

# If you want to remove an item from a specific position, you can pass the index to pop()
second_hobby = hobbies.pop(1)
print(second_hobby)

# Counting Occurrences: COUNT - Repeated items: How many times?
count_reading = hobbies.count("reading")
print(count_reading)

# Finding Position: POSITION - Where exactly is an item?
position_painting = hobbies.index("painting")
print(position_painting)

# If you're finished with a list & want to remove all its items at once you can use the clear() method.
# This method empties the list, leaving it blank but still available for future use.
# After running this code the hobbies list will be completely empty and will show [], indicating that all the items have been removed. 
# This is a quick & easy way to reset a list without deleting the list iteself.

hobbies.clear()
print(hobbies)