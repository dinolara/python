n = int(input())
meow = False

for i in range(n):
    text = input()
    if 'кот' in text or 'Кот' in text:
        meow = True
        break

if meow:
    print('МЯУ')
else:
    print('НЕТ')
