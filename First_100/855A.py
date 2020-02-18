# 02-855A-Tom Riddle's Diary

n = input();
n = int(n)
names = []
temp = []
for i in range(n):
    names.append(input())
    temp.append(0)
    for j in range(len(names) - 1):
        if names[i] == names[j]:
            temp[i] = 1
            break
for i in range(n):
    if temp[i] == 0:
        print("NO")
    else:
        print("YES")
