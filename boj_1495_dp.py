import sys
input = sys.stdin.readline

n, cur, v_max = list(map(int, input().rstrip().split(" ")))
v_list = list(map(int, input().rstrip().split(" ")))

dp = [[0,0] for _ in range(n)]
 
for i in range(n):
    if dp[i][0] - v_list[i] >= 0:    
        dp[i][0] = dp[i][0] - v_list[i]
    elif dp[i]
