import sys
input = sys.stdin.readline

n = int(input())
u = []
for i in range(n):
    u.append(int(input()))

sum = []
for i in range(len(u)):
    for j in range(len(u)):
        sum.append(u[i] + u[j])

# print(sum)
# print(u)
sum.sort()

def find_sum(target):
    res = -1
    st = 0
    en = len(sum) - 1
    while st < en:
        mid = int((st + en) / 2)
        if sum[mid] == target:
            res = mid
            break
        elif sum[mid] < target:
            st = mid + 1
        elif sum[mid] > target:
            en = mid - 1
    return res

output = []
for i in range(len(u)):
    for j in range(len(u)):
        res = find_sum(u[i] - u[j])
        if res != -1:
            output.append(u[i])
            

print(max(output))