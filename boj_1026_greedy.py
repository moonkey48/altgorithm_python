import sys
input = sys.stdin.readline
n = int(input())

a_list = list(map(int, input().rstrip().split()))
b_list = list(map(int, input().rstrip().split()))
a_list.sort()
b_list.sort(reverse=True)

total = 0
for i in range(n):
    total += a_list[i] * b_list[i]

print(total)