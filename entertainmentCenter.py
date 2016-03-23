# Lesson 3.4a: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064

import media # media.py we created and in the same folder as this file
import fresh_tomatoes

# file/module media, class Movie w/i said file/module
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

# print toy_story.storyline

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# print avatar.storyline
# avatar.show_trailer()

star_wars = media.Movie("Star Wars: The Force Awakens",
                        "The force calls to you. Let it in.",
"https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",
                        "https://www.youtube.com/watch?v=sGbxmsDFVnE")

batman_superman = media.Movie("Batman v Superman: Dawn of Justice",
                        "A bat and an alien. What's not to like?",
"https://upload.wikimedia.org/wikipedia/en/2/20/Batman_v_Superman_poster.jpg",
                        "https://www.youtube.com/watch?v=eX_iASz1Si8")

finding_dory = media.Movie("Finding Dory",
                        "A clown fish with a very short memory.",
"https://upload.wikimedia.org/wikipedia/en/3/3e/Finding_Dory.jpg",
                        "https://www.youtube.com/watch?v=oP0WR2Ql9yI")

petes_dragon = media.Movie("Pete's Dragon",
                        "A boy plays with his dragon.",
"https://upload.wikimedia.org/wikipedia/en/d/d2/Petes_dragon_2016_film_poster.jpg",
                        "https://www.youtube.com/watch?v=gkmhppxFk84")

# print star_wars.storyline
# star_wars.show_trailer()

movies = [toy_story, avatar, star_wars, batman_superman, finding_dory,
          petes_dragon]
# fresh_tomatoes.open_movies_page(movies)
print media.Movie.VALID_RATINGS # Class variable. See 'media.py'.
print media.Movie.__doc__ # Python includes some pre-defined Class variables
print media.Movie.__name__ # The name of the Class
print media.Movie.__module__ # Name of module in which the Class was defined
