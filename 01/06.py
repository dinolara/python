first_answer = input('Вы любите бравлстарс? ')
second_answer = input('Вы играете в майнкрафт? ')

if first_answer == 'да' and second_answer == 'да':
    print('Вам 5 лет.')
if first_answer == 'да' and second_answer == 'нет':
    print('Вам 0 лет.')
if first_answer == 'нет' and second_answer == 'да':
    print('Вам 10 лет.')
if first_answer == 'нет' and second_answer == 'нет':
    print('Вам 11 лет и вы "не такой как все".')
else:
    print('Ошибка! Ответы на вопрос могут быть только "да" или "нет".')
