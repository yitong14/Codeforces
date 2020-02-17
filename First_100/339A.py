# 339A - helpful maths

nums = input().split('+')
num = [int(n) for n in nums]
num.sort()
new_num = [str(n) for n in num]
s = "+".join(new_num)
print(s)
