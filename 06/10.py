m = int(input())
food_set = set()

for i in range(m):
    food = input()
    food_set.add(food)

n = int(input())
yes_set = set()

for i in range(n):
    m = int(input())
    for j in range(m):
        yes = input()
        yes_set.add(yes)

no_set = food_set - yes_set

for no in no_set:
    print(no)
