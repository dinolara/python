span_1 = 1000
span_2 = 1
number = span_1 // 2

print(number)
answer = input()

while answer != '=':
    if answer == '<':
        span_2 = number
        number = (number + span_1) // 2
    elif answer == '>':
        span_1 = number
        number = (number + span_2) // 2
    print(number)
    answer = input()
