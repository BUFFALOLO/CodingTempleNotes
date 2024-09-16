# ADDITION
strawberries = 10
blueberries = 5
mixed_fruits = strawberries + blueberries
print(mixed_fruits)

# SUBTRACTION
initial_cheese_slice = 5
cheese_used = 2
cheese_left = initial_cheese_slice - cheese_used
print(cheese_left)

# MULTIPLICATION
pizza_slices_per_person = 2
party_guests = 5
total_slices_needed = pizza_slices_per_person * party_guests
print(total_slices_needed)

# DIVISION
pie_pieces = 8
people_at_table = 4
pieces_per_person = pie_pieces / people_at_table
print(pieces_per_person)

# MODULUS
cookies = 14
cookies_per_jar = 5
outside_jar = cookies % cookies_per_jar
print(outside_jar)

# FLOOR DIVISION
total_sandwiches = 7
people = 3
sandwiches_each = total_sandwiches // people
print(sandwiches_each)

# EXPONENTIATION
tea_strength = 2
cups_of_tea = tea_strength **2
print(cups_of_tea)

# EXERCISES
# 1. The Baker's Dilemma: If one cake requires 250 grams of flour & you have 2.5 kilograms of flour, how many cakes can you make using the arthmetic operators?
flour_per_cake = 250
total_flour = 2.5 * 1000
number_of_cakes = total_flour // flour_per_cake
print(number_of_cakes)

# 2. Claiming Territories: Use the assignment operator to claim a variable kingdom with a value of "Pythonland"
kingdom = "Pythonland"

# 3. Fashion Contest: Given two shirts with prices shirt1 = 45 and shirt2 = 50, use a comparison operator to check if shirt1 is cheaper than shirt2.
shirt1 = 45
shirt2 = 50
result = shirt1 < shirt2
print(result)
# If shirt1 is less than shirt2 it will print True

# 4. Rainy Day Dilemma: Write a logical operation to determine if you should take an umbrella if it's either going to rain or going to rain heavily.
rain = True
heavy_rain = False
take_umbrella = rain or heavy_rain
print(take_umbrella)
# OR is looking for either rain or heavy_rain to be true. As long as one of them is True it will print True

# 5. Royal Order: Evaluate the expression 3 + 5 * 2 - 8. What would be the order of operations?
evaluation = 3 + 5 * 2 - 8
print(evaluation)
# Multiplication takes predescence so its does 5 * 2 first which is 10, it then adds the 3 which is 13 then minuses the 8 which equals 5

# 6. The Pastry Fractions: You have 10 pastries and you want to divide them equally among 3 friends. How many pastries does each friend get and how many are left?
pastries = 10
friends = 3
pastries_each = pastries // friends
left_over = pastries % friends
print(pastries_each, left_over)

# 7. Kingdom Expansion: You already have a kingdom names Pythonland. Use the assignment operator to add "is wonderful!" to it.
print(kingdom + " is wonderful!")

kingdom += " is wonderful!"
print(kingdom)

# 8. Royal Duel: Two knights have strength values of kinight1 = 45 and kight2 = 50. Use a comparison operator to determine if knight1 has the same strength as knight2
knight1 = 45
knight2 = 50
knight_strength = knight1 == knight2
print(knight_strength)

# 9. Chef's Special: A chef has two ingredients eggs = True and flour = False. He can only make pancakes if he has both. Determine if the chef can make pancakes.
eggs = True
flour = False
make_pancakes = eggs and flour
print(make_pancakes)

# 10. Medieval Architecture: A castle's height is 100 units & its moat's width is 50 units. If you double the castle's height & have the moat's width, what would be the new dimensions?
castle_height = 100
moat_width = 50
castle_height *= 2
moat_width /= 2
print(castle_height, moat_width)