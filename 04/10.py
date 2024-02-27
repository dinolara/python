for i in range(17):
    number = int(input())
    if i % number == 0:
        print('ДА')
    elif number == 0:
        print('На 0 делить нельзя')
    else:
        print('НЕТ')
