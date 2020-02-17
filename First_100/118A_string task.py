# 118A - string task

s = input().lower()
strings = list(s)
new_strings = []
vowels = ['a', 'o', 'y', 'e', 'u', 'i']
for i, char in enumerate(strings):
    if char in vowels:
        continue
    else:
        new_strings.append('.')
        new_strings.append(char)
print(''.join(new_strings))
