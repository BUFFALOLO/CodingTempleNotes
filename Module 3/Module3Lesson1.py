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

"""
Iterating over a Python dictionary is comparable to inspecting every room in a building or examining each book on a library shelf. 
It involves a systematic examination of each piece of data within the dictionary. 
Python offers various methods for iteration, providing access to keys, values, or both.
"""
# item( ) method: Returns a view object that displays a list of dictionary’s key-value tuple pairs.
book_ratings = {"1984": 4.5, "To Kill a Mockingbird": 4.8, "Brave New World": 4.3}

for book, rating in book_ratings.items():
    print(f"{book} has a rating of {rating}")

# keys( ) method: Returns a view object that displays a list of all the keys in the dictionary.
user_profile = {"name": "Alice", "age": 30, "email": "alice@example.com"}

for key in user_profile.keys():
    print(key)

# values( ) method: Returns a view object that displays a list of all the values in a dictionary.
for value in user_profile.values():
    print(value)

"""
Sometimes, you may want to iterate through a dictionary’s keys in a specific order, like alphabetical or numerical order. 
This can be achieved by sorting the keys first and then iterating through them. 
"""
# The below example will print the keys in alphabetical order
colors_count = {"red": 3, "blue": 4, "green": 1}
for color in sorted(colors_count.keys()):
    print(f"{color}: {colors_count[color]}")

# update( ) method: Merges another dictionary or an iterable of key-value pairs into the current dictionary.
default_settings = {"theme": "light", "notifications": "on"}
print(default_settings)

user_settings = {"theme": "dark"}
default_settings.update(user_settings)
print(default_settings) 

add_setting = {"status": "active"}
default_settings.update(add_setting)
print(default_settings)

# setdefault( ) method: Returns the value of a specified key. If the key is not found, inserts the key with the specified default value.
stock = {"apples": 30, "oranges": 20}
stock.setdefault("bananas", 0)
print(stock)

"""
Copying can be compared to art replication techniques. 
There are two primary methods: shallow copying, akin to taking a high qualify photograph of a painting, and 
deep copying, which is like creating a detailed, independent reproduction of the original artwork.
"""
# Shallow Copy: A shallow copy of a dictionary is like taking a photograph of a painting. 
# The photo captures the image on the surface, but it's still intrinsically linked to the original painting. 
# In Python, this means the outer dictionary is duplicated, but the contents still reference the same objects. 
original_artists = {"Picasso": 1881, "Van Gogh": 1853, "Monet": 1840}
copied_artists = original_artists.copy()

# Changing a value in the copied dictionary
copied_artists["Van Gogh"] = 1900
print("Original:", original_artists) #Original remains unchanged
print("Copied:", copied_artists) #Copied reflects the change

# Deep Copy: Conversely, a deep copy in Python is like creating a completely new and independent reproduction of an original painting. 
# Every detail is recreated, ensuring that changes to the copy don’t affect the original. 
import copy
original_paintings = {"The Starry Night": "Van Gogh", "The Scream": "Munch"}
reproduced_paintings = copy.deepcopy(original_paintings)

# Changing a value in the deep copied dictionary
reproduced_paintings["The Starry Night"] = "Da Vinci"
print("Original:", original_paintings) #Original remains unchanged
print("Reproduced:", reproduced_paintings) #Reproduced reflects the change

# A shallow copy of a dictionary can lead to scenarios where changes in the copied dictionary inadvertently affect the original dictionary. 
# This typically happens when the dictionary contains mutable objects like lists.

# Original exhibit information
museum_exhibit = {
    "Ancient Vase": ["Greece", "Egypt"],
    "Renaissance Painting": ["Italy", "France"]
}

# Creating a shallow copy
exhibit_copy = museum_exhibit.copy()

# Adding a new country to the Ancient Vase list in the copied dictionary
exhibit_copy["Ancient Vase"].append("China")

print("Original Exhibit:", museum_exhibit)
print("Copied Exhibit:", exhibit_copy)

