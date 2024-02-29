text = input()
meow = 0
cat = 0
poop = 0

while text != 'СТОП':
    meow += 1
    if 'кот' in text or 'Кот' in text:
        poop += 1
    if 'кот' in text or 'Кот' in text and not cat:
        cat = meow
    text = input()

print(poop, end=' ')

if cat:
    print(cat)
else:
    print(-1)
