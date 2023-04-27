import sys
from collections import deque
input = sys.stdin.readline

dx = [2,1,-1,-2,-2,-1,1,2]
dy = [1,2,2,1,-1,-2,-2,-1]

n = int(input())
answer = []

def bfs(size, f, t):
    visited = [[False for j in range(int(size))] for i in range(int(size))]
    distance = [[False for j in range(int(size))] for i in range(int(size))]
    des_pos = t
    que = deque()
    que.append(f)
    visited[f[0]][f[1]] = True
    distance[f[0]][f[1]] = 0
    
    while len(que) != 0:
        x, y = que.popleft()
        
        for i in range(8):
            next_x = x + dx[i]
            next_y = y + dy[i]
            
            
            if next_x < 0 or next_y < 0 or next_x > size - 1 or next_y > size - 1:
                continue
            if visited[next_x][next_y] == True:
                continue
            
            visited[next_x][next_y] = True
            distance[next_x][next_y] = distance[x][y] + 1
            que.append([next_x, next_y]) 
    
    
    answer.append(distance[des_pos[0]][des_pos[1]])

for i in range(n):
    s = int(input())
    knite_from = list(map(int, input().rstrip().split(" ")))
    knite_to = list(map(int, input().rstrip().split(" ")))
    bfs(s, knite_from, knite_to)
    

for item in answer:
    print(item)
