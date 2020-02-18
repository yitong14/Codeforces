# 230B - T-primes - 埃式筛法 - time limit exceed

t_prime = []
a = [i+1 for i in range(10**6)]
a[0] = False
for j in range(2, 10**6):
    if j**2 <= 10**6:
        for k in range(j+1, int(10**6//j)+2):
            if k*j < 10**6:
                a[j*k-1] = False


n = int(input())
nums = list(map(int, input().split()))
for num in nums:
    if num**0.5 in a:
        print('YES')
    else:
        print('NO')
