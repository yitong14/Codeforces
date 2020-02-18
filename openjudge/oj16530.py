# 16530 - 改卷子
n = int(input())
names = [input() for i in range(n)]
names.sort()
a = names[n//2-1]
b = names[n//2]

length = len(a)
cur = 0
temp = ''
rst = ''
ok = False
while cur < length:
    for i in range(26):
        rst = temp
        rst += chr(i+65)
        if a <= rst < b:
            ok = True
            break
    if ok:
        break
    temp += a[cur]
    cur += 1

print(rst)
