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
