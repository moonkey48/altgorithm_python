import sys
n = int(sys.stdin.readline())

dp = [[0 for _ in range(10)] for _ in range(n + 1)]


for i in range(1, n + 1):
    if i == 1:
        for j in range(1,10):
            dp[i][j] = 1
    else:
        for j in range(10):
            if j == 0:
                dp[i][1] += dp[i - 1][0]
            elif j == 9:
                dp[i][8] += dp[i - 1][9]
            else:
                dp[i][j + 1] += dp[i - 1][j]
                dp[i][j - 1] += dp[i - 1][j]

print(sum(dp[n]) % 1_000_000_000)

