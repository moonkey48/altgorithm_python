import sys
input = sys.stdin.readline

n, sum = list(map(int, input().rstrip().split(" ")))
num_list = list(map(int, input().rstrip().split(" ")))

count = 0    

def check(cur, total):
    global count
    if cur == n:
        if total == sum:
            count += 1
        return
    check(cur + 1, total)
    check(cur + 1, total + num_list[cur])


check(0, 0)

if sum == 0:
    count -= 1
print(count)
