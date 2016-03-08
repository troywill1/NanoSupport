# Lesson 3.3c: Use Classes
# Mini-Project: Check Profanity - Built-in Python Functions

# Using the documentation for Built-in Funcitons in the Python Standard
# Library, choose a function and write a program using it.

# I used cmp() and str()

def compare(a,b):
    result = cmp(a,b)

    if result < 0:
        print str(a) + " is less than " + str(b) + " (result = " + str(result) + ")"
    elif result > 0:
        print str(a) + " is greater than " + str(b) + " (result = " + str(result) + ")"
    else:
        print str(a) + " is equivalent to " + str(b) + " (result = " + str(result) + ")"

compare(4,6)
compare(345,56)
compare(32,32)
