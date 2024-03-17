first_list = []
second_list = []
for i in range(int(input())):
    first_list.append(input())
for i in range(int(input())):
    second_list.append(input())
for first in first_list:
    for second in second_list:
        if first == second:
            print(first)
