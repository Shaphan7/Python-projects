from movies import Movies
from movie import Movie
import hashlib
import hmac
import os
movies = Movies()
movies.load()
# password123
password = "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f"

def addMovie():
    # Name can indeed have numbers since there are sequels in movies
    name = input("Name: ")
    while True:
        genre = input("Genre: ")
        if genre.isdigit():
            print("Genre cannot have number!")
        else:
            break
    while True:
        try:
            price = float(input("Price: "))
            break
        except ValueError:
            print("Price must be a number!")
    while True:
        try:
            rating = float(input("Rating(Out of 10): "))
            if int(rating) > 10:
                print("Rating cannot be greater than 10!")
            else:
                break
        except ValueError:
            print("Rating must be a number!")
    release_date = input("Release Date: ")
    while True:
        views = input("Views: ")
        if not views.isdigit():
            print("Views must be a number!")
        else:
            break
    movies.add(name, genre, price, rating, release_date, views)

def removeMovie():
    name = input("Name: ")
    answer = input("Are you sure?(y/n): ")
    if answer == "y":
        movies.remove(name)
    else:
        print("Process Stoped!")

def searchMovie():
    name = input("Name: ")
    movies.search(name)

def searchMovieByFilter(filter):
    print("bob")

def sortBy(attribute, reverse=True):
    sorted_movies = sorted(movies.movies, key=lambda movie: getattr(movie, attribute), reverse=reverse)
    for movie in sorted_movies:
        print(movie)

def averageRating():
    ratings = [movie.rating for movie in movies.movies]
    print(f"Average Rating: {sum(ratings) / len(ratings)}")

def cleanDB():
    answer = input("Are you sure you want to delete everything in the DB? (y/n): ")
    if answer == "y":
        user_password = input("Password: ")
        isMatch = hmac.compare_digest(hashlib.sha256(user_password.encode("utf-8")).hexdigest(), password)
        if isMatch:
            movies.clean()
        else:
            print("Access denied!")
    else:
        print("Process Stoped!")

filters = {
    "-hr": lambda: sortBy("rating"),
    "-lr": lambda: sortBy("rating", reverse=False),
    "-ar": lambda: averageRating(),
    "-me": lambda: sortBy("price"),
    "-le": lambda: sortBy("price", reverse=False),
    "-mw": lambda: sortBy("views")
}

commands = {
    "a_movie": lambda: addMovie(),
    "r_movie": lambda: removeMovie(),
    "save": lambda: movies.save(),
    "clean": lambda: cleanDB(),
    "help": lambda: print("------------Help------------\n" \
                          "a_movie: add movie\n" \
                          "r_movie: remove movie\n" \
                          "save: save changes\n" \
                          "clean: delete all item in database\n" \
                          "s_movie: search movie\n" \
                          "s_movie -hr: sort by highest to lowest rating\n" \
                          "s_movie -lr: sort by lowest to highest rating\n" \
                          "s_movie -me: sort by highest to lowest price\n" \
                          "s_movie -le: sort by lowest to highest price\n" \
                          "s_movie -mw: sort by highest to lowest views\n" \
                          "s_movie -ar: finds the average rating of all movies\n" \
                          "exit: close app\n" \
                          "----------------------------")
}

def checkFilters(command):
    value = command.split(" ")
    try:
        if value[1] in filters:
            filters[value[1]]()
        else:
            return print("Invalid Filter!")
    except IndexError:
        searchMovie()

def main():
    print("|---------Movie-Database---------|")
    while True:
        command = input("Command: ")
        if command in commands:
            commands[command]()
        elif command.startswith("s_movie"):
            checkFilters(command)
        elif command == "exit":
            print("|-----------App-Closed-----------|")
            break
        else:
            print("The syntax of the command is incorrect! (use 'exit' or 'help')")

main()
