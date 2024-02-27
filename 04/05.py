number = int(input())
numbers = 1

for i in range(5):
    if number != 0:
        numbers *= number
    number = int(input())

print(numbers)
