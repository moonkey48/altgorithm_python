import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
stones = list(map(int, input().rstrip().split(" ")))
visited = [0] * n 
start = int(input())

que = deque([])
que.append(start - 1)

while len(que) > 0:
    cur_pos = que.popleft()
    visited[cur_pos] += 1
    if cur_pos + stones[cur_pos] <= n - 1 and visited[cur_pos + stones[cur_pos]] == 0:
        que.append(cur_pos + stones[cur_pos])
    if cur_pos - stones[cur_pos] >= 0 and visited[cur_pos - stones[cur_pos]] == 0:
        que.append(cur_pos - stones[cur_pos])

count = 0
for i in visited:
    if i != 0:
        count += 1
print(count)