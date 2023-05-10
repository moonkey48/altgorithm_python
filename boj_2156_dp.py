import sys
input = sys.stdin.readline

n = int(input())
wine_list = []
dp = [0] * n

for i in range(n):
    wine_list.append(int(input()))

dp[0] = wine_list[0]
dp[1] = wine_list[0] + wine_list[1]
dp[2] = max(wine_list[0] + wine_list[1], wine_list[0] + wine_list[2], wine_list[1] + wine_list[2])
dp[3] = max(
    wine_list[0] + wine_list[1] + wine_list[3],
    wine_list[0] + wine_list[2] + wine_list[3],
    wine_list[1] + wine_list[2]
    )
for i in range(3, n):
    dp[i] = max(
        dp[i - 3] + wine_list[i - 1] + wine_list[i],
        dp[i - 2] + wine_list[i]
    )
# print(wine_list)
# print(dp)
print(max(dp))

# D[i]는 i개의 포도주가 있을때 마실 수 있는 포도주의 최대 양
# D[0] = wine_list[0]
# D[1] = wine_list[0] + wine_list[1]
# D[2] = max(wine_list[0] + wine_list[1], wine_list[1] + wine_list[2], wine_list[0] + wine_list[2])
# D[3] = 
#
# 6
# 6 + 10
# 6 + 13 / 6 + 10 / 10 + 13 
# 6 + 10 + 9 / 6 + 13 + 9
# 6 + 10 + 9 + 8 / 6 + 10 + 9 + 8 / 6 + 13 + 8 / 10 + 13 + 8 /
dp[i - 3] + wine_list[i - 1] + wine_list[i]
dp[i - 2] + wine_list[i]





# D[i] = max(D[i - 3] + wine_list[i - 1] + wine_list[i],)