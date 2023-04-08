from pprint import pprint
import sys
from collections import deque

input = sys.stdin.readline

input_x, input_y = input().rstrip().split(" ")

pictures = []
visited = [[False for j in range(int(input_y))] for i in range(int(input_x))]
max_size = 0
pictures_count = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(int(input_x)):
    input_picture = list(map(int, input().split(" ")))
    pictures.append(input_picture)

for cur_x in range(int(input_x)):
    for cur_y in range(int(input_y)):
        if visited[cur_x][cur_y] == True:
            continue
        if pictures[cur_x][cur_y] == 0:
            continue
        
        queue = deque([])
        cur_size = 0
        visited[cur_x][cur_y] = True
        queue.append([cur_x,cur_y])
        pictures_count += 1

        
        while len(queue) != 0:
            cur_pos = queue.popleft()
            cur_size += 1
            
            for i in range(4):
                
                nx = cur_pos[0] + dx[i]
                ny = cur_pos[1] + dy[i]
                
                if nx < 0 or ny < 0 or nx >= int(input_x) or ny >= int(input_y):
                    continue
                
                if visited[nx][ny] == False and pictures[nx][ny] == 1:
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                    
            if max_size < cur_size:
                max_size = cur_size
        
print(pictures_count)
print(max_size)