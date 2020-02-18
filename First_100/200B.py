# 200B - drinks

n = int(input())
fractions = list(map(int, input().split()))
print('{:.8}'.format(sum(fractions)/len(fractions)))
