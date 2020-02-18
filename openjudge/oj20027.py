# 20027 - 字符串问题
a = list(input())
k = int(input())
for i in range(k+1):
    for j in range(len(a)-1, -1, -1):
        if a[j] == 'z':
            a[j] = 'a'
        else:
            a[j] = chr(ord(a[j])+1)
            break
print(''.join(a))