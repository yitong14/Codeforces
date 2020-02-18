# 03-71A-way too long words

n = input()
n = int(n)
abbreviation = []
words = []
long = [0, 0, 0]
for i in range(n):
    words.append(input())
    if len(words[i]) <= 10:
        abbreviation.append(words[i])
    else:
        long[0] = words[i][0]
        long[1] = str(len(words[i]) - 2)
        long[2] = words[i][-1]
        abbreviation.append("".join(long))
for i in range(n):
    print(abbreviation[i])
