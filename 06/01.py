first_set = set()
second_set = set()

number = input()

while number != '':
    first_set.add(number)
    number = input()

number = input()

while number != '':
    second_set.add(number)
    number = input()

intersection = first_set & second_set

if len(intersection) != 0:
    for num in intersection:
        print(num)
else:
    print('EMPTY')
