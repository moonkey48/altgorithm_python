import sys
from collections import deque
from pprint import pprint
input = sys.stdin.readline

n, m, start = list(map(int, input().rstrip().split(" ")))

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    f, t = list(map(int, input().rstrip().split(" ")))    
    graph[f].append(t)
    graph[t].append(f)

order = []
visited = [False for _ in range(n + 1)]
visited[start] = True

que = deque([])
que.append(start)
def dfs(start_node):
    global order
    global visited
    
    order.append(start_node)
    
    while len(que) != 0:
        cur_node = que.pop()
        for next_node in graph[cur_node]:
            if visited[next_node] == True:
                continue
            
            visited[next_node] = True
            que.append(next_node)
            dfs(next_node)
    

for p in graph:
    p.sort()
dfs(start)
print(" ".join(str(e) for e in order))


def bfs(start_node):
    order = []
    visited = [False for _ in range(n + 1)]
    visited[start_node] = True
    
    que = deque([])
    que.append(start_node)
    order.append(start_node)
    
    while len(que) != 0:
        cur_node = que.popleft()
        for next_node in graph[cur_node]:
            if visited[next_node] == True:
                continue
            
            order.append(next_node)
            visited[next_node] = True
            que.append(next_node)
    print(" ".join(str(e) for e in order))
bfs(start)

        
    