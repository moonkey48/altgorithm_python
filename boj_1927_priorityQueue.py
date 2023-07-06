import sys
from queue import PriorityQueue

input = sys.stdin.readline
que = PriorityQueue()

n = int(input())
res = []
for _ in range(n):
    num = int(input())
    if num == 0:
        if que.empty():
            res.append(0)
        else:
            res.append(que.get())
    else:
        que.put(num)

for r in res:
    print(r)