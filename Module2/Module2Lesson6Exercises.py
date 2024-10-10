# 1. The Book Index Finder
"""
You are developing a feature for an e-reader app that allows users to find the index of character in a book or document
This feature helps users to quickly navigate through the text by character references
    Write a function find_character_index that takes a text string and a character as parameters & returns the index of the characer in the text
    If the character is not found, the function should reutn a message stating that the character is not present
    Implement a loop that prompts the user to enter a string (representing a paragraph or line from a book) & a character to search for
    Use the function to find the index of the character & print the result using an f-string
    Ensure the program handles cases where the user may enter multiple characters instead of a single one
"""
def find_character_index(text, character):
    if len(character) == 1:
        index = text.find(character)
        if index == -1:
            return f"The character '{character}' is not present in the text."
        else:
            return f"The index of the character '{character}' is: {index}"
    else:
        return "Please enter only a single character"
    
while True:
    text_input = input("Enter a line of text from the book: ")
    char_input = input("Enter the character to find: ")

    result = find_character_index(text_input, char_input)
    print(result)

    continue_search = input("Do you want to search for another character? (yes/no): ").lower()
    if continue_search != 'yes':
        break

# 2. The Echo Text Generator
"""
You are tasked with developing a fesature for a social media app that allows users to create a fun echo effect with their text posts
This feature repeats each character in the text to create an echo=like pattern, making the posts more engaging & visually appealing
    Write a function generate_echo_text that takes a text string as a parameter & returns a new string with each character repeated twice
    Implement a loop that promots the user to enter a string (representing a social media post or message)
    Use the function to generate the echo text & print the result using an f-string
    Ensure the program handles empty strings & informs the user accordingly.
"""
def generate_echo_text(text):
    if text:
        return ''.join([char * 2 for char in text])
    else:
        return "The input text cannot be empty. Please enter some text."
    
while True:
    user_input = input("Enter your text to echo: ")

    echo_text = generate_echo_text(user_input)
    print(f"Your echoed text is: {echo_text}")

    continue_echo = input("Do you want to create another echo text? (yes/no): ").lower()
    if continue_echo!= 'yes':
        break

# 3. The Game Highlight
"""
You are developing a feature for a sports app that allows users to input a series of game highlights and then displays each event separately for easy reading & analysis
This feature is particularly useful for users who want to quickly create summaries of key moments in a match or game
    Write a function format_highlights that takes a string of highlights separates by commas & returns a list of individual plays
    Implement a loop that prompts the user to enter the string of highlights
    Use the function to format the highlights & print each play on a new line using an f-string
    Ensure the program handles empty strings by informing the user & asking for input again
"""
def format_highlights(highlight_string):
    if highlight_string.strip():
        return [play.strip() for play in highlight_string.split(',')]
    else:
        return []
    
while True:
    user_input = input("Enter the game highlights, separated by commas: ")
    formatted_highlights = format_highlights(user_input)

    if formatted_highlights:
        print("Game highlights: ")
        for play in formatted_highlights:
            print(f" - {play}")
    else:
        print("No highlighted entered. Please provide the highlights of the game")

    continue_input = input("Do you want to enter more highlights? (yes/no): ").lower()
    if continue_input != 'yes':
        break

# 4. The Annoucement Speaker
"""
You are creating a feature for a public address system app that allows users to input a message & then displays the message in uppercase which represents the announcement mode
    Write a function announce_message that takes a string & returns the same string in uppercase
    Implement a loop that prompts the user to enter their message
    Use the function to convert the message & print it using an f-string
    Ensure the program handles empty strings by informing the user & asks for input again
"""
def announce_message(message):
    return message.upper()

while True:
    user_input = input("Enter your message for the announcement: ")
    if user_input.strip():
        announcement = announce_message(user_input)
        print(f"Announcement: {announcement}")
    else:
        print("No message entered. Please provide a message for the announcement.")

    continue_input = input("Do you want to make another announcement? (yes/no): ").lower()
    if continue_input != 'yes':
        break

# 5. The Personalized Welcome Mat
"""
You are developing a feature for a hospitality app that personalized the welcome experience for guests
The app takes the guests name as input & prints a welcome message, with the name beautifully centered within a design made with asterisks
    Write a function create_welcome_message that takes a string (the users name) & returns a welcome message
    The welcome message shouls have the users name centered within a line of asterisks
    Implement a loop that prompts the use to enter their name
    Use the function to generate the welcome message & print it using an f-string
    Ensure the program handles empty or invalid names by informing the user & asking for input again
"""
def create_welcome_message(name):
    line_length = 30
    centered_name = name.center(line_length, "*")
    return f"Welcome {centered_name} Welcome"

while True:
    user_name = input("Please enter your name for a personalized welcome message: ")
    if user_name.isalpha():
        welcome_message = create_welcome_message(user_name)
        print(welcome_message)
    else:
        print("Invalid name. Please enter alphabetic characters only.")

    continue_welcome = input("Would you like to create another message? (yes/no): ")
    if continue_welcome != 'yes':
        break

