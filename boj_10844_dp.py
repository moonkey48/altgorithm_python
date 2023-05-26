import sys

n = int(sys.stdin.readline())

dp = [0] * (n + 1)

# 1   2   3   4   5   6   7   8   9 
# 02   13  24  35  46  57  68  79  8 17
# 1  1
# 15 * 2 + 2

# 0 9 9
# 29 * 2 + 3

# 3 + 3
# (dp[i - 1] - 6) * 2 + 6
# 55 * 2 + 6
# 116


# 116

# # 32 21
# # 32

# 0 9


if n == 1:
    dp[1] = 9
    print(dp[1])
elif n == 2:
    dp[1] = 9
    dp[2] = 17 
    print(dp[2])
else:
    dp[1] = 9
    dp[2] = 17 
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] - k) * 2 + k
    print(dp[n] % 1_000_000_000)


#  * 2 - 1

# 17
# 32
# 61
# 116
# 1 i == 2  i * 2 - 3
# 2 i == 3
# 3 i == 4
# 6 i == 5
