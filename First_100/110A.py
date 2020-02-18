# 110A - nearly lucky number
digits = list(input())
count = 0
for num in digits:
    if num == '4':
        count += 1
    elif num == '7':
        count += 1
if count == 4 or count == 7:
    print('YES')
else:
    print('NO')