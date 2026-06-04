# Detailed Summary:This code manages a guest list for an annual dinner celebration. 
# It starts with an initial list of guests and prints out personalized invitations for each guest. 
# Then, it simulates a situation where one guest (Nikola Tesla) cannot attend, 
# and updates the guest list accordingly by removing him and adding Julius Caesar. 
# The updated guest list is printed again. The code then simulates finding a larger venue, allowing for more guests to be invited. 
# It adds Michael Jackson, Ada Lovelace, and Galileo Galilei to the guest list and prints the updated list again. 
# Finally, it simulates a situation where only two guests can be invited, and removes guests from the list until only two remain, 
# printing a message for each removed guest. 
# The final guest list is printed, and then all guests are removed from the list, leaving it empty.
guests = ["Albert Einstein", "Lady Gaga", "Isaac Newton", "Nikola Tesla", "Michael Jordan", "Leonardo da Vinci", "William Shakespeare", "Cleopatra"]

print("Guest list:\n")

for guest in guests:
    print(f"Dear {guest}, you are hereby officially invited to an annual dinner celebration.")

print("\nUnfortunately, due to unforeseen circumstances, a member of the guest list cannot attend the dinner. We regret to inform you that Nikola Tesla will not be able to join us for the event.\n")

guests.remove("Nikola Tesla")
guests.append("Julius Caesar")

print("Updated guest list:\n")

for guest in guests:
    print(f"Dear {guest}, you are hereby officially invited to an annual dinner celebration.")


print("\nWe are please to announce that we have found a larger venue for the dinner, which means we can invite more guests!")

guests.insert(0, "Michael Jackson")
guests.append("Ada Lovelace")
guests.insert(len(guests) // 2, "Galileo Galilei")

print("\nUpdated guest list:\n")

for guest in guests:
    print(f"Dear {guest}, you are hereby officially invited to an annual dinner celebration.")

print(f"\nNumber of guests invited: {len(guests)}")
print("\nUnfortunately, due to unforeseen circumstances, we can only invite two guests to the dinner.")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Dear {removed_guest}, we regret to inform you that you will not be able to attend the dinner.")

print("\nFinal guest list:\n")

for guest in guests:
    print(f"Dear {guest}, you are hereby officially invited to an annual dinner celebration.")

while guests:
    del guests[0]

print(guests)