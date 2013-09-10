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
