n1 = int(input())
n2 = int(input())
english_set = set()
german_set = set()

for i in range(n1):
    english = input()
    english_set.add(english)

for i in range(n2):
    german = input()
    german_set.add(german)

single_set = english_set ^ german_set

if len(single_set) != 0:
    print(len(single_set))
else:
    print('NO')
