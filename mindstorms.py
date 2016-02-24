# Lesson 3.3: Use Classes
# Mini-Project: Draw Turtles

# turtle is a library we can use to make simple computer graphics. Kunal
# wants you to try drawing circles using squares. You can also use this
# space to create other kinds of shapes. Experiment and share your results
# on the Discussion Forum!

import turtle

# Your code here.
def draw_square(some_turtle):
    """
    docstring here
    """

    for i in range(0,4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_circle():

    # Draw a circle
    angie = turtle.Turtle()
    angie.shape("circle")
    angie.color("blue")
    angie.circle(100)

def draw_triangle():

    # Draw a triangle
    bart = turtle.Turtle()
    bart.shape("triangle")
    bart.color("red")

    for i in range(0,3):
        bart.forward(200)
        bart.left(120)

# Create a screen and set its background color
window = turtle.Screen()
window.bgcolor("white")

# Create a turtle to draw a square
troy = turtle.Turtle()
troy.shape("square")
troy.color("green", "blue")
troy.speed(2)

# Draw a circle out of squares
for i in range(0,36):
    draw_square(troy)
    troy.right(10)

# draw_circle()
# draw_triangle()

# Ability to exit the window by clicking
window.exitonclick()
