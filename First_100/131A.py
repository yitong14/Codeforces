# 131A - cAPS lOCK

s = input()
if s[1:] == s[1:].upper():
    if s[0] == s[0].upper():
        print(s.lower())
    else:
        print(s[0].upper() + s[1:].lower())
else:
    print(s)
