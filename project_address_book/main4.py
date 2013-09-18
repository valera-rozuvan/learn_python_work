# This is based on https://github.com/adambard/learnxinyminutes-docs/blob/master/python.html.markdown
# Main project site: http://learnxinyminutes.com/


# Single line comments start with a hash.
""" Multiline strings can be written
    using three "'s, and are often used
    as comments.
"""

##################################################
## 1. Primitive Datatypes and Operators
##################################################

# You have numbers.
3  # => 3

# Math is what you would expect.
1 + 1  # => 2
8 - 1  # => 7
10 * 2  # => 20
35 / 5  # => 7

# Division is a bit tricky. It is integer division and floors the rsult
# automatically.
5 / 2  # => 2

# To fix division we need to learn about floats.
2.0  # This is a float.
11.0 / 4.0  # => 2.75  ahhh ... much better.

# Enforce precedence with parentheses
(1 + 3) * 2  # => 8

# Boolean values are primitives.
True
False

# Negate with "not".
not True  # => False
not False  # => True

# Equality is "==".
1 == 1  # => True
2 == 1  # => False

# Inequality is "!=".
1 != 1  # => False
2 != 1  # => True

# More comparisons.
1 < 10  # => True
1 > 10  # => False
2 <= 2  # => True
2 >= 2  # => True

# Comparisons can be chained.
1 < 2 < 3  # => True
2 < 3 < 1  # => False

# Strings can be created with " or '
"This is a string."
'This is also a string.'

# Strings can be added too!
"Hello " + "worlds!"  # => "Hello, world!"

# A string can be treated like a list of characters.
"This is a string."[0]  # => 'T'

# % can be used to format strings, like this:
"%s can be %s" % ("strings", "interpolated")

# A newer way to format strings is the format method.
# This method is the preferred way.
"{0} can be {1}".format("strings", "formatted")
# You can use keywords if you don't want to count.
"{name} wants to eat {food}".format(name="Bob", food="lasagna")

# None is an object.
None  # => None

# Don't use the equality "==" symbol to compare objects to None.
# Use "is" operator instead.
"etc" is None  # => False
None is None   # => True

# The "is" operator tests for object identity. This isn't very
# useful when dealing with primitive values, but is very useful
# when dealing with objects.

# None, 0, and empty strings/lits all evaluate to False.
# All other values are True.
0 == False  # => True
"" == False  # => True


##################################################
## 2. Variables and Collections
##################################################

# Printing is pretty easy.
print "I'm Python. Nice to meet you!"

# No need to declare variables before assigning to them.
some_var = 5  # Convention is to use lower_case_with_underscore.

try:
    # Accessing a previously unassigned variable is an exception.
    # See Control Flow to leatn more about exception handling.
    some_other_var  # => Raises a name error.
except NameError as err:
    # pass  # Pass is just a no-op. Usually you would do recovery here.
    print "Custom ERROR: 'some_other_var' is not defined."

# If can be used as an expression.
"yahoo!" if 3 > 2 else 2  # => "yahoo!"


# == Lists ==

#Lists store sequences.
li = []
# You can start with a prefilled list.
other_li = [4, 5, 6]

# Add stuff to the end of the list with append.
li.append(1)  # li is now [1]
li.append(2)  # li is now [1, 2]
li.append(4)  # li is now [1, 2, 4]
li.append(3)  # li is now [1, 2, 4, 3]
# Remove from the end with pop().
li.pop()  # => 3, and li is now [1, 2, 4]
# Let's put it back.
li.append(3)  # li is now [1, 2, 4, 3]

# Access a list like you would any array.
li[0]  # => 1
# Look at the last element.
li[-1]  # => 3

try:
    # Looking out of bounds is an IndexError.
    li[4]  # Raises an IndexError.
except IndexError as err:
    # pass  # Pass is just a no-op. Usually you would do recovery here.
    print "Custom ERROR: 'li[4]' - list index out of range."

