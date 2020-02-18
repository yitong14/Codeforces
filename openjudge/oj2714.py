# 2714 - 求平均年龄
n = int(input())
age = [int(input()) for i in range(n)]
print('{:.2f}'.format(sum(age)/n))