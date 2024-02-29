n = int(input())
meow = False

for i in range(n):
    text = input()
    if 'пёс' in text or 'Пёс' in text:
        meow = False

    if 'кот' in text or 'Кот' in text:
        meow = True

if meow:
    print('МЯУ')
else:
    print('НЕТ')
