# PYTHON DICTIONARIES
""" 
Dictionaries offer a robust & user-friendly method for storing & managing data, providing more than just a basic collection. 
They serve as an organized & efficient means to establish relationships between different data points. 
As you advance in your Python exploration, you'll discover the indispensability of dictionaries, particularly in handling intricate data structures, data analysis & web development.

The Key-Value Pair: Let’s picture a key-value pair as a 2 sided coin. On one side, you have the key - it's like your home address, unique & specific to you. 
On the flip side is the value, which can be anything from a number, a string, a list, or even another dictionary. 
The key points to the value & together, they make a pair that's stored in the dictionary’s memory bank. 

Keys: Every key in a dictionary is like a snowflake, unique in its own right. 
No 2 keys are the same, which means no mix-ups in the data world. 
If you try to create a key that already exists, Python will simply look at your with a digital squint & overwrite the original value with the new one. 

Values: In the world of dictionaries, values are akin to the dynamic personality of a coin, capable of changing & evolving. 
They offer versatility, allowing you to store a variety of data types - from numbers to strings, and even nested dictionaries. 
Unlike keys, values can be duplicated across different keys, similar to how different homes can share the same color. 
This flexibility adds a layer of adaptability to dictionaries, enabling them to accommodate diverse data types & structures. 

The Power of Association: The concept of a key-value pair is likened to a powerful association, drawing parallels with managing contacts in a phone. 
In this analogy, the name serves as the key, and the associated phone number is the value. 
This efficient pairing eliminates the need to scroll through an entire list of numbers; instead, users can seamlessly connect by using the key (name). 
The analogy emphasizes the simplicity & effectiveness of the relationship between keys & values in a dictionary, resembling the ease of accessing specific information in a contact list.

Embrace the Key-Value Pair: Understanding the key-value pair is like getting the secret password to a club - it unlocks the full potential of dictionaries in Python. 
It's the concept you'll rely on whether you're keeping track of inventory, managing user data, or even coding up your next game. 
"""

"""
Suppose you're starting to organize your kitchen but haven't decided where to store everything yet & 
decide to create a Python dictionary as a starting point, planning to fill it with info about where each item is stored.

In this example "kitchen" is our dictionary's name & the empty curly braces {} show that its like an empty kitchen waiting to be filled. 
Right now, there are no utensils or items plaaced in specific spots.
As you decide where each item goes (like spoons, plates, cups), you'll add these detials to the kitchen dictionary.
It's like creating a guide to help you find everything in your kitchen.
"""
kitchen = {}
print(kitchen)

"""
In this kitchen dictionary, we directly create a structured collection of items & their locations.
Here, we're adding a key-value pair where the key is "spoons" & the value\
    Create a dicitonary with the curly braces {}, & inside the braces define key-value pairs separated by commas
    Set key values (spoons, plates, cups) to represent different kitchen items
    Set values (top drawer, middle shelf, top shelf) to specify the designated storage location for each item
    Use a colon to separate each key from its corresponding value
"""
kitchen = {
    "spoons": "top drawer",
    "plates": "middle shelf",
    "cups": "top shelf",
    "blender": "counter"
}

"""
Accessing elements is a process akin to finding a specific book in a library or a particular tool in a workshop.
In Python dictionaries, this is achieved through the keys, acting as guides to swiftly locate the corresponding values.

Suppose you want to find where the spoons are kept. You would access the value associated with the key "spoons" like this
"""
location_of_spoons = kitchen["spoons"]
print(location_of_spoons)
# location_of_toaster = kitchen["toaster"]
# print(location_of_toaster)
# If you try to print the above 2 lines you will get the below error

# Traceback (most recent call last):
#   File "c:\Users\Couch\Documents\Software Engineering - CodingTemple\Module 3\Module3Lesson1.py", line 65, in <module>
#     location_of_toaster = kitchen["toaster"]
        
# KeyError: 'toaster'

"""
To avoid errors when a ket might not be present, Python provides the get() method.
It allows you to access a value safely, providing an option to return a default  value if the key is not found.
"""
location_of_toaster = kitchen.get("toaster", "not found")
print(location_of_toaster)

# ADDING & UPDATING ELEMENTS IN PYTHON DICTIONARIES
community_center = {
    "yoga": "8 AM",
    "art": "10 AM"
}
print(community_center)

community_center["cooking"] = "1 PM"
print(community_center)

# MODIFYING EXISTING VALUES
community_center["yoga"] = "7:30 AM"
print(community_center)

# pop( ) method: Removes the item with the specified key & returns its value. 
# If the key is not found, & a default value is provided, it returns the default. Otherwise, it raises a KeyError.
# pop(key, [default])
inventory = {"Apples": 30, "Oranges": 20, "Bananas": 15}
print(inventory)

removed_item = inventory.pop("Oranges")
print(removed_item)
print(inventory)

# popitem( ) method: Removes & returns the last inserted key-value pair as a tuple. 
user_data = {"name": "Alice", "age": 30, "city": "New York"}
remove_item = user_data.popitem()
print(remove_item)

# del: Removes the item with the specified key. If the key does not exist, it raises a KeyError
# del dictionary[key]
book_shelf = {"fiction": 10, "non-fiction": 7, "mystery": 5}
del book_shelf["non-fiction"]
print(book_shelf)

# clear: Empties the entire dictionary, leaving it as an empty dictionary
# clear( )
session_data = {"user_id": 12345, "status": "active", "theme": "dark"}
print(session_data)
session_data.clear()
print(session_data)
