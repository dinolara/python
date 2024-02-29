n = int(input())
city_set = set()

for n in range(n):
    city = input()
    city_set.add(city)

answer = input()

if answer in city_set:
    print('TRY ANOTHER')
else:
    print('OK')
