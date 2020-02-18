# 122A - lucky division
lucky_number = [4, 7,
                44, 47, 74, 77,
                444, 447, 474, 744,
                477, 747, 774, 777]
n = int(input())
if n in lucky_number:
    print('YES')
else:
    temp = 0
    for num in lucky_number:
        if n % num == 0:
            print('YES')
            temp = 1
            break
        if num > n:
            break
    if temp == 0:
        print('NO')
