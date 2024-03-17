first_str = input()
n = int(first_str[:4])
summa = int(first_str[4:])
errors = []
actual_sum = 0
for i in range(n):
    shop = input()
    actual_sum += int(shop[13:])
    if int(shop[:7]) * int(shop[8:12]) != int(shop[13:]):
        errors.append(i + 1)
print(abs(summa - actual_sum))
for error in errors:
    print(error, end=' ')

