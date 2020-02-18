# 337A - puzzles

n, m = map(int, input().split())
nums = input().split(' ')
nums_int = [int(n) for n in nums]
nums_int.sort()
diff = nums_int[-1] - nums_int[0]
for i in range(m - n + 1):
    current_diff = nums_int[i + n - 1] - nums_int[i]
    if current_diff < diff:
        diff = current_diff
print(diff)
