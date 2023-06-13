import sys
from collections import deque
input = sys.stdin.readline

row, col, total_count = list(map(int, input().rstrip().split(" ")))

place = [[0 for _ in range(col)] for _ in range(row)]
visited = [[False for _ in range(col)] for _ in range(row)]

for _ in range(total_count):
    top, left = list(map(int, input().rstrip().split(" ")))
    place[top - 1][left - 1] = 1

max_trash = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def find(r, c):
    global max_trash
    cur_trash_count = 0
    que = deque([])
    que.append([r, c])
    visited[r][c] == True
    
    while len(que) != 0:
        cur = que.popleft()
        for k in range(4):
            cx = cur[0] + dx[k]
            cy = cur[1] + dy[k]
            
            if cx < 0 or cy < 0 or cx > row - 1 or cy > col - 1:
                continue
            if visited[cx][cy] == True:
                 continue
            if place[cx][cy] == 0:
                continue
            
            visited[cx][cy] = True
            que.append([cx, cy])
            cur_trash_count += 1
            
    max_trash = max(max_trash, cur_trash_count)

     
    


for i in range(row):
    for j in range(col):
        if place[i][j] == 1:
            find(i, j)
        
        
print(max_trash)
# print(place)
    