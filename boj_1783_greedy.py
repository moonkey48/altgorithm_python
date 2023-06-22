import sys
from collections import deque
row, col = list(map(int, sys.stdin.readline().rstrip().split(" ")))

board = [[False for _ in range(col)] for _ in range(row)]

dx = [1, 2, 2, 1]
dy = [-2, -1, 1, 2]

que = deque([])
que.append([0,0])
board[0][0] = True
count = 1

while len(que) != 0:
    cur = que.popleft()
    
    for i in range(4):
        r = cur[0] + dy[i]
        c = cur[1] + dx[i]
        
        if r < 0 or c < 0 or r > row - 1 or c > col - 1:
            continue
        if board[r][c] == True:
            continue
        
        count += 1
        board[r][c] = True
        que.append([r, c])
print(count)