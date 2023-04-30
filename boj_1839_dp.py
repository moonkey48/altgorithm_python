import sys
input = sys.stdin.readline

n = int(input())

start_len = int(n / 5)

while start_len >= 0:
    remain = n - ( 5 * start_len)
    if remain % 3 == 0:
        break
    start_len -= 1

if start_len < 0:
    print(-1)
else:
    count = 0
    while remain > 0:
        count += 1
        remain -= 3
    print(start_len + count)
    
