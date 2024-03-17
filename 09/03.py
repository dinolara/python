text = []
first = ''
for i in range(int(input())):
    text.append(input())
for word in text:
    first += word[0]
print(first)
