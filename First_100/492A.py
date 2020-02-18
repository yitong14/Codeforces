# 492A - vanya and cubes
n = int(input())
sum_ = 0
height = 1
while sum_ >= 0:
    for i in range(1, height+1):
        sum_ += i
    if sum_ == n:
        print(height)
        break
    if sum_ > n:
        print(height-1)
        break
    height += 1
