# 01-1167A-telephone number

t = input();
t = int(t)
temp = []
numbers = []
for i in range(t):
    n = input();
    n = int(n)
    numbers.append(input());
    temp.append(0)
    if n >= 11:
        for j in range(n - 10):
            if numbers[i][j] == "8":
                temp[i] = 1
                break
for i in range(t):
    if temp[i] == 0:
        print("NO")
    else:
        print("YES")
