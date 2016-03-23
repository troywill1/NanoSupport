# Lesson 3.4a: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/m-1013629057

import webbrowser

# Google Style Guide for Python suggests that the first letter of the name
# of a class should be uppercase.

# It is good style to define classes in one file and call them from another,
# however, that is not a requirement. It would all still work in a single file.

class Movie():
    """
    This class provides a way to store movie related information
    """

    # Class variable. Available to all instances of this class.
    # Google Style Guide suggests constant variables by UPPERCASE.
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    # 'self' is a convention used by most python programmers
    def __init__(self, movie_title, movie_storyline, poster_image,
                trailer_youtube):
        # initialize instance of class Movie
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
