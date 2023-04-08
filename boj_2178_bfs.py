import sys
from collections import deque

input = sys.stdin.readline

input_x, input_y = input().split(" ")
visited = [[False for j in range(int(input_y))] for i in range(int(input_x))]
length = [[0 for j in range(int(input_y))] for i in range(int(input_x))]
maze = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(int(input_x)):
    line = list(map(int, input().rstrip()))
    maze.append(line)

que = deque([])
que.append([0,0])
visited[0][0] = True
length[0][0] = 1

while len(que) != 0:
    cur_x, cur_y = que.popleft()
    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]
        
        if nx < 0 or ny < 0 or nx >= int(input_x) or ny >= int(input_y):
            continue
        if maze[nx][ny] == 0:
            continue
        
        if visited[nx][ny] == True:
            continue
        
        
        length[nx][ny] = length[cur_x][cur_y] + 1
        visited[nx][ny] = True
        if nx == int(input_x) and ny == int(input_y):
            break
        que.append([nx, ny])
        
print(length[int(input_x) -1][int(input_y) -1])