# PYTHON TUPLES
"""
Tuples is like delving into the classic section of a library.
These unchangeable, ordered sequences are akin to timeless literary works, each element a chapter in its own right, holding its unique place & value.

When you create a tuple, the order of the elements is fixed.

Tuples are immutable. Once a tuple is created, its content cannot be modified. A tuple gives you the certainty that its content will not change inadvertently.

Tuples allow duplicates. This feature can be useful in cases where you need to count occurrences or ensure that certain values are always available, regardless of how many times they appear.

Consistency in Repetition: The ability to have duplicate elements in a tuple is like having multiple copies of an important chapter in a book. It ensures that the info is readily available.

It's crucial to understand why & when to choose tuples over other data types like lists and dictionaries. 

Predictability & Safety: Their unchangeable nature means the data you store in tuples won't accidentally be modifies, which is crucial in certain programming scenarios where data integrity is paramount.

Performance & Efficiency: Tuples are faster than lists when it comes to iterating through elements, similar to how quickly you can flip through a well known book compared to a manuscript filled with
notes & edits. This speed becomes significant in scenarios where a large amount of data is being processed, and every millisecond counts.

Tuples vs Lists: If lists are like notebooks where you can add, remove or change pages, tuples are like printed books. The content in a tuple, like a printed book, is there to stay. Use tuples
when your data should not be modified & lists when you need a mutable sequence.

Tuples vs Dictionaries: Dictionaries are akin to encyclopedias with a system to find information quickly (key-value pairs). While dictionaries are mutable & great for fast data retrieval with
unique keys, tuples are simpler & better suited for ordered, unmodifiable collections. Use tuples for simpler, ordered, & unchanging data & dictionaries when you need a mutable, non-ordered
collection w/ a unique key for each pair.

Lists: Ordered, indexed, mutable, duplicates are allowed, mutable & immutable types allowed.
Tuples: Ordered, indexed, immutable, duplicates are allowed, mutable & immutable types allowed.
Dictionaries: Ordered, keyed indexing, mutable, duplicates are allowed in values but not keys, only keys are immutable.

empty_tuple = ()

BASIC TUPLE CREATION
my_tuple = ("fantasy", "Mystery", "Poetry")

my_tuple = "Epic", "Fable", "Legend"
another_packed_tuple = "Prologue", "Conflict", ["Climax", "Resolution"]

NESTED TUPLE
nested_tuple = ("Foreword", ("Chapter 1", "Chapter 2"), "Epilogue")
another_nested_tuple = ("Prologue", ("Conflict", ["Climax", "Resolution"]), "Afterword")
"""

"""
Think of indexing as revisiting a familiar chapter in a different book within our grand Python library. Just like how you would find a specific chapter in a list-themed book by its chapter number (positive indexing)
or start from the back & count backward (negative indexing), the same principles apply to tuples.
    Positive Index: Each element in a tuple is indexed starting from 0.
    Negative Index: Each element in a tuple is indexed starting from -1, which is the last element
"""
my_tuple = ("Prologue", "Adventure", "Epilogue")
print(my_tuple[0])
print(my_tuple[-1])

"""
SLICING TUPLES
Slicing a tuple is similar to reading a specific section of a book, from one chapter to another. It's helpful to recall our previous adventures with lists. The process of slicing
tuples is similar to skimming through specific sections of a book, much like we explored with lists. In both scenarios, we use a similar method.
REMEMBER: The 2nd number that you list is where the slicing ends therefore Epilogue is index 2 but if you wanted to print that you would do 0:3
"""
print(my_tuple[0:2])

"""
ACCESSING NESTED TUPLES
In nested tuples, similar to nested lists, accessing elements involves peeling back layers, & exploring stories within stories or books within books.
This layered approach provides a familiar framework for understanding & navigating complex data structures. As you explore nested tuples, remember the interconnected tales from nested lists.
A journey within the broader narrative of Python programming.
"""

