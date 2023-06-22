import sys
input = sys.stdin.readline

n, s = list(map(int, input().rstrip().split(" ")))
nums = list(map(int, input().rstrip().split(" ")))

nums.sort()


cur = []
p_count = 0

def find_num(index, sum):
    global p_count
    if sum == s:
        p_count += 1
        
    for j in range(index + 1, len(nums)):
        cur.append(nums[j])
        find_num(j, sum + nums[j])
        cur.pop()
    
for i in range(len(nums)):
    cur.append(nums[i])
    find_num(i, nums[i])
    cur.pop()
    
print(p_count)