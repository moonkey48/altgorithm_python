
import sys
input = sys.stdin.readline

dp = [
    [[0 for _ in range(-50,51) ] for _ in range(-50,51)] for _ in range(-50,51)
    ]
dp[70][70][70] = 1048576

for i in range(0,101):
    for j in range(0, 101):
        for k in range(0, 101):
            if i <= 50 or j <= 50 or k <= 50:
                dp[i][j][k] = 1
                continue
            if i > 70 or j > 70 or k > 70:
                dp[i][j][k] = dp[70][70][70]
                continue
            if i < j and j < k:
                dp[i][j][k] = dp[i][j][k - 1] + dp[i][j - 1][k - 1] - dp[i][j - 1][j]
                continue
            
            dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][j - 1][k] + dp[i - 1][j][k - 1] - dp[i - 1][j - 1][k - 1]

res = []
while True:
    nums = list(map(int, input().rstrip().split(" ")))    
    if nums[0] == -1 and nums[1] == -1 and nums[2] == -1:
        break
    res.append("w("+str(nums[0])+", "+str(nums[1])+", "+str(nums[2])+") = "+str(dp[nums[0] + 50][nums[1] + 50][nums[2] + 50]))

for r in res:
    print(r)

