m = int(input())
n = int(input())
library_set = set()

for i in range(m):
    book = input()
    library_set.add(book)

for i in range(n):
    book = input()
    if book in library_set:
        print('YES')
    else:
        print('NO')
