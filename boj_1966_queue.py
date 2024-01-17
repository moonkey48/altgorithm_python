import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

answer = []
for _ in range(n):
    print_total_count, print_pos = list(map(int, input().rstrip().split(" ")))
    queue = deque(map(int, input().rstrip().split(" ")))
    print_num = queue[print_pos] 
    printed_count = 0
    
    while True:
        current_num = queue.popleft()
        if len(queue) > 0:
            if current_num < max(queue):
                queue.append(current_num)
            else:
                printed_count += 1
            if current_num == print_num:
                break
        else:
            printed_count += 1
            break
    answer.append(printed_count)
print(answer)