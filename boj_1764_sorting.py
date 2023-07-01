import sys
from collections import Counter
input = sys.stdin.readline

n, m = list(map(int, input().rstrip().split(" ")))

not_seen = []
not_listen = []
for _ in range(n):
    not_seen.append(input().rstrip())
for _ in range(m):
    not_listen.append(input().rstrip())
    
res = Counter(not_seen) & Counter(not_listen)
intersection = list(res.elements())
intersection.sort()
print(len(intersection))
for i in intersection:
    print(i)