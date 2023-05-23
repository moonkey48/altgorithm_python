import sys
input = sys.stdin.readline

a_str = list(map(str, input().rstrip()))
b_str = list(map(str, input().rstrip()))
dp = [0] * len(a_str)

print(a_str)
print(b_str)
for i in range(len(a_str)):
    for j in range(len(b_str)):
        if b_str[j] == a_str[i] and dp[j] == 0:
            dp[j] = 1
            pos_a = i
            pos_b = j
            while a_str[pos_a] == b_str[pos_b] and pos_a < (len(a_str) - 1) and pos_b < (len(b_str) - 1):
                if a_str[pos_a] == b_str[pos_b]:
                    dp[pos_b] = dp[pos_b - 1] + 1
                    pos_b += 1
                    pos_a += 1
print(dp)