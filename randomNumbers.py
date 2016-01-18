# Let's learn a little bit of Data Analysis and how we can use
# loops and lists to create, aggregate, and summarize data

# For the part 1, we'll learn a basic way of creating data using
# Python's random number generator.

# To create a random integer from 0 to 10, we first import the
# "random" module

import random

# We then print a random integer using the random.randint(start, end) function

print "Random number generated: " + str(random.randint(0,10))

# Remember that if we want to concatenate a string and a number, we need to
# convert the integer into a string using the str() function

# We now want to create a list filled with random numbers. The list should be
# of length 20

random_list = []
list_length = 20

# Write code here and use a while loop to populate this list of random integers.
# A crucial function that will help you is to use the append() method to add
# elements to a list.

while len(random_list) < list_length:
    randomNumber = random.randint(0,10)
    random_list.append(randomNumber)

# Write code here to loop through the list and count all occurrences
# of the number 9. If statements and while loops will help solve
# this problem.

count = 0
for x in random_list:
    if x == 9:
        count += 1

# Initialize count_list for every integer between 0 and 10.
# A number will correspond to an index of this count_list. Therefore,
# if we see that there are 3 occurrences of the number 4, we assign
# count_list[4] = 3, if there are 5 occurrences of the number 6, we assign
# count_list[6] = 5.

# We can multiply a list construct to create a list with the same elements
# n number of times. This creates a list of zeros, with a length of 11.
# (Aggregate the data)
count_list = [0] * 11

# Write code here to loop through every number in random_list and update
# count_list appropriately.
for x in random_list:
    count_list[x] = count_list[x] + 1

# Write code here to summarize count_list and print a neatly formatted table
# that looks this:
"""
number | occurrence
     0 | 1
     1 | 2
     2 | 3
     3 | 2
     4 | 2
     5 | 1
     6 | 1
     7 | 2
     8 | 3
     9 | 1
    10 | 2
"""

# Build the tables with for loops so the length and random numbers can change.
# This is a "distribution table" or "histogram."
value = 0
print "number | occurrence"

for x in count_list:
    if value < 10:
        print "     " + str(value) + " | " + str(x)
    else:
        print "    " + str(value) + " | " + str(x)
    value += 1

print

value = 0
print "number | occurrence"

for x in count_list:
    if value < 10:
        print "     " + str(value) + " | " + "*" * x
    else:
        print "    " + str(value) + " | " + "*" * x
    value += 1

# When we print this list, we should get a list of random integers such as:
# [7, 5, 1, 6, 4, 1, 0, 6, 6, 8, 1, 1, 2, 7, 5, 10, 7, 8, 1, 3]

print
print random_list
print "String length = " + str(len(random_list))
print "Occurrences of the number 9: " + str(count)
print
print random_list
print count_list
print sum(count_list) # Sum should be 20
