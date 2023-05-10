import sys
input = sys.stdin.readline

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().rstrip().split(" "))))

dp = [[0] * n for i in range(n)]
for i in range(n):
    dp[n - 1][i] = graph[n - 1][i]

for i in reversed(range(0, n - 1)):
    for j in range(i + 1):
        dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1]) + graph[i][j]

print(dp[0][0])
