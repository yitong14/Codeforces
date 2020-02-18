# 2679 - 整数的立方和
k = int(input())
cnt = 0
for i in range(1, k+1):
    cnt += i**3
print(cnt)