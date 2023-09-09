import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
c = int(input())

computers = {}

for _ in range(c):
    f, t = list(map(int, input().split(" ")))
    if f in computers:
        computers[f].append(t)
    else:
        computers[f] = []
        computers[f].append(t)
        
    if t in computers:
        computers[t].append(f)
    else:
        computers[t] = []
        computers[t].append(f)

visited = {}
for i in range(1,n + 1):
    visited[i] = False

def bfs(key):
    que = deque([])
    visited[key] = True
    if key in computers:
        for t in computers[key]:
            que.append(t)
    
    while len(que) != 0:
        cur = que.popleft()
        if cur in visited:
            if visited[cur] == True:
                continue
            visited[cur] = True
            if cur in computers:
                for destination in computers[cur]:
                    que.append(destination)
    
bfs(1)
count = 0
for res in visited:
    if visited[res] == True:
        count +=1
print(count - 1)