# Lesson 3.4b: Make Classes - Advanced Topics
# Mini-Project:

# Sometimes we want to define classes that may have similarities.
# For example, a TVShow class and a Movie class would both have a title
# attribute. To cut down on repitition we can have classes inherit from each
# other. So in our example we could have both TVShow and Movie inherit from a
# class Video which includes all the shared attributes between Movie and TVShow.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4195428894/m-1016138543

class Parent():
    def __init__(self, last_name, eye_color):
        print "Parent Constructor Called"
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print "Last Name - " + self.last_name
        print "Eye Color - " + self.eye_color

class Child(Parent): # Inherit from Class Parent
    def __init__(self, last_name, eye_color, number_of_toys):
        print "Child Constructor Called"
        # Use Parent's __init__, this is for code re-use
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print "Last Name - " + self.last_name
        print "Eye Color - " + self.eye_color

# For simplicity, not putting this in its own file.
troy_williams = Parent("Williams", "blue")
troy_williams.show_info()
noah_williams = Child("Williams", "blue", 12)
noah_williams.show_info()
print noah_williams.number_of_toys
