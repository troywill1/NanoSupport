# Input -> Function -> Output - Sum Procedure

# What does the sum procedure do?

def sum(a,b):
	a = a + b
	return a

print sum(3,2)

# Input -> Function -> Output - Square

# Define a procedure, square, that takes one number
# as its input, and returns the square of that number
# (result of multiplying the number by itself).

def square(x):
	return x * x

print square(5)

x = 37
y = square(x)
print square(y)

print square(square(x))

# Input -> Function -> Output - Sum of Three

# Define a procedure, sum3, that takes three inputs,
# and returns the sum of the three input numbers.

def sum3(x, y, z):
	return x + y + z

print sum3(1,2,3)
print sum3(93,53,70)

# Input -> Function -> Output - Abbaize

# Define a procedure, abbaize, that takes two strings
# as its inputs, and returns a string that is the first
# input, followed by two repetitions of the second input,
# followed by the first input.

def abbaize(firstInput, secondInput):
	return firstInput + secondInput + secondInput + firstInput

print abbaize('a', 'b')
print abbaize('dog', 'cat')