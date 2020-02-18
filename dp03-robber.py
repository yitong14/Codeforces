# 03 - 打家劫舍

def f(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) <=2:
        return max(nums)
    d = [nums[0],  max(nums[0], nums[1])]
    for i in range(2, len(nums)):
        d.append(max(d[i-1], d[i-2] + nums[i]))
    return d[-1]


num = list(map(int, input().split()))
print(f(num))
