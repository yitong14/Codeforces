# 12556 - 编码字符串
s = list(input().lower())
a = s[0]
cnt = 1
zzz = []
for i in range(1, len(s)):
    if s[i] == a:
        cnt += 1
    else:
        zzz.append([a, cnt])
        a = s[i]
        cnt = 1
zzz.append([a, cnt])
for row in zzz:
    print('({},{})'.format(row[0], row[1]), end='')
