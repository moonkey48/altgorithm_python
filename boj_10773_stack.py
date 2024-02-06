import sys
input = sys.stdin.readline
n = int(input())
nums = [int(input().rstrip()) for _ in range(n)]

stack = []
for n in nums:
    if n == 0:
        if len(stack) > 0:
            stack.pop()
    else:
        stack.append(n)
print(sum(stack))
