import sys
from collections import deque
input = sys.stdin.readline

h, start, destination, up, down = list(map(int, input().rstrip().split(" ")))

que = deque([])
que.append(start)

dx = [up, -down]

buildings = [-1 for _ in range(h + 1)]
buildings[start] += 1
while len(que) != 0:
    cur = que.popleft()
    for i in range(2):
        next = cur + dx[i]
        if next < 1 or next > h:
            continue
        if buildings[next] == -1:
            buildings[next] = buildings[cur] + 1
            print(next)
            que.append(next)
        elif buildings[next] != buildings[cur] + 1:
            print(next)
            buildings[next] = min(buildings[next], buildings[cur] + 1)

if buildings[destination] == -1:
    print("use the stairs")
else:
    print(buildings[destination])