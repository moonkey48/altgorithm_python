import sys
input = sys.stdin.readline

n = int(input())

members = list(list(input().rstrip().split(" ")) for _ in range(n))
members_sorted = sorted(members, key=lambda x: int(x[0]))
for member in members_sorted:
    print(member[0] + " " + member[1])
