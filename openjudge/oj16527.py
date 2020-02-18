# 16527 - 字符串连接位置
a = input()
b = input()
for i in range(len(a)):
    if a[-(i+1):] == b[:i+1]:
        print(len(a)-i-1)
        break