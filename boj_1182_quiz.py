import sys
input = sys.stdin.readline

n, sum = list(map(int, input().rstrip().split(" ")))

checked_list = [False] * n
num_list = list(map(int, input().rstrip().split(" ")))

count = 0

