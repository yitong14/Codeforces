# 455A - boredom
## a better solution
n = int(input())
s = [0]*100002
for i in map(int, input().split()):
    s[i] += i

a = b = 0
for d in s:
    a, b = max(a, b), a+d

print(a)


## my solution
n = int(input())
a = [int(i) for i in input().split()]

max_value = max(a)

cnt = (max_value+1)*[0]
for i in range(n):
    cnt[a[i]] += 1

f = (max_value+1)*[0]
f[0] = 0
f[1] = cnt[1]

for i in range(2, max_value+1):
    f[i] = max(f[i-1], f[i-2]+cnt[i]*i)

print(f[max_value])