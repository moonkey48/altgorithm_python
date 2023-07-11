import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]
for i in range(n):
    for str in input().rstrip():
        graph[i].append(int(str))

visited = [[False for _ in range(n)] for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

res = []

def bfs(row, col):
    que = deque([])
    count = 1
    
    que.append([row, col])
    while len(que) != 0:
        cur = que.popleft()
        for k in range(4):
            if cur[0] + dx[k] < 0 or cur[0] + dx[k] > n - 1 or cur[1] + dy[k] < 0 or cur[1] + dy[k] > n -1:
                continue
            if graph[cur[0] + dx[k]][cur[1] + dy[k]] == 0:
                continue
            if visited[cur[0] + dx[k]][cur[1] + dy[k]] == True:
                continue
            visited[cur[0] + dx[k]][cur[1] + dy[k]] = True
            que.append([cur[0] + dx[k], cur[1] + dy[k]])
            count += 1
    res.append(count)
    
    

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            continue
        if visited[i][j] == True:
            continue
        visited[i][j] = True
        bfs(i, j)
print(len(res))
res.sort()
for r in res:
    print(r)

    