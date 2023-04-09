# N과 M

import sys
input = sys.stdin.readline

m, n = list(map(int, input().rstrip().split(" ")))

arr = [0] * n
isused = [False] * m

def next_num(count):
    if count == n:
        print(' '.join(str(e) for e in arr))
        return
    for i in range(m):
        if isused[i] == False:    
            arr[count] = i + 1
            isused[i] = True
            next_num(count + 1)
            isused[i] = False
    
next_num(0)