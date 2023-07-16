import sys
n = str(sys.stdin.readline().rstrip())

dp = [0 for _ in range(int(n))]

# dp[n] = dp[n - 2] + case(str- (n -2)) + dp[n - 1] + case(str - (n - 1))

dp[0] = 1
if int(n[0:2]) < 27:
    dp[1] = dp[0] + 1
else:
    dp[1] = dp[0]
for i in range(int(n)):
    dp[i] += dp[i - 1]
    if int(n[i - 1 : i + 1]) < 27:
        dp[i] += 1
print(dp)
