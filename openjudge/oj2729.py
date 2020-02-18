# 2729 - 求12以内n的阶乘
n = int(input())
resul = 1
for i in range(1, n+1):
    resul = resul * i
print(resul)
