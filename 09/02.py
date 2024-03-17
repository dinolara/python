data = []
for i in range(int(input())):
    inf = input()
    data.append(inf)
search = input()
for word in data:
    if search in word:
        print(word)
