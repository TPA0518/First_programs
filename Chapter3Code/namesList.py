# Names: Store the names of a few of your friends in a list called names. Print
# each person’s name by accessing each element in the list, one at a time

myFriendsList = ['Sam', 'Anand', 'Gohar', 'Shamar']
print(myFriendsList[0])
print(myFriendsList[1])
print(myFriendsList[2])
print(myFriendsList[3])

# Greetings:Start with the list you used in Exercise 3-1, but instead of just
# printing each person’s name, print a message to them. The text of each message
# should be the same, but each message should be personalized with the person’s name.
message = "This is my friend "

print(message + myFriendsList[0] + ".")
print(message + myFriendsList[1] + ".")
print(message + myFriendsList[2] + ".")
print(message + myFriendsList[3] + ".")

# 3-3. Your Own List: Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples. Use your list
# to print a series of statements about these items, such as “I would like to own a
# Honda motorcycle.”

carList = ['BMW', 'Mercedes', 'Honda', 'Toyota', 'Nissan']
message = "I would like to own a "
print(message + carList[0] + " 4-door car.")
print(message + carList[1] + " 4-door car.")
print(message + carList[2] + " 4-door car.")
print(message + carList[3] + " 4-door car.")
print(message + carList[4] + " 4-door car.")

carList.sort()
print(carList)
carList.sort(reverse=True)
print(carList)

print(sorted(carList))
secCarlist = ['BMW', 'Mercedes', 'Honda', 'Toyota', 'Nissan']
secCarlist.reverse()
print(secCarlist)
print(len(secCarlist))