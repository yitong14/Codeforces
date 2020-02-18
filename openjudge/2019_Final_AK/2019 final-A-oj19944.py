# A - 这一天星期几
import math

n = int(input())
weekday = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday',
           5: 'Friday', 6: 'Saturday'}
month = [0, 13, 14, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
weeks = []
for i in range(n):
    nums = list(input())
    year = int(''.join(nums[:4]))
    m = month[int(''.join(nums[4:6]))]
    d = int(''.join(nums[6:]))
    if m == 13 or m == 14:
        year -= 1
    year = str(year)
    y = int(year[2:])
    c = int(year[:2])
    w = (y + math.floor(y/4) + math.floor(c/4) - 2*c + math.floor(26*(m+1)/10) + d - 1) % 7
    weeks.append(weekday[w])
for w in weeks:
    print(w)