grand_library = ("Ancient Myths", ("Greek", "Norse"), "Modern Tales")
print(grand_library[1][1])

"""
In this example, we have an anthology with 2 volumes, where first 1st volume contains chapters & even pages within a chapter. To access Page 2 of Chapter 2 in Volume 2. This is similar
to navigating through the first volume, finding the second chapter & then turning to the second page
"""
nested_anthology = ("Volume 1", ("Chapter 1", "Chapter 2", ("Page 1", "Page 2", "Page 3")), "Volume 2")
print(nested_anthology[1][2][1])

historical_record = ("Medieval Era", ("Knights", "Castles", ("King", "Queen")), "Renaissance Period")
print(historical_record[1][2][1])


# Consider a nested structure where a tuple contains a list, & that list contains another tuple. It's like a bookshelf holding a series of books, some of which contain other smaller books within them.
enchanted_library = ("Magic Tome", ["Ancient Scrolls", ("Spell", "Curse")], "Wizards Guide")
print(enchanted_library[1][1][1])

# Nested structures can be multi-layered, creating a complex network of tuples & lists. In this example, we have a mixture of tuples & lists nested within each other. 
mythical_collection = ("Greek Myths", [("Zeus", "Hera"), ["Mount Olympus", ("Lightning", "Thunder")]], "Norse Myths")
print(mythical_collection[1][1][1][1])

# Adding dictionaries to our nested tuples & lists is akin to including detailed references within our books. These dictionaries can provide specific information, akin to a glossary or an atlas.
# In this example, enchanted library is a tuple w/ a dictionary as its 2nd element. The dictionary contains a list under Mythical Creatures & a tuple under Legendary Places.

enchanted_library = ("Chapter 1", {"Mythical Creatures": ["Dragon", "Unicorn"], "Legendary Places": ("Atlantis", "El Dorado")}, "Chapter 2")
print(enchanted_library[1]["Legendary Places"][1])

"""
While you can't directly change a tuple, you can convert it into a list, modify the list, & then turn is back into a tuple. It's like photocopying a page from a book, making edits to the copy,
& then binding it into a new book
"""
my_tuple = ("Introduction", "Conclusion")
print(my_tuple)
temp_list = list(my_tuple)
temp_list.append("Epilogue")
my_tuple = tuple(temp_list)
print(my_tuple)

"""
Exploring the dichotomy of immutability in programming reveals both the protective benefits of safeguarding data integrity & the consequential challenges of adaptability as follows:
Stability & Reliability: It ensures that the data remains consistent & uncorrupted over time.
Performance: Immutable objects, such as tuples, are faster to process than mutable counterparts like lists, akin to quickly referencing a well-known book versus editing a manuscript.
"""
# TUPLE UNPACKING
# Basic unpacking involves assigning each element of a tuple to a separate variable. 
my_tuple = ("Magic", "Mystery", "Myth")
genre1, genre2, genre3 = my_tuple
print(genre1)
print(genre2)
print(genre3)

# EXTENDED UNPACKING
# This method is especially useful when dealing with tuples of unknown or variable length. It's akin to receiving a box of books of different sizes & being able to distribute them efficiently.
my_tuple = ("Prologue", "Adventure", "Climax", "Epilogue")
beginning, *middle, end = my_tuple
print(beginning)
print(middle)
print(end)

"""
LOOPING THROUGH TUPLES
Looping through tuples, is similar to how a reader journeys through the pages of a book. Tuples, with their unchanging nature, can be iterated over using for loops, while loops with indexing,
& the convenient enumerate function.

A for loop is like reading through each chapter of a book sequentially. It's straightforward & efficient for going through each element in a tuple.
A while loop, combined with indexing, is like flipping through the pages of a book 1 at a time. This method provides more control, as you can use an index to access each element.
Consider enumerate as a wise storyteller. When summoned, it only narrates the tales (elements of a collection) but also meticulously notes their order (their index). 
What sets enumerate apart is its ability to return a tuple for each item in a collection, seamlessly combining the index & the item. While versatile & compatible with various collections,
its tru prowess shines in ordered structures like lists & tuples, where the index holds a clear & consistent significance.
"""
book_titles = ("Moby Dick", "1984", "To Kill a Mockingbird")
for title in book_titles:
    print(title)

