import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

dp = [0] * n
pos = n - 1
dp[pos] = arr[n - 1]

while pos >= 0:
    if pos == 1:
        dp[0] += dp[pos]
        pos -= 1
        break
    if arr[pos - 1] < arr[pos - 2]:
        dp[pos - 2] = arr[pos - 2] + dp[pos]
        pos -= 2
    else:
        dp[pos - 1] = arr[pos - 1] + dp[pos]
        pos -= 1
        
print(dp)
    
    
