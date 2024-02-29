n = int(input())

eurasia = 'Евразия'
ostasia = 'Остазия'
good = ostasia
bad = eurasia

for i in range(n):
    phrase = input()
    if phrase == 'С кем война?':
        print(bad)
    elif phrase == 'С кем мир?':
        print(good)
    elif phrase == 'Меняем':
        bad1 = bad
        bad = good
        good = bad1
