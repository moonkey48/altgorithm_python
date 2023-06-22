import sys
input = sys.stdin.readline

n, l = list(map(int, input().rstrip().split(" ")))
nums = list(map(int, input().rstrip().split(" ")))

taped = [False for _ in range(2002)]
nums.sort()
count = 0
for num in nums:
    if taped[num] == False:
        count += 1
        
        for i in range(num, num + l):
            taped[i] = True
print(count)
