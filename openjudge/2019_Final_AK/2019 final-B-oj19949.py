# B - 提取实体
n = int(input())
cnt = 0
for i in range(n):
    words = input().split()
    words_ = [1 if '###' in w else 0 for w in words]
    temp = 0
    for j in range(len(words)):
        if words_[j] == 0:
            temp = 0
        else:
            if temp == 0:
                cnt += 1
            temp = 1

print(cnt)
