import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 91 
dp[1] = 1
dp[2] = 1
if n < 3:
    print(dp[n])
else:
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp[n])

# D[i] = i자리수가 가지는 이친수의 개수
# D[3] = D[2] + D[1]

# D[1] = 1
# D[2] = 1
# D[3] = 2
# D[4] = 3
# D[5] = 5
# 10000
# 10001
# 10010
# 10100
# 10101
