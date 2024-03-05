word0 = input()
word1 = input()

while word0[-1] == word1[0]:
    word0 = word1
    word1 = input()

print(word1)
