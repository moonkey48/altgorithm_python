import sys

input = sys.stdin.readline
n = int(input())
num_list = list(list(map(int, input().rstrip().split(" "))) for _ in range(n))

num_list.sort(key= lambda x: (x[0], x[1]))
for num in num_list: print(str(num[0]) + " " + str(num[1]))