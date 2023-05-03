import sys
import math
input = sys.stdin.readline
n = int(input())

cur_str = ""
res_list = []

def is_prime(num):
    if num == 1:
        return False
    for i in range(2,int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def next_num(count):
    global cur_str
    if count == n:
        res = int(cur_str)
        res_list.append(res)
        return
    for i in range(1,10):
        temp_num = int(cur_str + str(i))
        if is_prime(temp_num):
            cur_str += str(i)
            next_num(count + 1)
            cur_str  = cur_str[:count]
    
next_num(0)
for i in res_list:
    print(i)