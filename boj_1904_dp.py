import sys
n = int(sys.stdin.readline())

dp = [0] * 1_000_001
dp[1] = 1
dp[2] = 2

for i in range(3,n + 1):
    if (dp[i - 2] + dp[i - 1]) > 15746:
        dp[i] = (dp[i - 2] + dp[i - 1]) % 15746
    else:
        dp[i] = dp[i - 2] + dp[i - 1]        
    
print(dp[n] % 15746)
    

# # 최소: n / 2 + n % 0
# # 최대: n
# dp[1] = 1
# dp[2] = 11, 00
# dp[3] = 111, 100, 001
# dp[4] = 1111, 1100, 0011, 1001, 0000