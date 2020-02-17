# 71A - way too long words
n = int(input())
words = []
for i in range(n):
    s = input()
    temp = []
    length = len(s)
    if length <= 10:
        words.append(s)
    else:
        temp.append(s[0])
        temp.append(str(length - 2))
        temp.append(s[length - 1])
        words.append("".join(temp))
for i, word in enumerate(words):
    print(word)
