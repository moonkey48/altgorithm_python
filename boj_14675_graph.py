import sys
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    f,t = list(map(int, input().rstrip().split(" ")))
    tree[f].append(t)

print(tree)