# oj16527 - 字符串连接位置

a = input()
b = input()
i = len(a) - 1
j = 1
while i >= 0:
    if a[i:] == b[:j]:
        print(i)
        break
    i -= 1
    j += 1
