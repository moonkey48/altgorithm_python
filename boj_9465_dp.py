import sys
input = sys.stdin.readline

n = int(input().rstrip())
results =[]

for _ in range(n):
    cases = int(input().rstrip())
    stickers = []
    dp = [[0 for _ in range(2)] for _ in range(cases)]
    
    
    for _ in range(2):
        stickers.append(list(map(int, input().rstrip().split(" "))))
        
    if cases == 1:
        results.append(max(stickers[0][0], stickers[1][0]))
        continue
    
    dp[0][0] = stickers[0][0]
    dp[0][1] = stickers[1][0]
    dp[1][0] = dp[0][1] + stickers[0][1]
    dp[1][1] = dp[0][0] + stickers[1][1]
    
    for i in range(2, cases):
        # print(i)
    
        dp[i][0] = max(dp[i - 1][1], dp[i - 2][0], dp[i - 2][1]) + stickers[0][i]
        dp[i][1] = max(dp[i - 1][0], dp[i - 2][1], dp[i - 2][0]) + stickers[1][i]
        # print(dp)
    
    results.append(max(dp[-1][0], dp[-1][1]))

for i in results:
    print(i)


    
## dp[i][0] = dp[i - 1][1] + stickers[i][0]


# 1
# 10
# 0 1 1 3 3 5 4 6 6 0
# 1 0 0 0 0 0 0 0 0 10


