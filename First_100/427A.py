# 427A - police recruits
n = int(input())
crimes = list(map(int, input().split()))
count = 0
police = 0
for c in crimes:
    police += c
    if police < 0:
        count += 1
        police = 0
print(count)