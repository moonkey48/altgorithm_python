import sys
from collections import deque

input = sys.stdin.readline
n = int(input().rstrip())
dx = [0,0,-1,1]
dy = [1,-1,0,0]

groups = []
for _ in range(n):
    groups.append(list(input().rstrip()))

visited = [[False for _ in range(n)] for _ in range(n)]
visited_weakness = [[False for _ in range(n)] for _ in range(n)]

visited_group_count = 0
visited_weakness_group_count = 0

def find_group(x, y, color):
    global visited_group_count
    visited[y][x] = True
    que = deque([])
    que.append([x,y])
    
    while len(que) != 0:
        cur = que.popleft()
        for k in range(4):
            pos_y = cur[1] + dy[k]
            pos_x = cur[0] + dx[k]
            if pos_x < 0 or pos_y < 0 or pos_x > n - 1 or pos_y > n - 1:
                continue
            if visited[pos_y][pos_x] == True:
                continue
            if groups[pos_y][pos_x] != color:
                continue
            
            visited[pos_y][pos_x] = True
            que.append([pos_x, pos_y])
            
    visited_group_count += 1
     
def find_weakness_group(x, y, color):
    global visited_weakness_group_count
    visited_weakness[y][x] = True
    que = deque([])
    que.append([x,y])
    
    while len(que) != 0:
        cur = que.popleft()
        for k in range(4):
            pos_y = cur[1] + dy[k]
            pos_x = cur[0] + dx[k]
            if pos_x < 0 or pos_y < 0 or pos_x > n - 1 or pos_y > n - 1:
                continue
            if visited_weakness[pos_y][pos_x] == True:
                continue
            if color == 'R' or color == 'G':
                if groups[pos_y][pos_x] == 'B':
                    continue
            else:
                if groups[pos_y][pos_x] == 'R' or groups[pos_y][pos_x] == 'G':
                    continue
            
            visited_weakness[pos_y][pos_x] = True
            que.append([pos_x, pos_y])
            
    visited_weakness_group_count += 1

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            find_group(j, i, groups[i][j])
        if visited_weakness[i][j] == False:
            find_weakness_group(j, i, groups[i][j])

print(str(visited_group_count) + ' ' + str(visited_weakness_group_count))