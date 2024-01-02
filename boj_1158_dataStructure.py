import sys

n, k = list(map(int, sys.stdin.readline().split()))

arr = [False for _ in range(n)]

stack = []

pos = 0
while len(stack) < n - 1:
    count = 0
    while count < k:
        if arr[pos] == False:
            count += 1
            arr[pos] = True
        if count == k:
            break
        pos += 1
        pos = pos % n
    print(pos)
    stack.append(pos + 1)
    print(stack)
print(stack)