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
