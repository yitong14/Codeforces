# 96A - football
## my solution
s = list(input())
count = 1
temp = 0
for i, num in enumerate(s):
    if i > 0:
        if num == s[i - 1]:
            count += 1
        if count >= 7:
            temp = 1
            print('YES')
            break
        if num != s[i - 1]:
            count = 1
if temp == 0:
    print('NO')

## a better solution
s = input()
if s.find('0000000') == -1 and s.find('1111111') == -1:
    print('NO')
else:
    print('YES')




