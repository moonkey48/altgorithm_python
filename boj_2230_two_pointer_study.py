import sys
input = sys.stdin.readline
n, m = list(map(int, input().rstrip().split(" ")))

nums = []

for _ in range(n):
    num = int(input())
    nums.append(num)
nums.sort()

left = 0
right = 0
max_gap = max(nums) - min(nums)

while left <= right:
    gap = nums[right] - nums[left]
    
    if gap >= m:
        max_gap = min(max_gap, gap)
        left += 1
    else:
        if right < n - 1:
            right += 1
        else:
            left += 1

print(max_gap)