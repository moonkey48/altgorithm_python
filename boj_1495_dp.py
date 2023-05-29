import sys
from collections import deque
input = sys.stdin.readline

n, start_volume, max_volume = list(map(int, input().rstrip().split(" ")))
volume_list = list(map(int, input().rstrip().split(" ")))


before = deque([start_volume])

for i in range(len(volume_list)):
    now = deque([])
    for j in range(len(before)):
        before_value = before.popleft()
        if before_value + volume_list[i] <= max_volume:
            if before_value + volume_list[i] not in now:
                now.append(before_value + volume_list[i]) 
        if before_value - volume_list[i] >= 0:
            if before_value - volume_list[i] not in now:
                now.append(before_value - volume_list[i])
    before = now
    if len(before) == 0:
        break 
    #  3 1 // 

if len(before) == 0:
    print(-1)
else:
    print(max(before))




