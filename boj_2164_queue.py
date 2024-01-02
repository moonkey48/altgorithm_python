import sys
from collections import deque

n = int(sys.stdin.readline())

deq = deque([])
for i in range(1,n + 1):
    deq.append(i)

while len(deq) > 1:
    deq.popleft()
    top = deq.popleft()
    deq.append(top)
print(deq[0])