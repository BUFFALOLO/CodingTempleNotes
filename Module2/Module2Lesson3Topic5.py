"""
Ever notice how the best party planners always seem to know who’s dancing to the beat, & who's at the bar? 
The in operator is just like that, always aware of what's happening within a collection.
Think of our guest_list as the dance floor. When “Alice” pops up with her iconic dance movies, the in operator (our party planner) instantly knows she's there. 
But, “Dana”? She's currently at the snack bar - not our dance floor.
"""
guest_list = ["Alice", "Bob", "Charlie"]
print("Alice" in guest_list) # Outputs: True
print("Dana" in guest_list) # Outputs: False

"""
On the flip side, the not in operator keeps tabs on who's taking a break from the dance floor. 
Imagine Dana, taking a brief break from dancing, opting for a quick snack. 
The not in operator, akin to a bartender, immediately recognizes she's not currently on the dance floor but enjoying her time at the bar. 
"""

print("Dana" not in guest_list) # Outputs: True

