import sys

n = int(sys.stdin.readline())

a = 0 
b = 0

dp = [[0,0] for _ in range(46)]
dp[1] = [0, 1]
for i in range(2, n + 1):
    dp[i][0] += dp[i - 1][1]
    dp[i][1] += dp[i - 1][1] + dp[i - 1][0]
print(" ".join(str(e) for e in dp[n]))