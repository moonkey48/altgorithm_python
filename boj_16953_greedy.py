import sys
from collections import deque
input = sys.stdin.readline

num_list = []
cur_num, max_num = list(map(int, input().rstrip().split(" ")))
max_count = 0

def find_num(num, count):
    global max_count
    if max_num == num:
        max_count = count
        return
    if max_num < num * 2:
        if max_num >= int(str(num) + str(1)):
            find_num(int(str(num) + str(1)), count + 1)
        else:
            return
    elif max_num < int(str(num) + str(1)):
        if max_num >= num * 2:
            find_num(num * 2, count + 1)
        else:
            return
    find_num(num * 2, count + 1)
    find_num(int(str(num) + str(1)), count + 1)
    
find_num(cur_num, 1)
if max_count == 0:
    print(-1)
else:
    print(max_count)