# Lesson 3.3: Use Classes
# Mini-Project: Draw Turtles

# turtle is a library we can use to make simple computer graphics. Kunal
# wants you to try drawing circles using squares. You can also use this
# space to create other kinds of shapes. Experiment and share your results
# on the Discussion Forum!

import turtle

# Your code here.
def draw_square():
    """
    docstring here
    """

    # Create a screen and set its background color
    window = turtle.Screen()
    window.bgcolor("red")

    troy = turtle.Turtle()
    troy.shape("circle")
    troy.color("green", "blue")
    troy.speed(2)

    troy.forward(100)
    troy.right(90)
    troy.forward(100)
    troy.right(90)
    troy.forward(100)
    troy.right(90)
    troy.forward(100)
    troy.right(90)

    # Ability to exit the window by clicking
    window.exitonclick()

draw_square()
