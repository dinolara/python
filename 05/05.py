text = input()
meow = 0
cat = 0

while text != 'СТОП':
    meow += 1
    if 'кот' in text or 'Кот' in text and not cat:
        cat = meow
    text = input()

if cat:
    print(cat)
else:
    print(-1)
