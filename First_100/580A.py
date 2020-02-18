# 580A - kefa and first steps
n = int(input())
nums = input().split()
num = [int(n) for n in nums]
count = 1
current_count = 1
for i, a in enumerate(num):
    if i > 0:
        if a >= num[i - 1]:
            current_count += 1
        else:
            current_count = 1
        if current_count > count:
            count = current_count
print(count)
