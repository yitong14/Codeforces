# 2796 - 数字求和
nums = [int(s) for s in input().split()]
cnt = 0
for i in range(1, 6):
    if nums[i] < nums[0]:
        cnt += nums[i]
print(cnt)