import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,1,-1,1,-1,1,-1]
dy = [1,-1,0,0,-1,1,1,-1]

lands_counts = []
while True:
    y, x = list(map(int, input().rstrip().split(" ")))
    if y == 0 and x == 0:
        break
    lands_count = 0
    
    lands = []
    visited = [[False for j in range(int(y))] for i in range(int(x))]
    for i in range(x):
        lands.append(list(map(int, input().rstrip().split(" "))))
    
    for i in range(x):
        for j in range(y):
            if visited[i][j] == True:
                continue
            if lands[i][j] == 0:
                continue
            
            
            que = deque([])
            que.append([i,j])
            lands_count += 1
            
            while len(que) != 0:
                new_land = que.popleft()
                for k in range(8):
                    cur_x = new_land[0] + dx[k]
                    cur_y = new_land[1] + dy[k]
                    
                    if cur_x < 0 or cur_y < 0 or cur_x >= x or cur_y >= y:
                        continue
                    if visited[cur_x][cur_y] == True:
                        continue
                    if lands[cur_x][cur_y] == 0:
                        continue
                    
                    visited[cur_x][cur_y] = True
                    que.append([cur_x,cur_y])
    lands_counts.append(lands_count)

for c in lands_counts:
    print(c)                

