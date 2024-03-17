numbs = []
for i in range(int(input())):
    numbs.append(int(input()))
for i in range(1, len(numbs)):
    print(numbs[i - 1] + numbs[i])
