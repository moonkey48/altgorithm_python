import sys

input = sys.stdin.readline

while True:
    nums = list(map(int, input().rstrip()))
    k = 0
    if nums[0] == 0:
        break
    while k <= int((len(nums) -1) / 2):
        if nums[k] != nums[len(nums) - 1 - k]:
            print("no")
            break
        k += 1
    if k > int((len(nums) -1) / 2):
        print("yes")
    
        
        