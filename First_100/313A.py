# 313A - ilya and bank account
n = int(input())
if n >= 0:
    print(n)
else:
    n = str(-n)
    if n[-1] >= n[-2]:
        print('-'+n[:-1])
    else:
        if n[:-2] + n[-1] == '0':
            print(0)
        else:
            print('-'+n[:-2]+n[-1])