import sys

n, k = list(map(int, input().rstrip().split(" ")))

dp = [[0 for _ in range(k + 1)] for _ in range(n)]

for i in range(n):
    weight, value = list(map(int, input().rstrip().split(" ")))
    if i == 0:
        for j in range(1, k + 1):
            if j >= weight:
                dp[i][j] = value
    else:
        for j in range(1, k + 1):
            if j >= weight:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
            else:
                dp[i][j] = dp[i - 1][j]
print(max(dp[n - 1]))


