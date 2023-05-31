import sys

n  = int(sys.stdin.readline())
dp = [0] * 1000_001

used = [1]

dp[1] = 1
cur_num = 1
for i in range(2,n + 1):
    if i < (cur_num + 1) ** 2:
        dp[i] = dp[cur_num ** 2] + dp[i - cur_num ** 2]
        for j in used:
            dp[i] = min(
                dp[j ** 2] + dp[i - j ** 2],
                dp[i]
                )
    else:
        used.append(cur_num + 1)
        cur_num += 1
        dp[i] = 1

print(dp[n])
        

