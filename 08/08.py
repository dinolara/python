text = input()
mx = 0
k = 0
for i in range(len(text)):
    if text[i] != 'р':
        k += 1
    elif text[i] == 'р':
        k = 0
    if k > mx:
        mx = k
print(mx)
