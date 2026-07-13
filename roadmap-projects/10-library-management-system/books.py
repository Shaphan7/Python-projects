import uuid
import json
from datetime import datetime, timedelta

class Books:
    def __init__(self):
        self.books = []

    def find_by_name(self, name, collection):
        for item in collection:
            if item.get('name') == name:
                return item
        else:
            return False
        
    def remove_book(self, name):
        book = self.find_by_name(name, self.books)
        if not book:
            return print("Book not found")
        self.books.remove(book)
        return print(f"{name} has been removed")

    def view_books(self):
        for book in self.books:
            print(f"------{book.get('id')}------\n" \
                  f"Name: {book.get('name')}\n" \
                  f"Genre: {book.get('genre')}\n" \
                  f"Availability: {book.get('availability')}\n" \
                  f"Borrowed By: {book.get('borrowed_by')}")
            if book.get('due_date'):
                print(f"Due Date: {book.get('due_date')}")
            print(f"------------------------------------------------")

    def add_book(self, name, genre):
        self.books.append({"id": str(uuid.uuid4()), "name": name, "genre": genre, "availability": True, "borrowed_by": None})
        return True

    def mark_borrowed(self, book_name, member_name):
        # Later change to 3 days
        due_date = datetime.now() + timedelta(seconds=20)
        formated_due_date = due_date.strftime("%Y-%m-%d %H:%M:%S")
        book = self.find_by_name(book_name, self.books)
        if not book:
            return print("Book not found")  
        book["due_date"] = formated_due_date
        book['borrowed_by'] = member_name
        book['availability'] = False
        return print(f"{book_name} was borrowed by {member_name}")

    def book_returned(self, book_name, member_name):
        book = self.find_by_name(book_name, self.books)
        if not book:
            return print("Book not found")
        if book.get('availability'):
            return print("Can't return an already existing book")
        if book.get("due_date"):
            del book["due_date"]
        if book.get("penalized"):
            del book["penalized"] 
        book['borrowed_by'] = None
        book['availability'] = True
        return print(f"{book_name} was returned by {member_name}")

    def save(self):
        with open("books.json", "w") as file:
            for book in self.books:
                due_date = book.get("due_date", None)
                if not isinstance(due_date, str) and not due_date is None:
                    book["due_date"] = due_date.strftime("%Y-%m-%d %H:%M:%S")
            json.dump(self.books, file)

    def load(self):
        try:
            with open("books.json", "r") as file:
                self.books = json.load(file)
                for book in self.books:
                    if book.get("due_date"):
                        book["due_date"] = datetime.strptime(book["due_date"], "%Y-%m-%d %H:%M:%S")
        except json.decoder.JSONDecodeError:
            print("File is empty")
        except FileNotFoundError:
            pass
