# Notes from the Stage 2, Functions, Print vs. Return Statements Hangout

# Local vs. Global Scope
# As a best practice, it is best to avoid Glogal variables.
a = 6

def some_function():
	a = 5
	print "Function: " + str(a)

some_function()
print "Global: " + str(a)


# Mutable vs. Immutable Objects

# Mutable Example
def some_function2(some_list):
	some_list.append(1)
	print "Local: " + str(some_list)

a = [1,2,3] # This is a list
some_function2(a)
print "Global: " + str(a)

# Immutable Example
def some_function3(some_list):
	some_list += 1
	print "Local: " + str(some_list)

a = 5 # a points to the contant 5, which is immutable
some_function3(a)
print "Global: " + str(a)

# This is why we need return statements


# Return Statements
def some_function4(some_value):
	some_value += 1
	print "Local: " + str(some_value)
	return some_value # Stops the function

a = 5 # a points to the contant 5, which is immutable
x = some_function4(a)
print "Global: " + str(x)

# Some interesting Return Statements
def some_function5(some_value):
	some_value += 1
	print "Local: " + str(some_value)
	return some_value, 1, 2 # multiple return items

a = 5
x, y, z = some_function5(a) # assigning to multiple variables
print "Global: " + str(x) + " " + str(y) + " " + str(z)
# - Or -
print some_function5(a) # just print the values

# Multiple return statements using 'if'
def some_function6(some_value):
	if type(some_value) == type(1):
		return 1
	else:
		return "Not and INT"

print some_function6(25)
print some_function6(25.0)

# Return statement with a 'for' loop
def some_function7(some_value):
	some_list = []
	for e in range(10):
		some_list.append(some_value)
	return some_list

print some_function7(25)
print some_function7(25.0)

# Returning with recursion (Python is not well-suited for this)
def some_function8(some_value, count):
	print some_value
	if count == 0:
		return some_value
	else:
		return some_function8(some_value + 1, count - 1)

print some_function8(25, 10)