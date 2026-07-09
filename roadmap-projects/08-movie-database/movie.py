class Movie:
    def __init__(self, name, genre, price, rating, release_date, views):
        self.name = name
        self.genre = genre
        self.price = price
        self.rating = rating
        self.release_date = release_date
        self.views = views
    def __str__(self):
        return "-----------------------------\n" \
              f"Name: {self.name}\n" \
              f"Genre: {self.genre}\n" \
              f"Price: {self.price}\n" \
              f"Rating: {self.rating}\n" \
              f"Release Date: {self.release_date}\n" \
              f"Views: {self.views}\n" \
               "-----------------------------" 
    def to_dict(self):
        return {
            "name": self.name,
            "genre": self.genre,
            "price": self.price,
            "rating": self.rating,
            "release_date": self.release_date,
            "views": self.views
        }