# 136A - presents

n = int(input())
seq = [int(n) for n in input().split()]
new_seq = []
for i in range(n):
    new_seq.append(str(seq.index(i + 1) + 1))
print(' '.join(new_seq))