"""
In a shallow copy, changes made to a list within the copy are reflected in the original, as the copy retains references to the same objects. 
It’s akin to a brochure linked directly to an exhibit’s artifacts, where modifications to the brochure impact the displayed information in the exhibit.

When dealing with dictionaries containing mutable objects, it’s crucial to grasp that a shallow copy acts more like a mirrored reflection than a distinct entity. 
Any changes made in the shallow copy also  impact the original dictionary. For scenarios requiring independent manipulation of copied data, opting for a deep copy is the more suitable choice. 
"""

"""
Nested Collections: Navigating through nested collections in Python is akin to exploring a set of Russian nesting dolls, 
where opening one doll reveals another smaller doll inside, and so on. In Python, this concept is mirrored through nested dictionaries and lists - 
structures within structures, each holding its own data.

Lists within Dictionaries: Diving deeper into the concept of lists within dictionaries, we can liken this structure to a meticulously organized shelf in a library. 
Each section of the shelf (the key in the dictionary) is dedicated to a specific collection of items (the list). 
This arrangement not only ensures orderliness but also offers an intuitive way to categorize and access groups of related items.
"""
library = {
    "Fantasy": ["Harry Potter", "The Hobbit"],
    "Science Fiction": ["Dune", "Neuromancer"],
    "Mystery": ["Sherlock Holmes", "And Then There Were None"]
}
print(library)

library["Fantasy"].append("The Name of the Wind")
print(library)

for book in library["Science Fiction"]:
    print(book)

for genre,  books in library.items():
    print(f"Genre: {genre}")
    for book in books:
        print(f" - {book}")

"""
Dictionaries within Lists: Having dictionaries within a list can be metaphorically compared to a series of display cases in an art gallery. 
Each display case, represented as an item in the list, serves as a unique exhibit - a dictionary - with its set of attributes and descriptions. 
This organizational structure facilitates a methodical and detailed presentation of a collection of items, each distinct yet interconnected. 
"""
art_gallery = [
    {"Title": "The Starry Night", "Artist": "Vincent van Gogh", "Year": 1889},
    {"Title": "The Scream", "Artist": "Munch", "Year": 1893},
    {"Title": "Guernica", "Artist": "Picasso", "Year": 1937}
]

art_gallery.append({"Title": "The Persistence of Memory", "Artist": "Dali", "Year": 1931})

for artwork in art_gallery:
    print(f"Title: {artwork['Title']}, Artist: {artwork['Artist']}, Year: {artwork['Year']}")

"""
Nested Dictionaries: Exploring nested dictionaries is like navigating a cabinet of curiosities. 
Each drawer (outer dictionary) houses smaller compartments (inner dictionaries), each containing specific items (key-value pairs). 
This layered structure mirrors the complexity of a cabinet, revealing details and information within each level.
"""
museum_exhibits = {
    "Ancient Egypt": {
        "Artifacts": ["Sphinx", "Pyramids"],
        "Famous Pharaohs": ["Tutankhamun", "Cleopatra"]
    },
    "Renaissance Art": {
        "Notable Artists": ["Da Vinci", "Michaelangelo"],
        "Key Works": ["Mona Lisa", "The Last Supper"]
    }
}

print(museum_exhibits)

museum_exhibits["Ancient Egypt"]["Recent Discoveries"] = ["New Tomb", "Ancient Scrolls"]
print(museum_exhibits)
print(museum_exhibits["Ancient Egypt"])

for exhibit, details in museum_exhibits.items():
    print(f"Exhibit: {exhibit}")
    for section, items in details.items():
        print(f" {section}: {',' .join(items)}")

"""
Common mistakes in using dictionaries often revolve around misunderstandings of how dictionaries work or overlooking certain behaviors. Here are some common pitfalls:
	Using Non-Immutable Types as Keys
	Modifying Dictionary Size During Iteration
	Assuming Dictionaries Are Ordered

Tips for Clean & Efficient Dictionary Code
	Use get( ) and setdefault( ) for Safe Access & Assignment
	Leverage Dictionary Comprehensions for Efficiency
	Iterate with items( ), keys( ) & values( ) when appropriate
	Avoid redundant key lookups
	Be mindful of memory usage with large dictionaries
"""
