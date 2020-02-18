# 455A - boredom - time limit exceed

def f(nums):
    if len(nums) == 0:
        return 0
    counts = {}
    for i in range(max(nums)+1):
        if i in nums:
            counts.update({i:nums.count(i)})
        else:
            counts.update({i: 0})
    d = [0, counts[1]]
    for i in range(2, max(nums)+1):
        d.append(max(d[i-1], d[i-2]+counts[i]*i))
    return d[-1]


n = int(input())
num = list(map(int, input().split()))
print(f(num))
