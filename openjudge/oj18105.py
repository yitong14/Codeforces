# 18105 - h指数
nums = [int(s) for s in input().split()]
nums.sort()
n = len(nums)
res = 0
for i in range(n):
    h = n-i
    if nums[i] >= h:
        print(h)
        break