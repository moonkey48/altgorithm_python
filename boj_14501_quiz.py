import sys
input = sys.stdin.readline

n = int(input())
time_table = []
for i in range(n):
    item = list(map(int, input().rstrip().split(" ")))
    time_table.append(item)

# D[i] = i일까지 최대 
