mx = int(input())

for i in range(int(input())):
    text = input()
    if len(text) > mx:
        text = text[:mx - 3] + '...'
    print(text)
