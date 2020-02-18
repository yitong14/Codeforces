# 12559 - 最大最小整数
n = int(input())
nums = input().split()

for i in range(n-1):
    for j in range(i+1, n):
        if nums[i] + nums[j] < nums[j] + nums[i]:
            nums[i], nums[j] = nums[j], nums[i]

print(''.join(nums), ''.join(nums[::-1]))