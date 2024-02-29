n = int(input())
food_set = set()

for i in range(n):
    food = input()
    food_set.add(food)

m = int(input())
recipe_set = set()

for i in range(m):
    recipe = input()
    n = int(input())
    for j in range(n):
        food = input()
        recipe_set.add(food)
    if food_set >= recipe_set:
        print(recipe)
    recipe_set = set()
