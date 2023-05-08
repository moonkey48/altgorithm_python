import sys
input = sys.stdin.readline

n, m = list(map(int, input().rstrip().split(" ")))

cur_arr = []

def next_num(count):
    if count == 0:
        print(' '.join(str(e) for e in cur_arr))
        return
    for i in range(1,n+1):
        cur_arr.append(i)
        next_num(count - 1)
        cur_arr.pop()
        
next_num(m)