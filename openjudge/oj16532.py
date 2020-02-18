# 16532 - 北大杯台球比赛
w1, w2 = map(int, input().split())
b1, b2 = map(int, input().split())
m1, m2 = map(int, input().split())
energy = int(input())
k = -1
if energy == 0:
    print(0)
else:
    while True:
        if energy == 0:
            print(0)
            break
        energy -= 1
        if 0 <= w1+m1 <= 16:
            w1 += m1
        else:
            w1 = w1-m1
            m1 = -m1
        if 0 <= w2+m2 <= 5:
            w2 += m2
        else:
            w2 = w2-m2
            m2 = -m2
        if w1 == b1 and w2 == b2:
            k = -k
        if w1 == 0 or w1 == 8 or w1 == 16:
            if w2 == 0 or w2 == 5:
                print(k)
                break