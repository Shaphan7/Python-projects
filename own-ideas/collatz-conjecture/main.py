
while True:
    s_number = input("Starting Number: ")
    if not s_number.isdigit():
        print("Please type a number!")
    else:
        break

answer = int(s_number)
while answer != 1:
    if not answer % 2 == 0:
        answer = (answer * 3) + 1
        print(answer)
    else:
        answer = answer // 2
        print(answer)