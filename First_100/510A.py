# 510A - fox and snake

n, m = map(int, input().split())
for i in range(n):
    if i % 2 == 0:
        print('#'*m)
    elif (i//2) % 2 == 0:
        print('.'*(m-1) + '#')
    else:
        print('#' + '.'*(m-1))
