# To slice, you specify where you want to start and end your cut. The magic of Python ensures that the start is inclusive, but the end remains elusive, always one step ahead.
hobbies = ["reading", "painting", "cycling", "singing", "dancing"]
print(hobbies)

"""
When you use slicing, the colon : acts as a separator, marking the beginning & the end of your journey through the list. 

Start Point: The number before the colon represents where you wish to begin your journey. If you leave it empty the journey starts from the very first item.

End Point: THe number after the colon signifies where you wish to end. 
However, this point remains just out of reach, making the journey stop just before it. If you leave it empty the journey continues till the very last items. 
"""

segment = hobbies[1:3] # This extracts painting & cycling
print(segment)

beginning_to_third = hobbies[:3] # This unveils reading, painting, cycling
print(beginning_to_third)

third_to_end = hobbies[2:] # This reveals cycling, singing, dancing
print(third_to_end)

