# Try Block: Consider the try block as your proactive measure. It’s the section of your code where you anticipate things might go awry & you plan accordingly. 
try:
    # code that might cause an exception
    user_input = int(input("Enter a number: "))
except ValueError:
# code to handle the exception
    print("Oops! That was not a valid number. Try again....")

# Think of using multiple except blocks, each section is for a different type of problem, just like each except block handles a different kind of error.

try:
    # code that might cause multiple exceptions
    number = int(input("Enter a number: "))
    result = 100 / number
except ValueError:
    # code to handle incorrect input type
    print("Please enter a valid integer")
except ZeroDivisionError:
    # code to handle division by zero
    print("Sorry, infinity is not on the menu today. Try a non-zero number")

# Except Block: Sometimes, you’re not sure what might go wrong & that's when a general purpose tool comes in handy. 
# A broad except block catches any exception that wasn’t specifically caught by earlier blocks.
def perform_complex_calculation(data):
    # simulating a complex calculation that might result in various exceptions
    result = 0
    for item in data:
        result += item ** 2
    average = result / len(data)
    return average

# handling exceptions
try:
    # code that might cause an unexpected exception
    data = [1, 2, 'a', 4]
    calculation_result = perform_complex_calculation(data)
except (ValueError, ZeroDivisionError):
    # code to handle known potential issues
    print("Please provide a list of numbers and ensure it's not empty")
except Exception as e:
    # code to handle an unexpected exception
    print(f"An unexpected error occured: {e}")

# Raising an exception is like sending up a flare for help when you’ve encountered a situation that your current code isn’t equipped to handle. 
# Raising an exception is a deliberate action. 
# You do it when you detect that something has gone so off-course that the best course of action is to stop & signal for help, rather than trying to limp along. 
# It’s a way to say, here's a problem I can't or shouldn't try to solve myself, and it's better to alert someone else that they need to take care of it. 
# You raise an exception with the raise keyword. 
fuel_input = -1
if fuel_input < 0:
    raise ValueError("Fuel level cannot be negative")

# Sometimes, the standard set of exceptions doesn’t quite fit the error you’re encountering. In these cases, you can define your own exceptions. 
fuel_level = 10
tank_capacity = 9

class FuelTankOverflowError(Exception):
    """Exception raised when the fuel tank is overfilled."""
    pass

if fuel_level > tank_capacity:
    raise FuelTankOverflowError("Fuel has exceeded the tank capacity")



