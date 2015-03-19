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

# Stage 2: Work Session 3 - Udacify

# Define a procedure, udacify, that takes as input a string,
# and returns a string that is an uppercase 'U' followed by
# the input string. For example, when you enter

# print udacify('dacians')

# the output should be the string 'Udacians'

def udacify(inputString):
	return 'U' + inputString

print udacify('dacians')
print udacify('turn')
print udacify('boat')

# Stage 2: Work Session 3 - Automatically Generate HTML

# Write a function that takes a concept title and a concept
# description as input and then returns HTML that you can copy
# and paste into your notes web page.

def webify(conceptTitle, conceptDescription):
	return '''
	<div class="concept">
		<div class="concept-title">
			''' + conceptTitle + '''
		</div>

		<div class="concept-description">
			''' + conceptDescription + '''
		</div>
	</div>'''

print webify('Troy Title', 'Troy Description')