# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.

famousPeople = ["Nelson Mandela", "Muhammed Ali", "Mike Tyson", "Tom Brady"]

print("Hello, " + famousPeople[0] + " please come to dinner at my home. Thank you!")
print("Hello, " + famousPeople[1] + " please come to dinner at my home. Thank you!")
print("Hello, " + famousPeople[2] + " please come to dinner at my home. Thank you!")
print("Hello, " + famousPeople[3] + " please come to dinner at my home. Thank you!")
print("I'm inviting " + str(len(famousPeople)) + " to dinner")



# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# •	 Start with your program from Exercise 3-4. Add a print() call at the end
# of your program stating the name of the guest who can’t make it.
# •	 Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
# •	 Print a second set of invitation messages, one for each person who is still
# in your list.

print("Unfortunately, " + famousPeople[2] + " is unable to attend.")

famousPeople[2] = "Ray Lewis"

print("Hello, " + famousPeople[0] + " please come to dinner at my home. Thank you!")
print("Hello, " + famousPeople[1] + " please come to dinner at my home. Thank you!")
print("Hello, " + famousPeople[2] + " please come to dinner at my home. Thank you!")
print("Hello, " + famousPeople[3] + " please come to dinner at my home. Thank you!")
print("I'm inviting " + str(len(famousPeople)) + " to dinner")


# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# •	 Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
# call to the end of your program informing people that you found a bigger
# dinner table.
# •	 Use insert() to add one new guest to the beginning of your list.
# •	 Use insert() to add one new guest to the middle of your list.
# •	 Use append() to add one new guest to the end of your list.
# •	 Print a new set of invitation messages, one for each person in your list

print("Hello, I have found a bigger table venue to have more people over. ")

famousPeople.insert(0, 'Kanye West')
famousPeople.insert(2, 'The Weeknd')
famousPeople.append('J. Cole')

print("Hello, " + famousPeople[0] + " please come to dinner at my home. Thank you!")
print("Hello, " + famousPeople[1] + " please come to dinner at my home. Thank you!")
print("Hello, " + famousPeople[2] + " please come to dinner at my home. Thank you!")
print("Hello, " + famousPeople[3] + " please come to dinner at my home. Thank you!")
print("Hello, " + famousPeople[4] + " please come to dinner at my home. Thank you!")
print("Hello, " + famousPeople[5] + " please come to dinner at my home. Thank you!")
print("Hello, " + famousPeople[6] + " please come to dinner at my home. Thank you!")
print("I'm inviting " + str(len(famousPeople)) + " to dinner")


# 3.7 Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
# •	 Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# •	 Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.
# •	 Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# •	 Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.

print("Hello, only two people are able to attend the dinner. Sorry.")

removedGuest = famousPeople.pop(0)
print("Hello, " + removedGuest + ". I'm sorry but I am unable to invite you to dinner.")

removedGuest = famousPeople.pop(1)
print("Hello, " + removedGuest + ". I'm sorry but I am unable to invite you to dinner.")

removedGuest = famousPeople.pop(3)
print("Hello, " + removedGuest + ". I'm sorry but I am unable to invite you to dinner.")

removedGuest = famousPeople.pop(1)
print("Hello, " + removedGuest + ". I'm sorry but I am unable to invite you to dinner.")

removedGuest = famousPeople.pop(2)
print("Hello, " + removedGuest + ". I'm sorry but I am unable to invite you to dinner.")

print("Hello, " + famousPeople[0] + " and " + famousPeople[1] + ". I have invited both of you to dinner. Thank you!")
print("I'm inviting " + str(len(famousPeople)) + " to dinner")


del famousPeople[1]
del famousPeople[0]

print(famousPeople)
