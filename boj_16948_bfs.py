import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
row_start, col_start, row_end, col_end = list(map(int, input().rstrip().split(" ")))

chess = [[-1 for _ in range(n)] for _ in range(n)]

que = deque([])
chess[row_start][col_start] += 1
que.append([row_start, col_start])

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]
while len(que) != 0:
    cur = que.popleft()
    for i in range(6):
        temp_x = cur[0] + dx[i]
        temp_y = cur[1] + dy[i]
        if  temp_x < 0 or temp_x > n - 1 or temp_y < 0 or temp_y > n - 1:
            continue
        
        if chess[temp_x][temp_y] == -1:
            chess[temp_x][temp_y] = chess[cur[0]][cur[1]] + 1
            que.append([temp_x, temp_y])
        elif chess[temp_x][temp_y] != chess[cur[0]][cur[1]] + 1:
            chess[temp_x][temp_y] = min(chess[temp_x][temp_y],chess[cur[0]][cur[1]] + 1)
            
print(chess[row_end][col_end])                
        
