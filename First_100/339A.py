# 05 - 339A - helpful maths

s = input()
if len(s) == 1:
    print(s)
else:
    number = s.split("+")
    numbers = [int(number[i]) for i in range(len(number))]
    numbers.sort()
    numberss = [str(numbers[i]) for i in range(len(number))]
    print("+".join(numberss))
