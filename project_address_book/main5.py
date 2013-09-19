# Taken from https://github.com/thehackerwithin/PyTrieste/wiki/Python2-ListsDictsSetsTuples

# Python 2: Lists, Dictionaries, Sets, Tuples
# Presented By : Tommy Guy
# Based on lecture materials by Milad Fatenejad


# ----------- Lists -----------

# Most languages have some kind of simple syntax for making lists of things.
# In Python it is extremely easy and intuitive to make a list of things, for
# example:
mylist = []  # Make an empty list.
mylist = [
    1, 1.0 + 3j, "aperitivo", True
]  # Make a list containing four entities.

# Using lists is easy and intuitive. Notice that lits can contain objects of
# any data type. Try the following:
mylist = [1, 2, 3, 4]
mylist[2] = 1.0 + 2j  # Modify an element.
mylist.append("test")  # Add an element to the end of the list.
print len(mylist)  # Print the length of mylist (5)