# 6. The Stats Breakdown
"""
You are creating a feature for a sports analytics app that categorizes & displays player statistics
The app takes a single string input of various stats separated by smicolons, where each stat is a category-value pair joined by a colon
The program should print each stat on a new line with its category & value clearly labeled
    Write a function print_stats that takes a string of stats & prints each one on a new line
    Each stat should be presented in the format: Category: [category], Value: [value]
    Use the function to parse the stats & print them in a user friendly manner
    Ensure the program handles invalid formats by informing the user & asking for input again
"""
def print_stats(stats_string):
    stats_list = stats_string.split(';')
    for stat in stats_list:
        category_value = stat.split(':')
        if len(category_value) == 2:
            category, value = category_value
            print(f"Category: {category}, Value: {value}")
        else:
            print(f"Invalid format for stat: {stat}")
            break

while True:
    stats_input = input("Enter your stats separated by semicolons (e.g. Goals:4;Assists:2;Fouls:1): ")
    print_stats(stats_input)

    continue_input = input("Would you like to enter more stats? (yes/no): ").lower()
    if continue_input != "yes":
        break

# 7. THe Name Tag Switcheroo
"""
You are developing a playful feature for a social networking app that allows users to swap the first & last characters of their username
The app takes a username as input & displays the modified version
    Write a function swap_characters that takes a strong & returns a new string with the first & last characters swapped
    Ensure the function handles usernames of any length, including single-character names
    Implement a loop that prompts the user to enter their username
    Use the function to swap the characters & print the result in a fun & engaging way
    Provide the user with the option to try another username or exit the program
"""
def swap_characters(username):
    if len(username) > 1:
        return username[-1] + username[1:-1] + username[0]
    return username

while True:
    username_input = input("Enter your username to see the magic swap: ")
    swapped_username = swap_characters(username_input)

    print(f" Ta-da! Your magical username is {swapped_username} ")

    continue_input = input("Want to try another username? (yes/no): ").lower()
    if continue_input != 'yes':
        break

# 8. The Meeting Agenda Reverser
"""
Imagine you're developing a feature for a meeting management app that allows users to reverse the order of items in their meeting agenda
The app accepts a string representing the agenda items in order & outputs them in reverse order
    Write a function reverse_agenda that takes a string of agenda items & returns a string with the items in reverse order
    Implement a loop that prompts the user to enter their agenda items separated by commas
    Use the function to reverse the order of the agenda items & print the result
    Provide the user with the option to enter a new agenda or exit the program
"""
def reverse_agenda(agenda_string):
    agenda_items = agenda_string.split(', ')
    reversed_agenda = agenda_items[::-1]
    return ','.join(reversed_agenda)

while True:
    user_agenda = input("Enter your meeting agenda items separated by commas: ")
    reversed_order = reverse_agenda(user_agenda)

    print(f" Reversed agenda order: {reversed_order}")

    continue_input = input("Would you like to reverse another agenda? (yes/no): ").lower()
    if continue_input != 'yes':
        break

# 9. The Social Media Post Formatter
"""
In the world of social media, users often like to sylize their posts with unique character replacements
You're tasked with developing a feature for a social media app that allows users to replace every instance of the letter a with @ and e with 3
    Write a function stylize_post tha takes a string & returns a stylized version of it according to the specified replacements
    Implement a loop that prompts the user to enter their post
    Provide the user with the option to stylize a new post or exit the program
"""
def stylize_post(post_string):
    stylized_chars = []
    for char in post_string:
        if char == 'a':
            stylized_chars.append('@')
        elif char == 'e':
            stylized_chars.append('3')
        else:
            stylized_chars.append(char)
    return ''.join(stylized_chars)

while True:
    user_post = input('Enter your social media post: ')
    stylized_post = stylize_post(user_post)

    print(f" Stylized Post: {stylized_post}")

    continue_input = input("Would you like to stylize another post? (yes/no): ").lower()
    if continue_input != 'yes':
        break

# 10. The Customer Repetition Message Generator
"""
In many user interfaces, there's a need to display a message or string repeatedly to grab attention or for esthetic purposes
You are tasked with developing a feature for a user interface toolkit that allows users to repeat a string a specified number of times, with each repetition separated by a dash
    Write a function repeat_message that takes a string & a number as arguments & returns the repeated string pattern
    Implement a loop that prompts the user to enter their message & the number of repetitions
    Use the function to generate the repeated string pattern & print the result
    Provide the user with the option to create a new repeated string pattern or exit the program
"""
def repeat_message(message, times):
    return '-'.join([message] * times)

while True:
    user_message = input('Enter the message you want to repeat: ')
    repeat_count = int(input("How many times would you like to repeat it? "))

    repeated_message = repeat_message(user_message, repeat_count)

    print(f"Repeated message: {repeated_message}")

    continue_input = input("Would you like to create another repeated message? (yes/no): ")
    if continue_input != 'yes':
        break