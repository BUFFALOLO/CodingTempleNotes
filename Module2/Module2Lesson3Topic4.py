"""
When someone claims to be a VIP, the bouncer doesn't just look at their attire or what they say; they verify the name on the list.
Imagine guest_2 as a celebrity's official plus-one - they enter the party under the celebrity's (guest_1) invitation. 
On the other hand, guest_3 might look like the celebrity & dress like the celebrity but is an entirely separate individual
"""

guest_1 = [1, 2, 3]
guest_2 = guest_1
guest_3 = [1, 2, 3]

print(guest_1 is guest_2) # Outputs: True
print(guest_1 is guest_3) # Outputs: False

"""
While it confirms VIPs, this does not ensure party crashers are identified & not allowed to join the festivities. 
Picture two people arriving at the party in identical outfits. 
The bouncer (identity operator) checks their IDs.  
Even if they look the same, if they aren't the same person, one might be our uninvited party crasher
"""

party_crasher = [4, 5, 6]
guest_4 = [4, 5, 6]
print(party_crasher is not guest_4) # Outputs: True

