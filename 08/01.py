word = input()
long = ''
short = ''

while word != 'стоп':
    if len(word) > len(long):
        long = word
    if len(word) < len(short) or not short:
        short = word
    word = input()

funded = True
for char in short:
    if char not in long:
        funded = False
        break
if funded:
    print('ДА')
else:
    print('НЕТ')
