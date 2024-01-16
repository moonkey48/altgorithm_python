import sys

input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int, input().rstrip().split(" ")))
m = max(nums)

sum = 0
for num in nums:
    sum += (num / m) * 100
print(sum / n)

