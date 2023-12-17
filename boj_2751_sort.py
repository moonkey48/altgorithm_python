import sys
n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

nums.sort()
for num in nums:
    print(num)