# 703A - mishka and game
n = int(input())
winner = {1: 'Mishka', 2: 'Chris', 3: 'Friendship is magic!^^'}
count = 0
for i in range(n):
    a, b = map(int, input().split())
    if a-b > 0:
        count += 1
    elif a-b < 0:
        count -= 1
if count > 0:
    print(winner[1])
elif count < 0:
    print(winner[2])
else:
    print(winner[3])