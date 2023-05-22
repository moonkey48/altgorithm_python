import sys
input = sys.stdin.readline

N = int(input())
num_list = [0]

dp = [0] * (N + 1)

num_list += list(map(int, input().rstrip().split(" ")))

for i in range(1, N + 1):
    for j in range(i):
        if num_list[i] > num_list[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))
result = []
order = max(dp)
for i in reversed(range(1, N + 1)):
    if dp[i] == order:
        result.append(num_list[i])
        order -= 1
result.reverse()
print(' '.join(str(e) for e in result))