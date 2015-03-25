# Here is a chance to play around with lists for a bit before you continue.
# Take a look at what the following code does and try and guess how it works.

print "EXAMPLE 1: Lists can contain strings"
string_list = ['HTML', 'CSS', 'Python']
print string_list

print "EXAMPLE 2: Lists can contain numbers"
number_list = [3.14159, 2.71828, 1.61803]
print number_list

print "EXAMPLE 3: Lists can be 'accessed' and 'sliced' like strings in previous lessons"
pi = number_list[0]
not_pi = number_list[1:]
print pi
print not_pi

print "EXAMPLE 4: Lists can contain strings AND numbers"
mixed_list = ['Hello!', 42, 'Goodbye!']
print mixed_list

print "EXAMPLE 5: Lists can even contain other lists"
lists_with_lists = [3, 'colors', ['red', 'green', 'blue'], 'your favorite?']
print lists_with_lists



# Structured Data: Lists and For Loops -> Stooges

# Define a variable, stooges, whose value is a list of the names of the Three
# Stooges: 'Moe', 'Larry' & 'Curly'.

stooges = ['Moe', 'Larry', 'Curly']



# Structured Data: Lists and For Loops -> Days in a Month

# Given the variable;

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# define a procedure, how_many_days, that takes as input a number representing
# a month, and returns the number of days in that month.

def how_many_days(month_number):
	return days_in_month[month_number - 1]

print how_many_days(1)
print how_many_days(9)



# Structured Data: Lists and For Loops -> Play with Nested Lists

# Every entry in the following list is itself a list

nested_list = [['HTML', 'Hypertext Markup Language forms the structure of webpages'],
				['CSS', 'Cascading Style Sheets give pages style'],
				['Python', 'Python is a programming language'],
				['Lists', 'Lists are a data structure that let you organize information']]

first_concept = nested_list[0]

print "What do you think this will print?"
print first_concept
print

print "Since first_concept was itself a list, we can access its elements."
first_title = first_concept[0]
first_description = first_concept[1]
print

print "What will this print?"
print first_title
print first_description
print



# Structured Data: Lists and For Loops -> Countries

# Given the variable 'countries' defined below:

#				Name   Capital    Population (millions)

countries = [['China', 'Beiging', 1350],
			 ['India', 'Delhi', 1210],
			 ['Romania', 'Bucharest', 21],
			 ['United States', 'Washington', 307]]

# Write code to print out the capital of India by accessing the list

print countries[1][1]
print

# What multiple of Romania's population is the population of China?
# Calculate this by accessing the list and dividing the population of
# China (1350) by the population of Romania (21). Please print your result.

print (countries[0][2]) / (countries[2][2])
print



# Structured Data: Lists and For Loops -> Different Stooges

# We defined 'stooges', see above. But, in some Stooges files, Curly
# was replaced by Shemp.

# Write one line of code that changes the vaule of stooges to be:
# ['Moe', 'Larry', 'Shemp'], but does not create a new list object.

# This is an example of 'mutation'. We are actually changing the list
# object itself, not creating a new one - which would be the behavior of
# a string.

stooges[2] = 'Shemp'
print stooges
print



# Structured Data: Lists and For Loops -> Secret Agent Man

# What is the value of 'agent[2]' after the following code runs:

spy = [0,0,7]
agent = spy
spy[2] = agent[2] +1

print agent[2]
print agent, spy
print



# Structured Data: Lists and For Loops -> Replace Spy

# Define a procedure, replace_spy, that takes as its input a list of three
# numbers, and modifies the value of the third element in the input list
# to be one more than its previous value.

spy = [0,0,7]

def replace_spy(p):
	p[2] = p[2] + 1 # notice no return statement. 'p' and 'spy' point to the same list.

# In the test below, the first line calls your procedure which will change spy,
# and the second checks you have changed it. Uncomment the two lines below.

replace_spy(spy)
print spy
print



# Structured Data: Lists and For Loops -> Len Quiz

# What is the value of 'len(p)' after running this code:

p = [1,2]
p.append(3)
p = p + [4,5]
print len(p) # answer is 5

print

# What is the value of 'len(p)' after running this code:

p = [1,2]
q = [3,4]
p.append(q)
print len(p) # answer is 3
print p

print