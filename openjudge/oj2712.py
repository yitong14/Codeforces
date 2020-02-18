# 2712 - 细菌繁殖
n = int(input())
month = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
nums = [input() for i in range(n)]
for nu in nums:
    ms, ds, num, me, de = map(int, nu.split())
    start = month[ms]+ds
    end = month[me]+de
    print(int(num*(2**(end-start))))