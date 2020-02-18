# 27A - beautiful year

start = int(input())
year = start + 1
while year > start:
    year_digits = set(str(year))
    if len(year_digits) == 4:
        print(year)
        break
    year += 1
