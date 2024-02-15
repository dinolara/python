first_place = input()
second_place = input()

if first_place != second_place and (first_place == 'Тула' or second_place == 'Пенза'):
    if first_place == 'Тула' and second_place == 'Пенза':
        print('НЕТ')
    else:
        print('ДА')
else:
    print('НЕТ')
