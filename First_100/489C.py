# 02 - 489C - given length and sum of digits

m, s = map(int, input().split())
if s == 0 and m == 1:
    print(0, 0)
elif s == 0:
    print(-1, -1)
elif m * 9 < s:
    print(-1, -1)
else:
    nums = []
    while len(nums) < m:
        nums.append(min(9, s))
        s = s - min(9, s)
    max_nums = [str(i) for i in nums]
    max_num = ''.join(max_nums)
    min_nums = nums[::-1]
    if min_nums[0] == 0:
        for j, num in enumerate(min_nums):
            if num != 0:
                min_nums[j] = num - 1
                break
        min_nums[0] = 1
    min_nums = [str(i) for i in min_nums]
    min_num = ''.join(min_nums)
    print(min_num, max_num)
