import sys
from collections import deque

input = sys.stdin.readline
deq = deque([])

input_length = input()
input_list = [input().rstrip() for _ in range(int(input_length))]

for i in input_list:
    com = i.split()
    
    if (com[0] == 'push_back'):
        deq.append(com[1])
    elif (com[0] == 'push_front'):
        deq.appendleft(com[1])
    elif (com[0] == 'pop_front'):
        if len(deq) != 0:
            print(deq.popleft())
        else:
            print(-1)
    elif (com[0] == 'pop_back'):
        if len(deq) != 0:
            print(deq.pop())       
        else:
            print(-1)
    elif (com[0] == 'front'):
        if len(deq) != 0:
            print(deq[0])
        else:
            print(-1)
    elif (com[0] == 'back'):
        if len(deq) != 0:
            print(deq[len(deq)-1])
        else:
            print(-1)
    elif (com[0] == 'size'):
        print(len(deq))
    elif (com[0] == 'empty'):
        if len(deq) != 0:
            print(0)
        else:
            print(1)
    
