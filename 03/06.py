i = 0

while i != 1:
    first_password = input()
    second_password = input()
    if len(first_password) >= 8:
        if '123' in first_password:
            print("Простой!")
        else:
            if first_password == second_password:
                i = 1
                print("OK")
            else:
                print("Различаются.")
    else:
        print("Короткий!")

