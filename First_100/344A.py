# 344A - magnets

n = int(input())
group = 1
a = input()
for i in range(n-1):
    b = input()
    if a != b:
        group += 1
    a = b
print(group)
