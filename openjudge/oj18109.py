# 18109 - 最频繁字符
s = list(input().lower())
count = {}
for i in s:
    if i in count.keys():
        count[i] += 1
    else:
        count.update({i: 1})
max_ = max(list(count.values()))
for i in count.keys():
    if count[i] == max_:
        print(i, count[i])
        break