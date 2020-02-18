# 18224 - 找魔数
x = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']


def to_b(y):
    nums = []
    while True:
        nums.append(str(y%2))
        y = y//2
        if y == 0:
            return '0b'+''.join(nums[::-1])


def to_o(y):
    nums = []
    while True:
        nums.append(str(y%8))
        y = y // 8
        if y == 0:
            return '0o'+''.join(nums[::-1])


def  to_x(y):
    nums = []
    while True:
        nums.append(x[y%16])
        y = y // 16
        if y == 0:
            return '0x'+''.join(nums[::-1])


def is_magic(y):
    max_ = int((y-1)**0.5)
    for i in range(1, max_+1):
        for j in range(i, max_+1):
            if y == i**2 + j**2:
                return True
    return False


m = int(input())
ns = [int(s) for s in input().split()]
out_ = []
for n in ns:
    if is_magic(n):
        out_.append(n)
for n in out_:
    print(to_b(n), to_o(n), to_x(n))