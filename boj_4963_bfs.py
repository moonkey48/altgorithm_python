import sys
from collections import deque
input = sys.stdin.readline

island_count = 0

dx = [0,0,1,-1,1,-1,-1,1]
dy = [1,-1,0,0,1,-1,1,-1]
islands_map = []
res_list = []
def find_island(pos, x, y):
    que = deque([])
    que.append(pos)
    
    while len(que) != 0:
        cur_pos = que.popleft()
        for i in range(8):
            cur_x = cur_pos[0] + dx[i]
            cur_y = cur_pos[1] + dy[i]
            if cur_x < 0 or cur_y < 0 or cur_x >= x or cur_y >= y:
                continue
            if visited[cur_x][cur_y] == True:
                continue
            if islands_map[cur_x][cur_y] == 0:
                continue
            
            visited[cur_x][cur_y] = True
            que.append([cur_x, cur_y])
    

while True:
    island_count = 0
    islands_map = []
    y, x = list(map(int, input().rstrip().split(" ")))
    if x == 0 and y == 0:
        break
    
    islands_map = []
    for i in range(x):
        islands_map.append(list(map(int, input().rstrip().split(" "))))
    
    visited = [[False for j in range(int(y))] for i in range(int(x))]
    
    for i in range(x):
        for j in range(y):
            if visited[i][j] == True:
                continue
            if islands_map[i][j] == 0:
                continue
            
            visited[i][j] == True
            island_count += 1
            find_island([i, j], x ,y)
    
    res_list.append(island_count)


for res in res_list:
    print(res)
                
                        
    
    