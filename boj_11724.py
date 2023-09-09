import sys
from collections import deque

input = sys.stdin.readline

n, m = list(map(int, input().split(" ")))
connections = {}
visited = {}
for i in range(1,n + 1):
    visited[i] = False

for _ in range(m):
    f, t = list(map(int, input().split(" ")))
    if f in connections:
        connections[f].append(t)
    else:
        connections[f] = []
        connections[f].append(t)
    if t in connections:
        connections[t].append(f)
    else:
        connections[t] = []
        connections[t].append(f)
    visited[f] = False
    visited[t] = False

count = 0
    
# print(connections)
def bfs(key):
    global connections
    global count
    deq = deque([])
    visited[key] = True
    # print([key, connections[key]])
    for destination in connections[key]:
        deq.append(destination)
    
    while len(deq) != 0:
        cur = deq.popleft()
        if visited[cur] == True:
            continue
        for new_destination in connections[cur]:
            deq.append(new_destination)
        visited[cur] = True
    count += 1
    return

for key in connections:
    if visited[key] == False:
        bfs(key)

for v in visited:
    if visited[v] == False:
        count += 1
print(count)
