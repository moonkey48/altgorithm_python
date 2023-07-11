import sys
from collections import deque
v,e = list(map(int, input().rstrip().split(" ")))
startNode = int(input().rstrip())
graph = [[] for _ in range(v)]

for _ in range(e):
    f,t,w = list(map(int, input().rstrip().split(" ")))
    graph[f-1].append((t, w))
    
res = []
weights = [0 for _ in range(v)]
visited = [False for _ in range(v)]

que = deque([])
que.append(startNode)

while len(que) != 0:
    cur = que.popleft()
    for item in graph[cur - 1]:
        if weights[item[0]] == 0:
            weights[item[0]] = weights[cur] + item[1]
        else:    
            weights[item[0]] = min(weights[item[0]], weights[cur] + item[1])
        if visited[item[0]] == False:
            que.append(item[0]) 
        else:
            visited[item[0]] == True
            que.append(item[0]) 

for i in range(1,v + 1):
    if i == startNode:
        print(0)
    elif weights[i] == 0:
        print("INF")
    else:
        print(weights[i])