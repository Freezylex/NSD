from math import fabs


def closest(sel, bomb, i):
    while i < len(bomb) - 1:
        if fabs(sel[0] - bomb[i][0]) >= fabs(sel[0] - bomb[i + 1][0]):
            i += 1
        else:
            break
    return sel[1], bomb[i][1], i

s = int(input())
num = 1
sel = []
for i in input().split():
    sel.append((int(i), num))
    num += 1
b = int(input())
num = 1
bomb = []
for i in input().split():
    bomb.append((int(i), num))
    num += 1
sel.sort()
bomb.sort()
i = 0
if s == 1:
    print(closest(sel[0], bomb, i)[1])
else:
    a = closest(sel[0], bomb, i)
    ans = []
    ans.append((a[0], a[1]))
    for j in sel[1:]:
        if a[2] < b - 1:
            a = closest(j, bomb, a[2])
            ans.append((a[0], a[1]))
        else:
            ans.append((j[1], bomb[-1][1]))
    for i in sorted(ans):
        print(i[1], end=' ')
