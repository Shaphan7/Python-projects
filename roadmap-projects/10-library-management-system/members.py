import uuid
import json
from datetime import datetime, timedelta

class Memembers:
    def __init__(self):
        self.members = []

    def restore_member_rating(self):
        for member in self.members:
            if member.get("rating") < 10:
                if member.get("rating_cool_down") < datetime.now().replace(microsecond=0):
                    member["rating"] += 1                    
                    # Later to 20 days
                    rating_cool_down = datetime.now() + timedelta(seconds=20)
                    formated_cool_down = rating_cool_down.strftime("%d-%m-%Y %H:%M:%S")
                    member["rating_cool_down"] = formated_cool_down
                    # I know I am creating a then checking should I del it
                    if member.get("rating") >= 10:
                        del member["rating_cool_down"]
                        
    def add_member(self, name, age):
        now = datetime.now()
        self.members.append({"id": str(uuid.uuid4()), "name": name, "age": age, "member_since": now.strftime("%d-%m-%y"), "books_borrowed": [], "rating": 10})
        return True
    
    # is self really needed here since I'm not using it?
    # Answer: If you remove it, it becomes a @staticmethod, but leaving it is fine since you can access it using self.method.
    def display_formated_member(self, member):
         print(f"------{member.get('id')}------\n" \
                  f"Name: {member.get('name')}\n" \
                  f"Age: {member.get('age')}\n" \
                  f"Member Since: {member.get('member_since')}\n" \
                  f"Books borrowed: {member.get('books_borrowed')}\n" \
                  f"Rating: {member.get('rating')}\n" \
                  f"------------------------------------------------")
    
    def find_by_name(self, name, collection):
        for item in collection:
            if item.get('name') == name:
                return item
        else:
            return False
        
    def remove_member(self, name):
        member = self.find_by_name(name, self.members)
        if not member:
            return print("Member not found!")
        self.members.remove(member)
        return print(f"{name} has been removed")

    def view_members(self):
        for member in self.members:
            self.display_formated_member(member)

    def view_by_id(self, id):
        for member in self.members:
            if member.get('id') == id:
                self.display_formated_member(member)    
                break
        else:
            print("User not found!")
        
    def borrow_book(self, member_name, book_name, books):
        book = self.find_by_name(book_name, books.books)
        member = self.find_by_name(member_name, self.members)
        if not book:
            return print("Book not found")
        if not member:
            return print("Member not found")
        if int(member.get('rating', 0)) <= 5:
            return print("Member rating too low.")
        if not book.get('availability'):
            return print(f"Book found but, it was borrowed by {book.get('borrowed_by')}")
        else:
            member['books_borrowed'].append(book.copy())
            books.mark_borrowed(book_name, member_name)
            return

    def return_book(self, member_name, book_name, books):
        book = self.find_by_name(book_name, books.books)
        member = self.find_by_name(member_name, self.members)
        if not book:
            return print("Book not found")
        if not member:
            return print("Member not found")
        if member_name == book.get("borrowed_by"):
            for borrowed_book in member['books_borrowed']:
                if borrowed_book.get("id") == book.get("id"):
                    member["books_borrowed"].remove(borrowed_book)
                    books.book_returned(book_name, member_name)
                    return
        else:
             return print("You haven't borrowed this book!")
 
    def save(self):
        with open("members.json", "w") as file:
            json.dump(self.members, file)

    def load(self):
        try:
            with open("members.json", "r") as file:
                self.members = json.load(file)
                for member in self.members:
                    if member.get("rating_cool_down"):
                        member["rating_cool_down"] = datetime.strptime(member["rating_cool_down"], "%Y-%m-%d %H:%M:%S")
        except json.decoder.JSONDecodeError:
            print("File is empty")
        except FileNotFoundError:
            pass