# 05-236A-boy or girl

name = input()
n = len(name)
for i in range(n):
    for j in range(i):
        if name[i] == name[j]:
            n = n - 1
            break
if n % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
