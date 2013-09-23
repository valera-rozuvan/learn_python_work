"""
    7.2 Reading and writing files.

    http://docs.python.org/2/tutorial/inputoutput.html
"""

WRITE_MODE = 'w'

# open() returns a file object, and is most commonly used with two arguments:
#
#     open(filename, mode)
#
# The first argument is a string containing the filename. The second argument
# is another string containing a few characters describing the way in which the
# file will be used.

f = open('workfile.txt', WRITE_MODE)
print f

# When you are done with a file, call close() to close it and free up any
# system resources taken up by the open file. After calling close(), attempts
# to use the file object will automatically fail.
f.close()
