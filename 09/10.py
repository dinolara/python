numbs = []
for i in range(int(input())):
    numbs.append(int(input()))
summa = 0
for i in range(int(input()) - 1, int(input())):
    summa += numbs[i]
print(summa)