# You can look at ranges with slice syntax.
# (It's a closed/open range for you mathy types.)
li[1:3]  # => [2, 4]
# Omit the beginning.
li[2:]  # => [4, 3]
# Omit the end.
li[:3]  # => [1, 2, 4]

# Remove arbitrary elements from a list with "del".
del li[2]  # li is now [1, 2, 3]

# You can add lists.
li + other_li  # => [1, 2, 3, 4, 5, 6] - Note: li and other_li is left alone.

# Concatenate lists with "extend()".
li.extend(other_li)  # => Now li is [1, 2, 3, 4, 5, 6]

# Check for existence in a list with "in".
1 in li  # => True

# Examine the length with "len()".
len(li)  # => 6


# == Tuples ==

# Tuples are like lists but are immutable.
# Note: immutable - unchanging over time or unable to be changed.
tup = (1, 2, 3)
tup[0]  # => 1

try:
    tup[0] = 3  # => Raises a TypeError
except TypeError as err:
    # pass  # Pass is just a no-op. Usually you would do recovery here.
    print """Custom ERROR: 'tup[0] = 3' - 'tuple' object does not support \
item assignment."""

# You can do all those list thingies on tuples too.
len(tup)  # => 3
tup + (4, 5, 6)  # => (1, 2, 3, 4, 5, 6)
tup[:2]  # => (1, 2)
2 in tup  # => True

# You can unpack tuples (or lists) into variables.
a, b, c = (1, 2, 3)  # a is now 1, b is now 2, and c is now 3.
# Tuples are created by default if you leave out the parentheses.
d, e, f = 4, 5, 6
# Now look how easy it is to swap two values.
e, d = d, e  # d is now 5 and e is now 4.


# == Dictionaries ==

# Dictionaries store mappings.
empty_dict = {}
# Here is a prefilled dictionary.
filled_dict = {"one": 1, "two": 2, "three": 3}

# Look up values with [].
filled_dict["one"]  # => 1

# Get all keys as list with "keys()".
filled_dict.keys()  # => ["three", "two", "one"]
# Note: dictionary key ordering is not guaranteed.
# Your results might now match this exactly.

# Get all values as a list with "values()".
filled_dict.values()  # => [3, 2, 1]
# Note: same as above regarding key ordering.

# Check for existence of keys in a dictionary with "in".
"one" in filled_dict  # => True
1 in filled_dict  # => False

try:
    # Looking up a non-existent key is a KeyError.
    filled_dict["four"]
except KeyError as err:
    print """Custom ERROR: filled_dict["four"] - non-existent key!"""

# Use "get()" method to avoid the KeyError.
filled_dict.get("one")  # => 1
filled_dict.get("four")  # => None
# The get method supports a default argument when the value is missing.
filled_dict.get("one", 4)  # => 1
filled_dict.get("four", 4)  # => 4

# "setdefault()" method is a safe way to add new key-value pair into
# a dictionary.
filled_dict.setdefault("five", 5)  # filled_dict["five"] is set to 5 when it's
                                   # value is not set.
filled_dict.setdefault("five", 6)  # filled_dict["five"] is still 5.


# == Sets store ... well sets ==
empty_set = set()
# Initialize a "set()" with a bunch of values.
some_set = set([1, 2, 2, 3, 4])  # => some_set is now set([1, 2, 3, 4])

# Since Python 2.7, {} can be used to declare a set.
filled_set = {1, 2, 2, 3, 4}  # => {1, 2, 3, 4}

# Add more items to a set.
filled_set.add(5)  # => filled_set is now {1, 2, 3, 4, 5}

# Do set intersection with "&".
other_set = {3, 4, 5, 6}
filled_set & other_set  # => {13, 4, 5}

# Do set union with "|".
filled_set | other_set  # => {1, 2, 3, 4, 5, 6}

# Do set difference with "-".
{1, 2, 3, 4} - {2, 3, 5}  # => {1, 4}

# Check for existence in a set with in.
2 in filled_set  # => True
10 in filled_set  # => False
