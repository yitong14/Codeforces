# 02 - 59A - word

s = input()
length = len(s)
l = list(s)
uppercase = 0
lowercase = 0
for i in range(length):
    if l[i].islower():
        lowercase += 1
    else:
        uppercase += 1
if uppercase > lowercase:
    print(s.upper())
else:
    print(s.lower())
