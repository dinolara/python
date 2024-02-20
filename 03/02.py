first_password = input()
second_password = input()

if len(first_password) >= 8:
    if first_password == second_password:
        print("OK")
    else:
        print("Различаются.")
else:
    print("Короткий!")
