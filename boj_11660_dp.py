import sys
input = sys.stdin.readline

n, m = list(map(int, input().rstrip().split(" ")))
num_map = []
for i in range(n):
    num_map.append(list(map(int, input().rstrip().split(" "))))
q_list = []
for i in range(m):
    x1, y1, x2, y2 = list(map(int, input().rstrip().split(" ")))
    q_list.append([x1 - 1, y1 - 1, x2 - 1, y2 - 1])    

sum_list = []
for i in range(n):
    row_list = []
    for j in range(n):
        if j == 0:
            row_list.append(num_map[i][j])   
        else:
            row_list.append(row_list[j - 1] + num_map[i][j])
    sum_list.append(row_list)

for q in q_list:
    sum = 0
    for i in range(q[0],q[2] + 1):
        sum += sum_list[i][q[3]] - sum_list[i][q[1]] + num_map[i][q[1]]
    print(sum)