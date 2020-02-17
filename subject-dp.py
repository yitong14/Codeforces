# 01 - 爬楼梯 - dp
'''
def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return f(n-1) + f(n-2)


n = int(input())
print(f(n))
'''

# 02 - 最大子序和
'''
def f(nums):
    if len(nums) == 0:
        return 0
    d = [nums[0]]
    for i in range(1, len(nums)):
        d.append(max(nums[i], nums[i] + d[i-1]))
    return max(d)


num = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f(num))
'''

# 03 - 打家劫舍
'''
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
'''

# 04 - 买卖股票
'''
def f(nums):
    if len(nums) <= 1:
        return 0
    d = [0]
    for i in range(1, len(nums)):
        d.append(nums[i]-min(nums[:i]))
    return max(d)


num = list(map(int, input().split()))
print(f(num))
'''

# 05 - 比特位计数
'''
def f(num):
    if num == 0:
        return [0]
    d = [0]
    k = 0
    for i in range(1, num+1):
        if i == 2**k:
            d.append(1)
            k += 1
        else:
            d.append(1+d[i-2**k])
    return d


n = int(input())
print(f(n))
'''

# 06 - 三角形最小路径和
'''
def f(triangle):
    if len(triangle) == 1:
        return triangle[0][0]
    d = [[triangle[0][0]]]
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            d.append([])
            if j == 0:
                d[i].append(d[i-1][j]+triangle[i][j])
            elif j == len(triangle[i]) - 1:
                d[i].append(d[i-1][j-1]+triangle[i][j])
            else:
                d[i].append(min(d[i-1][j-1], d[i-1][j])+triangle[i][j])
    return min(d[len(triangle)-1])


n = int(input())
tri = []
for i in range(n):
    tri.append(list(map(int, input().split())))
print(f(tri))
'''

