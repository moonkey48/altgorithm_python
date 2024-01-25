import sys
input = sys.stdin.readline

n, k = list(map(int, input().rstrip().split(" ")))
num_list = list(i for i in range(1,n + 1))
is_used = [False for _ in range(n)]

used_num_list = []
cur_index = 0

while len(used_num_list) < n:
    count = 0
    while count < k:
        if is_used[cur_index] == False:
            count += 1
        if count >= k:
            break
        cur_index += 1
        cur_index = cur_index % n
    used_num_list.append(num_list[cur_index])
    is_used[cur_index] = True
    
print('<' + ', '.join(str(e) for e in used_num_list) + '>')