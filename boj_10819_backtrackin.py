import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().rstrip().split(" ")))

cur_num = [0] * n
visited = [False] * n
sum_list = []

def calculate_sum():
    sum = 0
    for i in range(1,n):
        sum += abs(cur_num[i - 1] - cur_num[i])
    sum_list.append(sum)

def next_num(count):
    if count == n:
        calculate_sum()    
        return
    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            cur_num[count] = num_list[i]
            next_num(count + 1)
            visited[i] = False
    

next_num(0)
# print(sum_list)
print(max(sum_list))