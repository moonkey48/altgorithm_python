# import sys
# from collections import deque
# input = sys.stdin.readline

# n = int(input())

# res_list = []

# for i in range(n):
#     case_length = int(input())
#     sum = 0
#     que = deque(list(map(int, input().rstrip().split(" "))))
    
#     while len(que) != 0:
#         temp_list = []
#         max_num = max(que)
#         while len(que) != 0:
#             num = que.popleft()
#             if num == max_num:
#                 for k in temp_list:
#                     sum += max_num - k
#                 break
#             else:
#                 temp_list.append(num)
        
#     res_list.append(sum)
    

# for res in res_list:
#     print(res)


import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

res_list = []

case_length_list = []
stock_total = []
for i in range(n):
    case_length = int(input())
    case_length_list.append(case_length)
    stock_list = list(map(int, input().rstrip().split(" ")))
    stock_total.append(stock_list)

for i in range(n):
    c_length = case_length_list[i]
    stocks = stock_total[i]
    sum = 0
    cur_pos = 0
    
    while cur_pos < c_length:
        max_num = max(stocks[cur_pos:])
        
        while cur_pos < c_length:
            num = stocks[cur_pos]
            if num == max_num:
                break
            else:
                sum += max_num - num
                cur_pos += 1
        cur_pos += 1
    
    res_list.append(sum)
    
for res in res_list:
    print(res)

