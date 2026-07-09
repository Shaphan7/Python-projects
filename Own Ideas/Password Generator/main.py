import random
import os

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_',  '/', '<', '>', '`', '~']
s_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
c_alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [1, 2, 3, 4, 5, 7, 8, 9, 0]
commands = {
    'help': lambda: print("-------------Help-------------\n" \
                          "view = view current password" \
                          "g_pwd length of password (g_pwd 23) = generates password with given length\n" \
                          "export name of file (export bob) = export password with to file with given name\n" \
                          "exit = close app\n" \
                          "------------------------------")
}

password_l = []

def generatePassword(length):
    if length.isdigit():
        if not int(length) <= 32:
            return("Password length is too big")
        elif not int(length) >= 8:
            return("Password length is too small")
    else:
        return("Length must be a number!")
    
    if len(password_l) > 0:
        while True:
            answer = input("Password already exists! Overide? (y/n)\n Answer: ")
            if answer == "y":
                break
            elif answer == "n":
                return "Process stoped!"
            else:
                print("Please type a valid answer.")
    while len(password_l) < int(length):
        if not len(password_l) < int(length): break
        password_l.append(random.choice(symbols))
        if not len(password_l) < int(length): break
        password_l.append(random.choice(s_alphabets))
        if not len(password_l) < int(length): break
        password_l.append(random.choice(c_alphabets))
        if not len(password_l) < int(length): break
        password_l.append(str(random.choice(numbers)))
    random.shuffle(password_l)
    return f"Password Generated: {"".join(password_l)} (Be sure to export it)"

def exportPassword(name):
    if os.path.isfile(f"{name}.txt"):
        while True:
            answer = input(f'"{name}.txt" already exists! Overide? (y/n)\nAnswer: ')
            if answer == "y":
                break
            elif answer == "n":
                return "Process stoped!"
            else:
                print("Please type a valid answer.")
    with open(f"{name}.txt", "w") as file:
        if password_l == []:
            return "No password to save!"
        file.write("".join(password_l))
        return "Password saved!"

def main():
    print("|---------Password-Generator---------|")
    while True:
        command = input("Command: ")
        if command in commands:
            commands[command]()
        elif command.startswith('export'): 
            length = command.split(" ")
            try:
                print(exportPassword(length[1]))
            except IndexError:
                print("No file name was given.")
        elif command == "view":
            if password_l == []:
                print("No password to view.")
            else:
                print("".join(password_l))
        elif command.startswith('g_pwd'): 
            length = command.split(" ")
            try:
                print(generatePassword(length[1]))
            except IndexError:
                print("No length was given (8-32).")
        elif command == "exit":
            print("|-------------App-Closed-------------|")
            break
        else:
            print("The syntax of the command is incorrect! (use 'exit' or 'help')")

main()
        