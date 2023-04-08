import sys
from collections import deque
from pprint import pprint
import copy


input = sys.stdin.readline

input_row, input_col = list(map(int, input().rstrip().split(" ")))

maze = []
maze_j = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(input_row):
    maze.append(list(input().rstrip()))

maze_j = copy.deepcopy(maze)
pos_j = []
pos_f = []

for i in range(input_row):
    for j in range(input_col):
        if maze[i][j] == 'J':
            pos_j = [i,j]
        elif maze[i][j] == 'F':
            pos_f.append([i,j])

queue = deque([])

if pos_f:
    for fire in pos_f:
        queue.append(fire)        
        maze[fire[0]][fire[1]] = 0
    while len(queue) != 0:
        cur_x, cur_y = queue.popleft()
        
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            
            if nx < 0 or ny <0 or nx >= input_row or ny >= input_col:
                continue     
            if maze[nx][ny] == "#":
                continue
            
            if maze[nx][ny] == '.' or maze[nx][ny] == 'J':
                maze[nx][ny] = maze[cur_x][cur_y] + 1
                queue.append([nx, ny])
            elif isinstance(maze[nx][ny], int):
                if maze[nx][ny] > maze[cur_x][cur_y] + 1:
                    maze[nx][ny] = maze[cur_x][cur_y] + 1
                    queue.append([nx, ny])
else:
    for i in range(input_row):
        for j in range(input_col):
            if maze[i][j] == '.':
                maze[i][j] = 10000

maze_j[pos_j[0]][pos_j[1]] = 0
visited = [[False for j in range(int(input_col))] for i in range(int(input_row))]
visited[pos_j[0]][pos_j[1]] = True
res = []

queue.append(pos_j)
while len(queue) != 0:
    cur_x, cur_y = queue.popleft()
    if cur_x == input_row -1 or cur_x == 0 or cur_y == input_col -1 or cur_y == 0:
                res.append(maze_j[cur_x][cur_y])                
    
    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]
        
        
        if nx < 0 or ny <0 or nx >= input_row or ny >= input_col:
            continue     
        elif maze[nx][ny] == "#":
            continue
        elif visited[nx][ny] == True:
            continue
        # elif maze_j[nx][ny] == 'F':
        #     continue        
        
        if maze_j[nx][ny] == '.':
            if maze[nx][ny] == '.':
                queue.append([nx, ny])
                visited[nx][ny] = True
                maze_j[nx][ny] = maze_j[cur_x][cur_y] + 1
                if nx == input_row -1 or nx == 0 or ny == input_col -1 or ny == 0:
                    res.append(maze_j[nx][ny])                
            elif maze[nx][ny] > maze_j[cur_x][cur_y] + 1:
                queue.append([nx, ny])
                visited[nx][ny] = True
                maze_j[nx][ny] = maze_j[cur_x][cur_y] + 1
                if nx == input_row -1 or nx == 0 or ny == input_col -1 or ny == 0:
                    res.append(maze_j[nx][ny])                

if len(res) != 0:
    print(min(res) + 1)    
else: 
    print("IMPOSSIBLE")





