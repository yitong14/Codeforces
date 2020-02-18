# 732A - buy a shovel
k, r = map(int, input().split())
temp = 0
for i in range(1, 11):
    if k*i % 10 == r:
        print(i)
        temp = 1
        break
    elif k*i % 10 == 0:
        print(i)
        temp = 1
        break
if temp == 0:
    print(10)