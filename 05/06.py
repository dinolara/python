number = int(input())
s = 0
k = 0

while number != 0:
    if s < 10:
        s += number
        k += 1
    number = int(input())

print(k)
