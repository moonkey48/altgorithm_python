import sys
input = sys.stdin.readline

n = int(input())
arr = []
life = list(map(int, input().rstrip().split()))
joy = list(map(int, input().rstrip().split()))
for i in range(n):
    arr.append([life[i], joy[i]])

arr.sort(key = lambda x : x[1], reverse= True)

dp = [0] * n

# dp[0] 