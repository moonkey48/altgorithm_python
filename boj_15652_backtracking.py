import sys
n, m = list(map(int, input().rstrip().split(" ")))

num_list = []

def next_num(num, count):
    if count == m:
        print(' '.join(str(e) for e in num_list))
        return
    for i in range(num, n + 1):
        num_list.append(i)
        next_num(i, count + 1)
        num_list.pop()
        
    
for i in range(1,n + 1):
    num_list.append(i)
    next_num(i, 1)
    num_list.pop()