# 12555 - 寻找四分位数
import math

n = int(input())
samples = list(map(float, input().split()))
samples.sort()
h = (n-1)/4+1
h_ = math.floor((n-1)/4+1)
print('{:.2f}'.format(samples[h_-1]+(h-h_)*(samples[h_] - samples[h_-1])))
h = 2*(n-1)/4+1
h_ = math.floor(2*(n-1)/4+1)
print('{:.2f}'.format(samples[h_-1]+(h-h_)*(samples[h_] - samples[h_-1])))
h = 3*(n-1)/4+1
h_ = math.floor(3*(n-1)/4+1)
print('{:.2f}'.format(samples[h_-1]+(h-h_)*(samples[h_] - samples[h_-1])))