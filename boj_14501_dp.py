import sys
input = sys.stdin.readline
n = int(input())

time_list = []
pay_list = []
max_list = [0] * (n + 1) 


for i in range(n):
    t, p = list(map(int, input().rstrip().split(" ")))
    time_list.append(t)
    pay_list.append(p)

for i in reversed(range(n)):
    if i + time_list[i] == n:
        max_list[i] = max(
            pay_list[i],
            max_list[i + 1]
        )
        continue
    elif i + time_list[i] > n:
        max_list[i] = max_list[i + 1] if i != n - 1 else 0
        continue
    
    max_list[i] = max(
        pay_list[i] + max_list[time_list[i] + i],
        max_list[i + 1]
    )

print(max_list[0])
