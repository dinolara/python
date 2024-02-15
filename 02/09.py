first_boy = int(input())
second_boy = int(input())
third_boy = int(input())

boys = [first_boy, second_boy, third_boy]

boys.sort(reverse=True)

for t in boys:
    print(t)
