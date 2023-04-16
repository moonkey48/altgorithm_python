import sys

n = int(sys.stdin.readline())

dist = [0] * (n + 1)
dist[1] = 0
for i in range(2,n+1):
    dist[i] = dist[i-1] + 1
    if i % 2 == 0:
        dist[i] = min(dist[i], dist[i // 2] + 1)
    if i % 3 == 0:
        dist[i] = min(dist[i], dist[i // 3] + 1)

print(dist[n])