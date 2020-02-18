# 158B - taxi
n = int(input())
members = input().split(' ')
one = 0
two = 0
three = 0
four = 0
for i, num in enumerate(members):
    if num == '1':
        one += 1
    elif num == '2':
        two += 1
    elif num == '3':
        three +=1
    else:
        four += 1
count = four + three
if two % 2 == 0:
    count += two // 2
    if one > three:
        if (one - three) % 4 == 0:
            count += (one - three) // 4
        else:
            count += (one - three) // 4 + 1
else:
    count += two // 2 + 1
    one -= 2
    if one > three:
        if (one - three) % 4 == 0:
            count += (one - three) // 4
        else:
            count += (one - three) // 4 + 1
print(count)