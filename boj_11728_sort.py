import sys
input = sys.stdin.readline

n, m = list(map(int, input().rstrip().split(" ")))
list_n  = list(map(int, input().rstrip().split(" ")))
list_m = list(map(int, input().rstrip().split(" ")))

cur_n = 0
cur_m = 0
res = []

while cur_n < n or cur_m < m:
    if cur_m == m:
        res.append(list_n[cur_n])
        cur_n += 1
    elif cur_n == n:
        res.append(list_m[cur_m])
        cur_m += 1
    elif list_m[cur_m] < list_n[cur_n]:
        res.append(list_m[cur_m])
        cur_m += 1
    elif list_m[cur_m] >= list_n[cur_n]:
        res.append(list_n[cur_n])
        cur_n += 1
print(" ".join(list(map(str, res))))