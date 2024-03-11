name = input()
alphabet = 'qwertyuiopasdfghjklzxcvbnm_1234567890'

for char in name:
    if char not in alphabet:
        print(f'Неверный символ: {char}')
        break
else:
    print('OK')
