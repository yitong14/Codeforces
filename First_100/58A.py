# 58A - chat room - 待改进！！
s = input()
temp = 0
h = []
e = []
l = []
o = []
for i, char in enumerate(s):
    if char == 'h':
        h.append(i)
    elif char == 'e':
        e.append(i)
    elif char == 'l':
        l.append(i)
    elif char == 'o':
        o.append(i)
for i in h:
    for j in e:
        for k in l:
            for m in l:
                for n in o:
                    if i < j < k < m < n:
                        temp = 1
                        break
                if temp == 1:
                    break
            if temp == 1:
                break
        if temp == 1:
            break
    if temp == 1:
        break
if temp == 1:
    print('YES')
else:
    print('NO')