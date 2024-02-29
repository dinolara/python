a = int(input())
b = int(input())

for i in range(a, b + 1):
    if not i % 15:
        print('FizzBuzz')
        continue
    elif not i % 3:
        print('Fizz')
    elif not i % 5:
        print('Buzz')
    else:
        print(i)
