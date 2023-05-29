import sys
input = sys.stdin.readline

n = int(input().rstrip())

weights = list(map(int, input().rstrip().split(" ")))
joys = list(map(int, input().rstrip().split(" ")))

dp = [[0 for _ in range(101)] for _ in range(n)]

for i in range(n):
    if i == 0:
        for j in range(1, 101):
            if j > weights[i]:
                dp[i][j] = joys[i]
    else:
        for j in range(1, 101):
            if j > weights[i]:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i]] + joys[i])
            else:
                dp[i][j] = dp[i - 1][j]
        
print(max(dp[n - 1]))