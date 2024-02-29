n = int(input())
study_set = set()
good_set = set()
perfect_set = set()

for i in range(n):
    m = int(input())
    for j in range(m):
        student = input()
        study_set.add(student)
        if student in good_set:
            perfect_set.add(student)
        else:
            perfect_set.discard(student)
    good_set = study_set
    study_set = set()

for student in perfect_set:
    print(student)
