import sys
input = sys.stdin.readline

n, m = list(map(int, input().rstrip().split(" ")))

arr = [0] * m
visited = [False] * n

def next_num(count, prev_num):
    if count == m:
        print(' '.join(str(e) for e in arr))
        return
    for i in range(prev_num,n + 1):
        if visited[i - 1] == False:
            arr[count] = i
            visited[i - 1] = True
            next_num(count + 1, arr[count])        
            visited[i - 1] = False
    
next_num(0, 1)