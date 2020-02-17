# 112A - petya and strings
alpha_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4,
              'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
              'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
              'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
              'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24,
              'z': 25}
a = input().lower()
b = input().lower()
temp = 0
for i, j in zip(a, b):
    if alpha_dict[i] == alpha_dict[j]:
        continue
    elif alpha_dict[i] < alpha_dict[j]:
        print(-1)
        temp = 1
        break
    else:
        print(1)
        temp = 1
        break
if temp == 0:
    print(0)