import sys
from itertools import combinations
input = sys.stdin.readline
n, m = list(map(int, input().rstrip().split(" ")))
cards = list(map(int, input().rstrip().split(" ")))

combis = list(combinations(cards,3))

max_num = 0
for combi in combis:
    if sum(combi) > max_num and sum(combi) <= m:
        max_num = sum(combi)
print(max_num)
            