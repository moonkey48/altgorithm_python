import sys
from collections import deque
input = sys.stdin.readline

case_count = int(input())
res = []

for _ in range(case_count):
    n, index = list(map(int, input().split(" ")))
    files = list(map(int, input().split(" ")))
    deq = deque(files)
    
    cur_index = 0
    count = 0
    while cur_index != index:
        cur_priority = deq[cur_index]
        higher_priority_index = -1
        for i in range(len(deq)):
            if deq[i] > cur_priority:
                higher_priority_index = i
                break
        if higher_priority_index != -1:
            for j in range(higher_priority_index):
                if j == index:
                    index += len(deq) - 1
                else:
                    index -= 1
                p = deq.popleft()
                deq.append(p)
        else:
            deq.popleft()
            index -= 1
            cur_index -= 1
            count += 1
    res.append(count)
    # print(count)
    
    # print([n, index])
    # print(files)
print(res)