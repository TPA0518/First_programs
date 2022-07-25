# 3-8. Seeing the World: Think of at least five places in the world you’d like to
# visit.
# •	 Store the locations in a list. Make sure the list is not in alphabetical order.
# •	 Print your list in its original order. Don’t worry about printing the list neatly,
# just print it as a raw Python list.
# •	 Use sorted() to print your list in alphabetical order without modifying the
# actual list.
# •	 Show that your list is still in its original order by printing it.
# •	 Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
# •	 Show that your list is still in its original order by printing it again.
# •	 Use reverse() to change the order of your list. Print the list to show that its
# order has changed.
# •	 Use reverse() to change the order of your list again. Print the list to show
# it’s back to its original order.
# •	 Use sort() to change your list so it’s stored in alphabetical order. Print the
# list to show that its order has been changed.
# •	 Use sort() to change your list so it’s stored in reverse alphabetical order.
# Print the list to show that its order has changed.

vacationPlaces = ['Cancun', 'Caribbean', 'Greece', 'Japan', 'India']
print(vacationPlaces)
print(sorted(vacationPlaces))
print(vacationPlaces)
print(sorted(vacationPlaces, reverse=True))
print(vacationPlaces)
vacationPlaces.reverse()
print(vacationPlaces)
vacationPlaces.reverse()
print(vacationPlaces)
vacationPlaces.sort()
print(vacationPlaces)
vacationPlaces.sort(reverse=True)
print(vacationPlaces)
# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
# through 3-7 (page 42), use len() to print a message indicating the number
# of people you are inviting to dinner.


# 3-10. Every Function: Think of something you could store in a list. For example,
# you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like.
# Write a program that creates a list containing these items
# and then uses each function introduced in this chapter at least once.

countriesList = ['USA', 'Canada', 'Mexico', 'China', 'India', 'Russia', 'France', 'Dominican Republic']
print(countriesList)
countriesList.append('Brazil')
print(countriesList)
countriesList.insert(4, 'Germany')
print(countriesList)
del countriesList[6]
print(countriesList)
popCountry = countriesList.pop(2)
print(countriesList)
countriesList.remove('China')
print(countriesList)
print(sorted(countriesList))
print(sorted(countriesList, reverse=True))
countriesList.sort()
print(countriesList)
countriesList.reverse()
print(countriesList)
print(len(countriesList))
