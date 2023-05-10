import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 1001
dp[1] = 1
dp[2] = 2
for i in range(3,1001):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[n] % 10007)

# D[i] = n개의 타일 길이에서 채우는 방법의 수

# D[1] = 1
# D[2] = D[1] + 1
# D[3] = D[2] + 1
# D[4] = D[3] + 2
# D[5] = D[4] + D[3]
