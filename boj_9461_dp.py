import sys
input = sys.stdin.readline

n = int(input())

num_list = [0] * 101
num_list[1] = 1
num_list[2] = 1
num_list[3] = 1
num_list[4] = 2
num_list[5] = 2

for i in range(6,101):
    num_list[i] = num_list[i - 1] + num_list[i - 5]

res_list = []
for i in range(n):
    input_num = int(input())
    res = num_list[input_num]
    res_list.append(res)

for i in res_list:
    print(i)
    

