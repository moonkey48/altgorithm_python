# 풀긴했지만 이해 못함 ;

import sys 
input = sys.stdin.readline

a,b,c = list(map(int, input().rstrip().split(" ")))

def recursion(num, repeat, divider):
    if repeat == 1:
        return num % divider
    val = recursion(num, int(repeat/2), divider)
    val = val * val % divider
    if repeat % 2 == 0:
        return val
    return val * num % divider

res = recursion(a,b,c)
print(res)
