number = int(input())
s = 0

for i in range(number):
    n = int(input())
    s += (-1)**i * n

print(s)
