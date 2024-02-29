n1 = int(input())
n2 = int(input())
n3 = int(input())
english_set = set()
german_set = set()
french_set = set()

for i in range(n1):
    english = input()
    english_set.add(english)

for i in range(n2):
    german = input()
    german_set.add(german)

for i in range(n3):
    french = input()
    french_set.add(french)

single_set = english_set ^ german_set ^ french_set
duo_set = (english_set | german_set | french_set) ^ single_set

if len(duo_set) != 0:
    print(len(duo_set))
else:
    print('NO')
