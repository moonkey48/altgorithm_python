import sys
n = int(sys.stdin.readlines())

dp[1] = 1 => CY
dp[2] = 2 => SK
dp[3] = 3 => CY
dp[4] = 3 + 1 => CY
dp[5] = 3 + 1 + 1, 1 + 3 + 1, 1 + 1 + 1 + 1 + 1 => SK
1 2 3 

rest = n % 4
if rest == 0:
    print("CY")
elif rest == 1:
    print("CY")
elif rest == 2:
    print("SK")
elif rest == 3:
    print("CY")

