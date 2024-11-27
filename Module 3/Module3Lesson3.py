# PYTHON SETS
"""
Elements don't have a fixed position.
Unique characteristic - no duplicates rule.
Once an element is in a set, it is unchangeable.
Set elements are unindexed.

SETS vs LISTS OR TUPLES vs DICTIONARIES
SETS: 
    Uniqueness - Eliminate duplicates
    Performance - Faster
    Simplicity in Uniqueness operations - Operations like union, intersection & difference is straightforward
    No key-value pairs needed - No value associating additional information
    Set-specific operations - Perform set operations

LIST/TUPLES: 
    Uniqueness - Does not eliminate duplicates
    Performance - Not so fast 
    Simplicity in Uniqueness operations - No straightforward operations

DICTIONARIES:
    No key-value pairs needed - Associating additional information
    Set-specific operations - Operations that aren't directly available or efficient
"""

# Using Curly Braces {}: This is like creating a guest list with the names Alice, Bob & Charlie. Remember, no duplicates are allowed.
unique_party = {"Alice", "Bob", "Charlie"}
print(unique_party)

# Using the set() Constructor: This is like having a list of potential guests & then deciding. 
guest_list = set(["Alice", "Bob", "Charlie"])
print(guest_list)

# How to turn a list, tuple or dictionary into a set party.

# From a list: This is like taking a regular party list & converting it into our unique name party. The duplicate Alice gets automatically removed.
list_guests = ["Alice", "Bob", "Alice", "Diane"]
set_party = set(list_guests)
print(set_party)

# From a Tuple: Like waving a magic wand & transforming a formal event (tuple) into our cool set party.
tuple_guests = ("Alice", "Bob", "Charlie")
set_party = set(tuple_guests)
print(set_party)

# CONVERTING OTHER DATA TYPES TO SETS: How to turn a list, tuple or dictionary into a set party.
# From a Dictionary: Here, we're inviting only the values from a dictionary, ensuring they're unique at our set party.
# REMEMBER: A set cannot contain another set directly as its element. This is because sets are designed to only contain hashable objects & sets themselves are not hashable. 
# The unhashability of sets is due to their mutable nature; their contents can change, which makes it impossible for them to have a consistent hash value.

dict_guests = {"name1": "Alice", "name2": "Bob", "name3": "Alice"}
set_party = set(dict_guests.values())
print(set_party)

# ACCESSING ELEMENTS IN SETS
# Using loops: Just as you stroll through the party to see who's there, you can loop through a set to access its elements.
for guest in {"Alice", "Bob", "Charlie"}:
    print("Welcome,", guest, "to the party!")

# The "in" keyword
guests = {"Alice", "Bob", "Charlie"}
if "Alice" in guests:
    print("Alice is enjoying the party.")
else:
    print("Alice couldn't make it.")

# ADDING & UPDATING ELEMENTS IN SETS
# Just like deciding to invite more friends to our exclusive party, in sets, you can always add new & unique guests, but remember, no duplicates are allowed. 
# The Rule of Uniqueness: Constraints on Adding to Sets
# Immutability of Elements - Elements can be removed or added. They cannot change or be modified.
# No Duplicates Allowed - Duplicated elements have NO effect.

guests = {"Alice", "Bob", "Charlie"}
guests.add("Diana")
print(guests)

guests = {"Alice", "Bob", "Charlie"}
more_guests = ["Ethan", "Fiona"]
guests.update(more_guests)
print(guests)

# REMOVING ELEMENTS FROM SETS
# Choosing the right method - best practices in set management
# remove - elements are in the set for sure
# discard - not sure if the element is in the set or not
# pop - need to remove an element, no matter which one
# clear - delete every element & start fresh

guests = {"Alice", "Bob", "Charlie"}
guests.remove("Charlie")
print(guests)
guests.discard("Diana")
print(guests)

random_guest = guests.pop()
print("We randomly asked", random_guest, "to leave.")

guests.clear()
print(guests)

