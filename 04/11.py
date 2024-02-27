number = int(input())
mid = 0

for i in range(number):
    iq = int(input())
    mid += iq
    if iq < (mid / (i + 1)):
        print('<')
    elif iq > (mid / (i + 1)):
        print('>')
    else:
        print(0)
