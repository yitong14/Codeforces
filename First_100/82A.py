# 82A - double cola
n = int(input())
names = {1: 'Sheldon', 2:'Leonard', 3:'Penny', 4:'Rajesh', 5:'Howard'}
r = 0
while n > 0:
    for j in range(1, 6):
        name = j
        n -= 2**r
        if n <= 0:
            break
    r += 1
print(names[name])