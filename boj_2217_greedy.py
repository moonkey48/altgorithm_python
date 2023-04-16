import sys
input = sys.stdin.readline

k = int(input())

ropes = []
for i in range(k):
    ropes.append(int(input()))

ropes.sort()

ans = 0
for i in range(1, k + 1):
    ans = max(ans, ropes[k-i]*i)
print(ans)