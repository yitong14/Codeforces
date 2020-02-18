# 18182 - 打怪兽
ncases = int(input())
for i in range(ncases):
    n, m, b = map(int, input().split())
    skills = [list(map(int, input().split())) for j in range(n)]
    skills.sort(key=lambda x: (x[0], -x[1]))
    t0 = skills[0][0]
    cur_skill = []
    for k in skills:
        if k[0] == t0:
            cur_skill.append(k[1])
            continue
        b -= sum(cur_skill[:min(m, len(cur_skill))])
        if b <= 0:
            break
        t0 = k[0]
        cur_skill = [k[1]]
    else:
        b -= sum(cur_skill[:min(m, len(cur_skill))])
    if b > 0:
        print('alive')
    else:
        print(t0)
