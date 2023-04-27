import sys
input = sys.stdin.readline

n, m = list(map(int, input().rstrip().split(" ")))

arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()

max = max(arr) - min(arr)
st = 0
en = 0

while st < len(arr) - 1:
    gap = arr[en] - arr[st]
    # print([st, en, gap, max])
    if gap >= m:
        if max > gap:
            max = gap
        st += 1
    elif gap < m:
        if len(arr) - 1 > en:
            en += 1
        else:
            st += 1
        

print(max)