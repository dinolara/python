first_number = float(input())
second_number = float(input())
operation = input()
if operation == '+':
    print(first_number + second_number)
elif operation == '-':
    print(first_number - second_number)
elif operation == '*':
    print(first_number * second_number)
elif operation == '/' and second_number != 0:
    print(first_number / second_number)
else:
    print('888888')
