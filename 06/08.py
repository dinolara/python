n = int(input())
work_set = set()

for i in range(n):
    worker = input()
    work_set.add(worker)

print(len(work_set))
