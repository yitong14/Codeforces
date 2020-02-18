# 479A - expression

a = int(input())
b = int(input())
c = int(input())
result_1 = a * b * c
result_2 = a + b + c
result_3 = (a + b) * c
result_4 = (b + c) * a
result_5 = a + b * c
result_6 = a * b + c
print(max(result_1, result_2, result_3, result_4, result_5, result_6))
