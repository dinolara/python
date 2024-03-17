text = []
search = []
for i in range(int(input())):
    text.append(input())
for i in range(int(input())):
    search.append(input())
n = 0
for word in text:
    for name in search:
        if name in word:
            n += 1
    if n == len(search):
        print(word)
    n = 0

