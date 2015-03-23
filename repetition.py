# Decisions and Repitition: Equality Comparisons

print 2 < 3
print 21 < 3
print 7 * 3 < 21

print 7 * 3 != 21
print 7 * 3 == 21 # '=' means assignment, '==' mean equality

# Decisions and Repitition: Decision Making Playground

print "Example 1: Greater-than and less-than comparisons"
print 2 > 1
print 1 > 2
print 5 < 20
print 100 < 19

print "Example 2: Equality and non-equality comparisons"
print 5 == 5
print "hello" == "hello"
print 5 == 10
print 5 == '5' # What do you think will happen here?
print 7 != 10
print 7 != 7

print "Example 3: A demo of what you are about to learn"
if 3 < 5:
	print "Three is definitely smaller than 5!"

if 10 > 20:
	print "Did you know that 10 is greater than 20!?"
else:
	print "20 is greater than 10"

# Decisions and Repitition: If Statements

def absolute(x):
	if x < 0:
		x = -x
	return x

print absolute(10)
print absolute(-10)

# Define a procedure, bigger, that takes in two numbers
# as inputs, and returns the greater of the two inputs.

def bigger(x,y):
	if x > y:
		return x
	else:
		return y

print bigger(2,7)
print bigger(3,2)
print bigger(3,3)

# Decisions and Repitition: Is Friend

# Define a procedure, is_friend, that takes a string as
# its input, and returns a Boolean indicating  if the 
# input string is the name of a friend. Assume I am friends
# with everyone whose name starts with 'D' and no one else.
# You do not need to check for the lowercase 'd'.

def is_friend(friend):
	if friend[0] == 'D':
		return True # Boolean value, not string
	else:
		return False # Boolean value, not string

print is_friend('Diane')
print is_friend('Fred')

# Or, an easier way:

def is_friend2(name):
	return name[0] == 'D' # The result of this evaluation is a Boolean

print is_friend2('Diane')
print is_friend2('Fred')

# Decisions and Repitition: More Friends

# Define a procedure, is_friend, that takes a string as
# its input, and returns a Boolean indicating  if the 
# input string is the name of a friend. Assume I am friends
# with everyone whose name starts with 'D' or 'N' and no one else.
# You do not need to check for the lowercase 'd' or 'n.

def is_friend3(name):
	if name[0] == 'D':
		return True
	elif name[0] == 'N':
		return True
	else:
		return False

print is_friend3('Diane')
print is_friend3('Ned')
print is_friend3('Moe')

# Or, an easier way:

def is_friend4(name):
	return name[0] == 'D' or name[0] == 'N' # logical 'or' operator

print is_friend4('Doug')
print is_friend4('Nicole')
print is_friend4('Fred')

print True or False
print False or True
print True or True
print False or False
print True or this_is_an_error # 'or' only evaluate what it needs to, this will not produce an error

# Define a procedure, biggest, that takes three numbers as
# inputs and returns the largest of those three numbers.

def biggest(x,y,z):
	if (x >= y) and (x >= z):
		return x
	if (y >= x) and (y >= z):
		return y
	else:
		return z

print biggest(3, 6, 9)
print biggest(6, 9, 3)
print biggest(9, 3, 6)
print biggest(3, 3, 9)
print biggest(9, 3, 9)
print biggest(2, 2, 1)
print biggest(1, 2, 2)
print biggest(2, 1, 2)

# This is the solution in the Udacity video

def biggest2(a,b,c):
	if a > b:
		if a > c:
			return a
		else:
			return c
	else:
		if b > c:
			return b
		else:
			return c

print biggest2(3, 6, 9)
print biggest2(6, 9, 3)
print biggest2(9, 3, 6)
print biggest2(3, 3, 9)
print biggest2(9, 3, 9)
print biggest2(2, 2, 1)
print biggest2(1, 2, 2)
print biggest2(2, 1, 2)

# Remember our 'bigger' function from earlier in the lesson (scroll up!).
# This procedure can be used to solve this problem.

def biggest3(x,y,z):
	return bigger(bigger(x,y), z)

print biggest3(3, 6, 9)
print biggest3(6, 9, 3)
print biggest3(9, 3, 6)
print biggest3(3, 3, 9)
print biggest3(9, 3, 9)
print biggest3(2, 2, 1)
print biggest3(1, 2, 2)
print biggest3(2, 1, 2)

# Or, even easier, there is a built-in Python operator, 'max'.

def biggest4(x,y,z):  # Wouldn't even need this procedure, could just use 'max'
	return max(x,y,z)

print biggest4(3, 6, 9)
print biggest4(6, 9, 3)
print biggest4(9, 3, 6)
print biggest4(3, 3, 9)
print biggest4(9, 3, 9)
print biggest4(2, 2, 1)
print biggest4(1, 2, 2)
print biggest4(2, 1, 2)

# Decisions and Repitition: While Loop Playground

# This code demonstrates a while loop with a 'counting variable'
i = 0
while i < 10:
	print i
	i = i + 1

# This uses a while loop to remove all the spaces from a string of
# text. Can you figure out how it works?

def remove_spaces(text):
	text_without_spaces = '' # empty string for now

	while text != '':
		next_character = text[0]
		if next_character != ' ': # that's a single space
			text_without_spaces = text_without_spaces + next_character
		text = text[1:]

	return text_without_spaces

print remove_spaces("Hello my name is Troy how are you?")

# Decisions and Repitition: Print Numbers

# Define a procedure, print_numbers, that takes as input a positive
# whole number, and prints out all the whole numbers from 1 to the
# input number.

# Make sure your procedure prints 'upwards', so from 1 up to the 
# input number.

def print_numbers(number):
	i = 1
	while i <= number:
		print i
		i = i + 1

print_numbers(3)

# Stage 2: Work Session 4: Weekend

# Define a procedure, weekend, which takes a string as its input
# and returns the boolean True if it's 'Saturday' or 'Sunday' and
# False otherwise.

def weekend(day):
	return day == 'Saturday' or day == 'Sunday' # logical 'or' operator

print weekend("Monday")
print weekend("Tuesday")
print weekend("Wednesday")
print weekend("Thursday")
print weekend("Friday")
print weekend("Saturday")
print weekend("Sunday")

# Stage 2: Work Session 4: Blastoff

# Define a procedure, countdown, that takes a positive whole number
# as its input, and prints out a countdown from that number to 1, 
# followed by Blastoff!

# The procedure should not return anything. For this question, you 
# just need to call the procedure using the line 'countdown(3)', instead
# of 'print countdown(3)'

def countdown(number):
	while number > 0:
		print number
		number = number - 1
	print "Blastoff!"

countdown(3)
countdown(5)
countdown(-1)