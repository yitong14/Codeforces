# 04 - 买卖股票

def f(nums):
    if len(nums) <= 1:
        return 0
    d = [0]
    for i in range(1, len(nums)):
        d.append(nums[i]-min(nums[:i]))
    return max(d)


num = list(map(int, input().split()))
print(f(num))
