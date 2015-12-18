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
print p

print

# What is the value of 'len(p)' after running this code:

p = [1,2]
q = [3,4]
p.append(q)
print len(p) # answer is 3
print p

print

# Try and figure out what the following examples will do.

print "EXAMPLE 1: We can use for loops to go through a list of strings:"
example_list_1 = ['a', 'b', 'c', 'd']

for thing in example_list_1:
	print thing

print

print "EXAMPLE 2: We can use for loops on nested lists too:"
example_list_2 = [['China', 'Beijing'],
					['USA', 'Washington D.C.'],
					['India', 'Delhi']]

for country_with_capital in example_list_2:
	country = country_with_capital[0]
	capital = country_with_capital[1]
	print capital + ' is the captial of ' + country

print

# Sum List Quiz

# Define a procedure, sum_list, that takes as its input a list of numbers,
# and returns the sum of all the elements in the input list.

def sum_list(numbersList):
	sumTotal = 0
	for x in numbersList:
		sumTotal += x

	return sumTotal

print sum_list([1, 7, 4])
print sum_list([9, 4, 10])
print sum_list([44, 14, 76])
print sum_list([])

print

# Measure Udacity Quiz

# Define a procedure, measure_udacity, that takes as its input a list of
# strings, and returns a number that is a count of the number of elements
# in the input list that start with the uppercase letter 'U'.

def measure_udacity(stringsList):
	count = 0
	for x in stringsList:
		if x[0] == 'U':
			count += 1

	return count

print measure_udacity(['Dave', 'Sebastian', 'Katy'])
print measure_udacity(['Umika', 'Umberta'])
print measure_udacity([])

print

# Find Element Quiz

# Define a procedure, find_element, that takes as its inputs a list and a
# value of any type, and returns the index of the frist element in the input
# list that matches the value. If there is no matching element, return -1.

def find_element(list, element):
	count = 0
	for x in list:
		if x == element:
			return count
		else:
			count += 1

	return -1

print find_element([1, 2, 3], 3)
print find_element(['alpha', 'beta'], 'gamma')

print

# Find Element with Index Quiz

# Define a procedure, find_element, using index that takes as its inputs a list
# and a value of any type, and returns the index of the first element in the
# input list that matches the value. If there is no matching element,
# return -1.

def find_element2(list, element):
	if element in list:
		return list.index(element)
	else:
		return -1

print find_element2([1, 2, 3], 3)
print find_element2(['alpha', 'beta'], 'gamma')

print

# -or- using 'not in'

def find_element3(list, element):
	if element not in list:
		return -1
	else:
		return list.index(element)

print find_element3([1, 2, 3], 3)
print find_element3(['alpha', 'beta'], 'gamma')