authors = ("Herman Melville", "George Orwell", "Harper Lee")
index = 0
while index < len(authors):
    print(authors[index])
    index += 1

chapters = ("The Lighthouse", "The Ministry of Truth", "The Trial")
for index, chapter in enumerate(chapters):
    print(f"Chapter {index + 1}: {chapter}")

"""
NAVIGATING NESTED TUPLES
This is like delving into a multi-layered novel , with each level representing a different layer of the story.Before embarking on the journey of looping through a nested tuple, understanding
its depth - how many layers of stories it contains - is crucial. This awareness is essential for selecting the appropriate approach to navigate through the nested structure efficiently.

Understanding the depth of nested tuple is crucial; otherwise, you risk skimming the surface & missing deeper elements. In our lesson, we're exploring straightforward looping for tuples
with a known depth. However, deeply nested tuples require advanced methods like recursion - akin to navigating an anthology with multiple layers or narrative.

Looping through a nested tuple is like reading a book that contains other books. 
"""
nested_tables = (("The Dawn", "The Noon"), ("The Dusk", "The Night"))
for pair in nested_tables:
    for tale in pair:
        print(tale)

# LOOPING THROUGH NEST TUPLES WITH LISTS
# When tuples contain lists, it's like a book with chapters that have their own sections. We loop through each chapter & then through its sections.
mixed_collection = ("Poetry", ["Sonnet", "Haiku"], "Prose")
for element in mixed_collection:
    if isinstance(element, list):
        for item in element:
            print(f"List Item: {item}")
    else:
        print(f"Tuple Element: {element}")

# LOOPING THROUGH TUPLES WITH DICTIONARIES
# Tuples containing dictionaries are like volumes with detailed encyclopedic entries. We iterate through each entry for insights.
historical_records = ("Ancient", {"Rome": "Republic", "Greece": "Democracy"}, "Medieval")
for element in historical_records:
    if isinstance(element, dict):
        for key, value in element.items():
            print(f"{key}: {value}")
    else:
        print(element)

# count() method in tuples is like counting how many times a specific word or theme appears in a book. 
literary_elements = ("Irony", "Metaphor", "Irony", "Symbolism")
print(literary_elements.count("Irony"))

# index() method is similar to finding the page number of the first occurrence of a chapter title in a book. It returns the index of the 1st occurrence of a specified element.
book_chapters = ("Introduction", "Rising Action", "Climax", "Conclusion")
print(book_chapters.index("Climax"))

# The + operator is the seamstress of our tuple fabirc, seamlessly stitching together separate collections into one continuous thread.
epic = ("Odyssey", "Iliad")
drama = ("Hamlet", "Orthello")
literary_union = epic + drama
print(literary_union)

# Nesting tuples allow us to combine collections while retaining their identity, like placing distinct sets of books on a shared shelf.
historical = ("War and Peace", "Gone with the Wind")
fantasy = ("Lord of the Rings", "Harry Potter")
big_library = (historical, fantasy)
print(big_library)

# While the immutability of tuples limits certain operations, there are still various ways we can manipulate & explore these data structures such as repeating tuples & the tuple membership test.
# Tuples can be repeated using the times operator, much like reprinting a beloved story to fill a shelf.
short_story = ("A Tale",)
anthology = short_story * 3
print(anthology)

# Checking if an item exists in a tuple is like searching for a specific book in a collection.
if "Odyssey" in literary_union:
    print("Epic tale found")

# 