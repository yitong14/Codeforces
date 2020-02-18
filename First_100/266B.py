# 266B - queue at the school
## my solution
n, t = map(int, input().split())
queue = list(input())
for j in range(t):
    i = 0
    while i < n - 1:
        if queue[i] == 'B' and queue[i+1] == 'G':
            queue[i], queue[i+1] = 'G', 'B'
            i += 1
        i += 1
print(''.join(queue))

## a better solution
n, t = [int(x) for x in input().split()]
L = input()
for i in range(t):
    L = L.replace('BG','GB')

print(L)
