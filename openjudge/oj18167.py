# 18167 - 寻找周期
## my solution
n = int(input())
for k in range(n):
    s = input()
    cycle = ''
    for i in range(len(s)):
        cycle = cycle + s[i]
        if len(s)%len(cycle) == 0:
            if cycle * (len(s)//len(cycle)) == s:
                print(len(cycle))
                break

## a better solution
n = int(input())
for i in range(n):
    s = input()
    n = 0
    set1 = set()
    while len(set1) != 1:
        n += 1
        set1 = set(s.split(s[:n]))
        print(set1)
    print(n)