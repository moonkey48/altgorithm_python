import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().rstrip().split(" ")))
operator_list = list(map(int, input().rstrip().split(" ")))

cur_ops = []
sum_list = []

def calculate():
    sum = num_list[0]
    for i in range(n - 1):
        if cur_ops[i] == 0:
            sum += num_list[i + 1]
        elif cur_ops[i] == 1:
            sum -= num_list[i + 1]
        elif cur_ops[i] == 2:
            sum *= num_list[i + 1]
        elif cur_ops[i] == 3:
            sum = int(sum / num_list[i + 1])
    sum_list.append(sum)

def next_num(count):
    if count == n - 1: 
        calculate()
        return
    for i in range(4):
        if operator_list[i] != 0:
            operator_list[i] -= 1
            cur_ops.append(i)
            next_num(count + 1)
            operator_list[i] += 1
            cur_ops.pop()

next_num(0)
print(max(sum_list))
print(min(sum_list))
