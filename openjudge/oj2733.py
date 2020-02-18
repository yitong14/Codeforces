# 2733 - 判断闰年
n = int(input())
if n % 4 == 0 and n % 100 != 0:
    print('Y')
elif n % 400 == 0:
    print('Y')
else:
    print('N')