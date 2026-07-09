from movie import Movie
import json

class Movies:
    def __init__(self):
        self.movies = []
    def add(self, name, genre, price, rating, release_date, views):
        self.movies.append(Movie(name, genre, price, rating, release_date, views))
        print("Movie Successfully Added!")
    def search(self, name):
        for movie in self.movies:
            if movie.name.lower() == name.lower():
                print(movie)
                break
        else:
            print("Movie not found!")
    def remove(self, name):
        for movie in self.movies:
            if movie.name.lower() == name.lower():
                self.movies.remove(movie)
                break
        else:
            print("Movie not found!")
    def save(self):
        with open("movies_db.json", "w")as file:
            json.dump([movie.to_dict() for movie in self.movies], file)
            print("Saved Successfully!")
    def load(self):
        with open("movies_db.json", "r")as file:
            for movie in json.load(file):
                self.movies.append(Movie(
                    movie.get('name'),
                    movie.get('genre'),
                    movie.get('price'),
                    movie.get('rating'),
                    movie.get('release_date'),
                    movie.get('views')
                ))
    def clean(self):
        with open("movies_db.json", "w")as file:
            file.write('[]')
        print("File Cleaned!")
                        