# 12557 - 比较版本
version1 = [int(s) for s in input().split('.')]
version2 = [int(s) for s in input().split('.')]
for v1, v2 in zip(version1, version2):
    if v1 > v2:
        print('.'.join([str(s) for s in version1]))
        break
    elif v2 > v1:
        print('.'.join([str(s) for s in version2]))
        break