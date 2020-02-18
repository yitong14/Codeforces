# 41A - translation

s = list(input())
t = input()
s.reverse()
st = ''.join(s)
if st == t:
    print('YES')
else:
    print('NO')
