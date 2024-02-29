n1 = int(input())
n2 = int(input())
english_german_set = set()

for i in range(n1 + n2):
    student = input()
    english_german_set.add(student)

if len(english_german_set) * 2 != (n1 + n2):
    print(n1 + n2 - (n1 + n2 - len(english_german_set)) * 2)
else:
    print('NO')
