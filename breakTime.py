# Lesson 3.2: Use functions
# Mini-Project: Take a Break

# Write a program that prompts the user to take a break
# once every two hours, a maximum of three times.

# User this space to describe your approach to the problem.
# 1. Start a timer
# 2. Wait for the timer to reach 2hrs
# 3. When the timer reaches 2hrs, prompt the user to take a break
# 4. Reset the timer
# 5. Follow the above steps 2 more times
# 6. Exit

# Your code here.
import time, webbrowser

totalBreaks = 3
counter = 0

print "Take a Break program started at: " + time.ctime() # current time
while counter < totalBreaks:
    time.sleep(7200) # time in seconds
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    counter += 1
