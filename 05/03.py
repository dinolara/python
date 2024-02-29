text = input()
meow = 1
cat = 0

while text != 'СТОП':
    if ('кот' in text or 'Кот' in text) and not cat:
        cat = meow
    else:
        meow += 1
    text = input()

if cat:
    print(cat)
else:
    print(-1)
