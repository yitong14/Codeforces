# 02 - 最大子序和

def f(nums):
    if len(nums) == 0:
        return 0
    d = [nums[0]]
    for i in range(1, len(nums)):
        d.append(max(nums[i], nums[i] + d[i-1]))
    return max(d)


num = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f(num))
