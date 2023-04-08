import sys
from pprint import pprint
from collections import deque
input = sys.stdin.readline

input_col, input_row = list(map(int, input().rstrip().split(" ")))
field = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(input_row):
    field.append(list(map(int, input().rstrip().split(" "))))

tomato_start = []

que = deque([])
for row in range(input_row):
    for col in range(input_col):
        if field[row][col] == 1:
            tomato_start.append([row, col])

for tomato in tomato_start:
    que.append(tomato)
    
while len(que) != 0:
    cur_x, cur_y = que.popleft()
    
    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]
        
        if nx < 0 or ny < 0 or nx >= input_row or ny >= input_col:
            continue
        
        if field[nx][ny] == -1:
            continue
        
        if field[nx][ny] == 0:
            field[nx][ny] = field[cur_x][cur_y] + 1
            que.append([nx, ny])
        else:
            if field[nx][ny] < field[cur_x][cur_y] + 1:
                continue
            elif field[nx][ny] > field[cur_x][cur_y] + 1:
                field[nx][ny] = field[cur_x][cur_y] + 1
                que.append([nx, ny])
max_num = 0
res = 0
for i in range(input_row):
    for j in range(input_col):
        if field[i][j] == 0:
            res = -1
        elif field[i][j] > max_num:
            max_num = field[i][j]

if res != -1:
    print(max_num -1)
else:
    print(-1)