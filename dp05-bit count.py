# 05 - 比特位计数

def f(num):
    if num == 0:
        return [0]
    d = [0]
    k = 0
    for i in range(1, num+1):
        if i == 2**k:
            d.append(1)
            k += 1
        else:
            d.append(1+d[i-2**k])
    return d


n = int(input())
print(f(n))
