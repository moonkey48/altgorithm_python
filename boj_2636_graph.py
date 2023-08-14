import sys
from collections import deque
from pprint import pprint

input = sys.stdin.readline

max_row, max_col = list(map(int, input().rstrip().split(" ")))

board = []

for row in range(max_row):
    board.append(list(map(int, input().rstrip().split(" "))))

count_board  = [[100 for _ in range(max_col)] for _ in range(max_row)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(r, c):
    global board
    global count_board
    
    que = deque([])
    que.append([r,c])
    
    while len(que) != 0:
        cur = que.popleft()
        for i in range(4):
            cur_x = cur[0] + dx[i]
            cur_y = cur[1] + dy[i]
            if cur_x < 1 or cur_x > max_row - 1 or cur_y < 1 or cur_y > max_col - 1:
                continue
            if board[cur_x][cur_y] == 0:
                continue
            if count_board[cur_x][cur_y] > count_board[cur[0]][cur[1]] + 1:
                continue
            
            count_board[cur_x][cur_y] = count_board[cur[0]][cur[1]] + 1
            que.append([cur_x, cur_y])
    return


for row in range(max_row):
    for col in range(max_col):
        if board[row][col] == 0:
            continue
        count_board[row][col] = 1
        bfs(row, col)

pprint(count_board)