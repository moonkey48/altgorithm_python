import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]


test_count = int(input())
res_list = []

def find_worm():
    worm_count = 0
    x_length, y_length, vegetable_num = list(map(int, input().rstrip().split(" ")))
    visited = [[False for i in range(x_length)] for j in range(y_length)]
    ground_map = [[0 for i in range(x_length)] for j in range(y_length)]
    for i in range(vegetable_num):
        x, y = list(map(int, input().rstrip().split(" ")))
        ground_map[y][x] = 1
    for i in range(y_length):
        for j in range(x_length):
            if ground_map[i][j] == 0:
                continue
            if visited[i][j] == True:
                continue
            
            visited[i][j] = True
            que = deque([])
            que.append([i, j])
            while len(que) != 0:
                cur_pos = que.popleft()
                for k in range(4):
                    temp_y = cur_pos[0] + dx[k]
                    temp_x = cur_pos[1] + dy[k]
                    if temp_x < 0 or temp_y < 0 or temp_x >= x_length or temp_y >= y_length:
                        continue
                    if visited[temp_y][temp_x] == True:
                        continue
                    if ground_map[temp_y][temp_x] == 0:
                        continue
                    visited[temp_y][temp_x] = True
                    que.append([temp_y, temp_x])
            worm_count += 1
    
    
    res_list.append(worm_count)
    
for i in range(test_count):
    find_worm()
for res in res_list:
    print(res)
