# 4C - registration system

n = int(input())
names = {}
output = ['OK' for i in range(n)]
for i in range(n):
    name = input()
    if name not in names.keys():
        names.update({name: 1})
    else:
        output[i] = name + str(names[name])
        names[name] = names[name] + 1
for out in output:
    print(out)
