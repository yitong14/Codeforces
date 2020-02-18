# 579A -raising bacteria
x = int(input())
num = 0
while x > 0:
    num += x % 2
    x = x // 2
print(num)