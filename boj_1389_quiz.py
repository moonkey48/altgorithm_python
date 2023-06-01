import sys
from collections import deque
input = sys.stdin.readline

n, m = list(map(int, input().rstrip().split(" ")))

r = {}
for i in range(1, n + 1):
    r[i] = []

for i in range(m):
    f, t = list(map(int, input().rstrip().split(" ")))
    r[f].append(t)
    r[t].append(f)

print(r)
cur_visited = []
sum_list = [0] * (n + 1)
def find_num(count, start, init_num, to_find):
    global sum_list
    # print(count,start, to_find)
    arr = r[start]
    for num_to in arr:
        if num_to == to_find:
            sum_list[init_num] += count
            print([count, start,init_num, to_find])
            return
        if num_to in cur_visited:
            continue
        
        cur_visited.append(num_to)
        find_num(count + 1, num_to, init_num,to_find)
        cur_visited.pop()
    
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i != j:
            cur_visited.append(i)
            print([i,j])
            find_num(1, i, i, j)
            cur_visited.pop()
print(sum_list)