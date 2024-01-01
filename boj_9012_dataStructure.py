import sys

input = sys.stdin.readline

n = int(input())
ps_list = [input().rstrip() for _ in range(n)]

for ps in ps_list:
    psCount = 0
    for i in range(0, len(ps)):
        if ps[i] == '(':
            psCount += 1
        else:
            psCount -= 1
            if psCount < 0:
                break
    if psCount == 0:
        print("YES")
    else:
        print("NO")
                