# Union: The Grand Gathering
# What? Joining 2 parties' guest list, ensuring no one is invited twice.
# Practical Use: Merging 2 datasets while ensuring no duplicate entries.
set1 = {"Alice", "Bob", "Charlie"}
set2 = {"David", "Emma", "Charlie"}
grand_gathering = set1.union(set2)
print(grand_gathering)

# Intersection: Finding Common Ground
# What? Identifying the same guests in 2 different party lists.
# Practical Use: Finding common elements in datasets.
set1 = {"Alice", "Bob", "Charlie"}
set2 = {"David", "Emma", "Charlie"}
mutual_friends = set1.intersection(set2)
print(mutual_friends)

# Difference: The Exclusive Aspect
# What? Identifying the exclusive attendees.
# Practical Use: Identifying unique features.
set1 = {"Alice", "Bob", "Charlie"}
set2 = {"David", "Emma", "Charlie"}
exclusive_guests = set1.difference(set2)
print(exclusive_guests)

# Symmetric Difference: Identifying Uniqueness
# What? Finds people who are in 1 of the 2 parties going on.
# Practical Use: Compares datasets to find elements exclusive to each.
set1 = {"Alice", "Bob", "Charlie"}
set2 = {"David", "Emma", "Charlie"}
unique_attendees = set1.symmetric_difference(set2)
print(unique_attendees)

# PRACTICAL TIPS & TRICKS FOR SET OPERATIONS
# Union for Merging: union - collection from multiple sets without worrying about duplicates.
# Intersection for Commonalities: intersection - pinpoint similarities between sets.
# Difference for Uniqueness: difference - highlight the unique aspects of a set.
# Symmetric Difference for Exclusive Analysis: symmetric difference - extract elements that are exclusive to each set.

# Using enumerate: Use enumerate to loop through the set with an index
guests = {"Alice", "Bob", "Charlie"}
for index, guest in enumerate(guests):
    print(f"Guest #", index, "is", guest)

# Enumerate to keep track of iterations for logging, debugging or performing operations of amounted elements processed.
# Generating a list of items with their indices for display purposes or mapping set elements to another list.
guests = {"Alice", "Bob", "Charlie"}
for index, guest in enumerate(sorted(guests)):
    print("Welcome, guest #", index, ":", guest)

"""
SET COMPREHENSIONS: THE EFFICIENT WAY TO BUILD SETS

The Concept: make sets quickly using existing lists or sequences, and you can add conditions or changes if you want.
Why use them: provide a clearer & more efficient method for forming sets, especially when incorporating conditions or operations on the elements.
Unique by nature: automatic elimination of duplicate elements
"""
square_party = {a**2 for a in range(6)}
print(square_party)

# you can add conditions to your set comprehensions to filter elements
odd_square_party = {a**2 for a in range(6) if a % 2 != 0}
print(odd_square_party)

# you can later multiple conditions to refine your set
special_set = {a for a in range(16, 35) if a % 2 == 0 if a % 3 == 0}
print(special_set)

# you can transform elements in a specific way, based on certain criteria
transformed_set = {a**2 if a % 2 == 0 else a for a in range(10)}
print(transformed_set)

"""
BEST PRACTICES FOR SET COMPREHENSIONS
Clarity is key: prioritize readability
Avoid overcomplicating: try not to nest multiple comprehensions or use complex conditions
Remember the uniqueness: set comprehensions are ideal where unique elements are a priority
"""

# Mistaking sets for lists or tuples: We can confuse sets with lists, & tuples as they might look similar. But remember, sets are unordered & don't allow duplicates.
# Mistakenly using a list instead of a set
party_items = ["cake", "balloons", "cake"] # a list, not a set
unique_items = set(party_items)
print(unique_items)

# Modifying sets during iteration: trying to add or remove elements from a set while iterating over it can lease to unexpected behavior or errors.
guests = {"Alice", "Bob", "Charlie"}
for guest in guests:
    if guest == "Alice":
        guests.remove(guest) # Risky operation!

"""
BEST PRACTICES FOR SET USAGE
Set Manners: Avoid modifications
Reserve a copy or plan modification for later
Example of excellence: unique & interesting
Practical Applications: no duplicates
Best Practice: uniqueness, unions or intersections
Efficient Planning: clear & concise
"""
