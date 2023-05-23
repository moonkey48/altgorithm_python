import sys
input = sys.stdin.readline

n, k = list(map(int, input().rstrip().split(" ")))
arr = list(map(int, input().rstrip().split(" ")))
used = [False] * n

cur_arr = []
res_count = 0

def next_num(count, cur_w):
    global res_arr
    global res_count
    if count == n:
        res_count += 1
        return
    
    for i in range(len(arr)):
        if used[i] == True:
            continue
        if cur_w + arr[i] - k >= 500:
            used[i] = True
            cur_arr.append(arr[i])
            next_num(count + 1, cur_w + arr[i] - k)
            used[i] = False
            cur_arr.pop()
        

for i in range(len(arr)):
    if arr[i] >= k:
        cur_arr.append(arr[i])
        used[i] = True
        next_num(1, 500 - k + arr[i])
        cur_arr.pop()
        used[i] = False


print(res_count)