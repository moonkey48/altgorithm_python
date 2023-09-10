import sys
from collections import deque

distance = [0 for _ in range(100_001)]
start, destination = list(map(int, input().split(" ")))

result = 0
def bfs(start, destination):
    global result
    deq = deque([])
    deq.append(start)
    while len(deq) != 0:
        cur = deq.popleft()
        if cur == destination:
            result = distance[cur]
            return
        for next in (cur -1 ,cur + 1, cur * 2):
            if 0 <= next <= 100_000 and not distance[next]:
                distance[next] = distance[cur] + 1
                deq.append(next)
    return

bfs(start, destination)
print(result)