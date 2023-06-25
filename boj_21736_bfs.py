import sys
from collections import deque
input = sys.stdin.readline

total_count = 0

row,col = list(map(int, input().rstrip().split(" ")))
univ = []
start = []
for i in range(row):
    row_input = list(map(str, input().rstrip()))
    univ.append([])
    for j in range(len(row_input)):
        univ[i].append(row_input[j])
        if row_input[j] == "I":
            start = [i, j]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

visited = [[False for _ in range(col)] for _ in range(row)]

def bfs(st):
    global total_count
    que = deque([])
    que.append(st)
    visited[st[0]][st[1]] = True
    
    while len(que) != 0:
        cur = que.popleft()
        
        for i in range(4):
            next_row = cur[0] + dx[i]
            next_col = cur[1] + dy[i]
            if next_row < 0 or next_row > row - 1 or next_col < 0 or next_col > col - 1:
                continue
            if visited[next_row][next_col] == True:
                continue
            if univ[next_row][next_col] == "X":
                continue
            
            visited[next_row][next_col] = True
            if univ[next_row][next_col] == "P":
                total_count += 1
            que.append([next_row, next_col])
bfs(start)

if total_count == 0:
    print("TT")
else:
    print(total_count)