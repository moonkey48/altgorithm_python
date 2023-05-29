import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    left, right = list(map(int, input().rstrip().split(" ")))
    dp = [0 for _ in range(left)] 
    for j in range(left):
        if j == 0:
            dp[j] += right
        else:
            dp[j] += dp[j - 1]
    total = 1
    
    print(dp)
    
        
