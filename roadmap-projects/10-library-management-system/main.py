from books import Books
from members import Memembers
import hashlib
import string
import secrets
import hmac
import os
from datetime import datetime, timedelta
members = Memembers()
books = Books()
books.load()
members.load()
# I know rn anyone can borrow a book using anyones name since you can guess the name

def verify_due_dates():
    real_datetime = datetime.now().replace(microsecond=0)
    for book in books.books:
        if book.get("due_date"):
            if real_datetime > book["due_date"] and not book.get("penalized"):
                for member in members.members:
                    if member.get("name") == book.get("borrowed_by"):
                        member["rating"] -= 1
                        book["penalized"] = True
                        rating_cool_down = datetime.now() + timedelta(seconds=20)
                        formated_cool_down = rating_cool_down.strftime("%d-%m-%Y %H:%M:%S")
                        member["rating_cool_down"] = formated_cool_down

#=CaHaz+ldi53Ha^^
def generate_password():
    password_list = []
    for _ in range(16):
        password_list.append(secrets.choice(string.ascii_letters + string.digits + string.punctuation))

    password = "".join(password_list)
    with open(".env", "w") as file:
        file.write(f"PWD_HASH={hashlib.sha256(password.encode('utf-8')).hexdigest()}")
    print(f"Password generated!\nPassword: {password}\n(save it somewhere since it's has been hashed)")

def pwd_generation_auth():
    if os.path.isfile("./.env"):
        typed_password = input("Password: ")
        with open('.env', "r") as file:
            _, real_password_hash = file.read().split("=")
        isMatch = hmac.compare_digest(real_password_hash, hashlib.sha256(typed_password.encode("utf-8")).hexdigest())
        if isMatch:
            answer = input("Password already exist, overide?(y/n): ")
            if answer == "y":
                generate_password()
            else:
                return print("Process stopped!")
        else:
            print("Access Denied!")
    else:
        generate_password()
    
# I couldn't shorten this since it covers a lot of input validation
def add(member=False, book=False):
    if book:
        name = input("Name: ")
        genre = input("Genre: ")
        if books.add_book(name, genre):
            print("Book has been added successfully!")
        else:
            print("Book couldn't been added!")
    elif member:
        while True:
            name = input("Name: ")
            if name.isdigit():
                print("Name cannot contain number!")
            else:
                break
        while True:
            age = input("Age: ")
            if not age.isdigit():
                print("Age must be number!")
            else:
                break
        
        if members.add_member(name, age):
            print("Member has been added successfully!")
        else:
            print("Member couldn't been added!")

def borrowBookValidation():
    member_name = input("Member Name: ")
    book_name = input("Book Name: ")
    members.borrow_book(member_name, book_name, books)

def returnBookValidation():
    member_name = input("Member Name: ")
    book_name = input("Book Name: ")
    members.return_book(member_name, book_name, books)

def view_all_members():
    typed_password = input("Password: ")
    with open('.env', "r") as file:
        _, real_password_hash = file.read().split("=")
    isMatch = hmac.compare_digest(real_password_hash, hashlib.sha256(typed_password.encode("utf-8")).hexdigest())
    if isMatch:
        members.view_members()
    else:
        print("Access Denied!")

def id_search_validation():
    id = input("Member ID: ")
    members.view_by_id(id)

def remove(book=False, member=False):
    if member:
        name = input("Member Name: ")
        members.remove_member(name)
    elif book: 
        name = input("Book Name: ")
        books.remove_book(name)
commands = {
    "g_pwd": lambda: pwd_generation_auth(),
    "a_member": lambda: add(member=True),
    "r_member": lambda: remove(member=True),
    "v_member_id": lambda: id_search_validation(),
    "v_members": lambda: view_all_members(),
    "a_book": lambda: add(book=True),
    "r_book": lambda: remove(book=True),
    "v_books": lambda: books.view_books(),
    "b_book": lambda: borrowBookValidation(),
    "rtn_book": lambda: returnBookValidation(),
    "help": lambda: print("-------------Help-------------\n" \
                          "g_pwd = generate password (restricted)\n" \
                          "a_member = add member\n" \
                          "r_member = remove member\n" \
                          "v_member_id = view member by id\n" \
                          "v_members = view all members (restricted)\n" \
                          "a_book = add book\n" \
                          "r_book = remove book\n" \
                          "v_books = view all books\n" \
                          "b_book = borrow book\n" \
                          "rtn_book = return book\n" \
                          "save = save changes\n" \
                          "help = show help\n" \
                          "exit = close app"),
}

def main():
    while True:
        command = input("Command: ")
        if command in commands:
            commands[command]()
        elif command == "exit":
            print("----------App-closed----------")
            break
        elif command == "save":
            books.save()
            members.save()
            print("Saved Successfully")
        else:
            print("Invalid syntax. Use 'help' or 'exit'")

verify_due_dates()
members.restore_member_rating()
main()
