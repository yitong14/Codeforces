# 2746 - 约瑟夫问题
while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    cnt = 0
    i = 0
    monkey = [1]*n
    while True:
        if i == n:
            i -= n
        if monkey[i] == 1:
            cnt += 1
            if cnt == m:
                monkey[i] = 0
                cnt = 0
        i += 1
        if sum(monkey) == 1:
            print(monkey.index(1)+1)
            break