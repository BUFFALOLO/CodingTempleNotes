# PYTHON REGULAR EXPRESSIONS
"""
Regular Expressions (regex) are a powerful tool for pattern matching & text manipulation that allows you to: search efficiently, validate data, manipulate text & save time.

Regex builds upon the foundations of strings & loops
strings: enhance your ability to analyze & manipulate strings
loops: help you process multiple pieces of text in sophisticated ways

Regex uses 2 main types of characters
literal characters: exact characters you want to match
metacharacters: special symbols that represent broader categories or patterns

metacharacters are the building blocks of regex patterns, each serving a special function

METACHARACTERS
1. Dot (.) - matches any single character except newline(\n). Imagine it as a shape-shifter, able to become any character you need, just for a moment.
2. Caret (^) - the anchor for the start of a string. Like a sentinel, standing guard at the beginning of your text.
3. Dollar ($) - the anchor for the end of string. The sentinel at the gates, ensuring nothing goes beyond the end of your text.
4. Asterisk (*) - matches 0 or more occurrences of the pattern left to it. Think of it as a multiplier, creating copies of the character before it.
5. Plus (+) - matches one or more occurrences of the pattern left to it. Similar to the asterisk, but insists on at least 1 occurrence.
6. Question Mark (?) - it makes the preceding character optional. It's the symbol of uncertainty, allowing flexibility in your patterns.
7. Backslash (\) - escapes special characters or signals a special sequence. They key to differentiating between a literal character & a magical symbol.
8. Brackets [] - a set of characters. Matches any one character in the brackets. Like choosing one tool from a toolbox, it selects 1 character from a set.
9. Pipe (|) - the OR operator. It matches either the pattern before or after it. A fork in the road, giving you a choice between paths.
10. Parentheses () - groups patterns together & captures them. Think of them as binding a spell, containing its power within.
11. Curly Braces ({}) - curly braces are used to define the exact number of times a character or a pattern must occur for a match to be found. It's like telling your magic spell exactly how much power to use

SPECIAL SEQUENCES
\d - hunts down digits (0-9) in your text. Use it when you need to find or validate numbers, such as in phone numbers or dates. Its like a metal detector that beeps only when it finds numbers.
\w - find word characters (letters, digits & underscores). Imagine it as a magnet that attracts only words & numbers, leaving everything else behind.
\s - seeks out whitespace (spaces, tabs, newlines). Think of it as a radar that pins whenever it detects open space in your text.

Regex sets, symbolized by square brackets, function like a painter's palette for characters. They allow you to tailor your search by defining specific groups
[abc] can match a, b or c
[a-z] can match any lowercase letter
These sets act as customizable tools, enabling you to precisely mix & match characters in the vast expanse of text, akin to a painter creating the perfect shade with a palette of colors.

Within sets, you can define ranges
[a-e] matches any letter from a to e
[a-z] match any alphanumeric character

Integrating sets with Python concepts
With Loops: Iterate through strings, using sets in regex to process or extract specific patterns.
With Conditions: Use sets in regex within conditional statements to make decisions based on text patterns.

Regex pattern: [aeiou]
Sentence: Regular expressions are fun
Expected Matches: e u a e e i o a e u
Explanation: The set [aeiou] matches any vowel in the sentence.

Regex pattern: [A-Za-z]
Sentence: Regex in Python 3.12 is powerful!
Expected Matches: R e g e x i n P y t h o n i s p o w e r f u l
Explanation: [A-Za-z] includes all lowercase & uppercase letters, leaving out numbers & symbols.

Regex pattern: [0-9!@#\$%\^&\*\(\)]
Sentence: The price is $15 for 3 items! #Sale
Expected Matches: $ 1 5 3 ! #
Explanation: The set [0-9!@#\$%\^&\*\(\)] is like selecting both the numbers & special accent colors on your palette, allowing you to pick out digits & special characters from the sentence.

Regex pattern: [a-z!?]
Sentence: What is regex? It's amazing!
Expected Matches: h a t i s r e g e x ? t s a m a z i n g !
Explanation: [a-z!?] combines a range of lowercase letters with ! and ?

The re module in Python is a built-in library that provides support for writing Regular Expressions.
It's like a specialized toolbox for text pattern recognition & manipulation.
Regular Expressions are sequences of characters used as a search pattern. THey can be used for everything from validating strings to parsing text data.
Key features of the re module:
    - Pattern matching - search for specific text patterns within strings
    - String parsing & splitting - break down strings into components or extract specific parts
    - Text substitution - replace text in strings based on pattern matching
    - Complex string manipulation - perform advances manipulations that go beyond basic string methods

COMMONLY USED FUNCTIONS IN RE
re.findall() - Retrieves all non-overlapping matches of a pattern in a string, returning them as a list. 
re.search() - Scans through a string, looking for any location where the pattern matches.
re.match() - Determines if the regex pattern matches at the beginning of a string
re.split() - Splits a string by occurrences of the pattern
re.sub() - Replaces occurrences of the pattern in a string with a replacement string

"""
import re 

# re.findall() - This function is particularly useful in data extraction, text analysis & processing tasks where pattern recurrence is key
text = "Contact us at support@example.com or sales@example.com"
emails = re.findall(r"[A-za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", text)
print(emails)

post = "Loving the #Python and #Regex learning journey! #coding"
hashtags = re.findall(r"#\w+", post)
print(hashtags)

sentence = "Write a program to build a bridge but beware of the beehive"
words = re.findall(r"\bb\w*e\b", sentence)
print(words)

# re.search() - Think of this as a high-precision tool in your text exploration journey, akin to a metal detector that beeps when it finds something interesting.
# Unlike re.findall(), which retrieves all matches, re.search() focuses on finding the 1st occurrence of a pattern within a string. 
# It's perfect for tasks where you need to locate specific info quickly & efficiently
email = "user@example.com"
if re.search(r"[A-za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", email):
    print("Valid email address.")
else:
    print("Invalid email address")

sentence = "The event was held on 15/06/2021."
match = re.search(r"\b\d{4}\b", sentence)
if match:
    print("Year extracted:", match.group())

# re.match() - Picture this as a vigilant guard standing at the gates of your text, only allowing patterns that appear right at the beginning to pass through. 
# This function is specifically designed to check if a regex pattern matches at the start of a string. 
text = "Hello, World!"
if re.search(r"^Hello", text):
    print("The string starts with Hello.")
else:
    print("The string does not start with Hello.")

text = "@user123"
if re.match(r"@\w+", text):
    print("Valid username format")
else:
    print("Invalid username format")

url = "https://www.example.com"
match = re.match(r"^(https|http)", url)
if match:
    print("Protocol found: ", match.group())

# re.split() - This function is particularly useful for breaking down data into manageable parts or when dealing with inconsistent delimiters.
text = "Python, Regex;Splitting-Examples. Fun, right?"
words = re.split(r"[,;.\s-]+", text)
print(words)

csv_data = "Name,Age,Occupation"
fields = re.split(r",", csv_data)
print(fields)

sentence = "Hello,world!Welcome to Python."
parts = re.split(r"(\W+)", sentence)
print(parts)

# re.sub() - This function is a powerful tool for modifying & cleaning up strings, allowing for both simple replacements & more complex, pattern-based transformations.
phone = "Phone:+1(123)456-7890"
standard_phone = re.sub(r"\D","",  phone)
print(standard_phone)

html = "<p>This is <em> HTML</em> content! </p>"
clean_text = re.sub(r"<.*?>", "", html)
print(clean_text)

date_string = "Today's date is 15/04/2021."
formatted_date = re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\2-\1", date_string)
print(formatted_date)

