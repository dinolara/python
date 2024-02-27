number = int(input())
a = 0

for i in range(1, number + 1):
    if (number % i) == 0:
        print(i, end=' ')
        a += 1

if a > 2:
    print('\nНЕТ')
else:
    print('\nПРОСТОЕ')
