import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4


for i in range(n):
    step = 4
    while step != 12:
        dp[step] = dp[step -3] + dp[step -2] + dp[step -1]
        step += 1

num_list =[]
for i in range(n):
    num = int(input())
    num_list.append(num)

for num in num_list:
    print(dp[num])
    
