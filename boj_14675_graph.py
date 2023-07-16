import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]
lines = []
for _ in range(n - 1):
    f,t = list(map(int, input().rstrip().split(" ")))
    tree[f].append(t)
    lines.append([f,t])

q_n = int(input())

def bfs_point(start, cutted_point):
    total_length = 1
    visited = [False for _ in range(n + 1)]
    que = deque([])
    que.append(start)
    visited[start] = True
    while len(que) != 0:
        cur = que.popleft()
        for connected_point in tree[cur]:
            if connected_point == cutted_point:
                continue
            if visited[connected_point] == False:
                que.append(connected_point)
                total_length += 1
            
    return total_length
def bfs_line(start, cutted_line):
    total_length = 1
    visited = [False for _ in range(n + 1)]
    que = deque([])
    que.append(start)
    visited[start] = True
    while len(que) != 0:
        cur = que.popleft()
        for connected_point in tree[cur]:
            
            if visited[connected_point] == False:
                que.append(connected_point)
                total_length += 1
            
    return total_length

res = []
for _ in range(q_n):
    q, point = list(map(int, input().rstrip().split(" ")))
    if q == 1:
        if len(tree) != bfs_point(1, point):
            res.append("no")      
        else:
            res.append("yes")
    else:
              
    