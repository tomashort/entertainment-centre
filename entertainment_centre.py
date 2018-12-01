from movie import Movie

toy_story = Movie("Toy Story",
                  "A story of a boy and his toys that come to life.",
                  "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                  "https://www.youtube.com/watch?v=KYz2wyBy3kc")
print(f"{toy_story.title}: {toy_story.storyline}")
avatar = Movie("Avatar",
               "A marine on an alien planet.",
               "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
               "https://www.youtube.com/watch?v=5PSNL1qE6VY")
print(f"{avatar.title}: {avatar.storyline}")
withnail_and_i = Movie("Withnail & I",
                       "Two unemployed actors go on holiday by mistake.",
                       "https://upload.wikimedia.org/wikipedia/en/f/fe/Withnail_and_i_poster.jpg",
                       "https://www.youtube.com/watch?v=d9Z0DV33gAY")
print(f"{withnail_and_i.title}: {withnail_and_i.storyline}")
