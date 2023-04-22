import sys
input = sys.stdin.readline

n = int(input())
input_list = list(map(int, input().rstrip().split(" ")))
list = input_list[:]
list.sort()

removed_list = []
removed_list.append(list[0])
cur_index = 0

for i in range(1,len(list)):
    if list[i] == removed_list[cur_index]:
        continue
    else:
        removed_list.append(list[i])
        cur_index += 1

def upper_index(target):
    st = 0
    en = len(removed_list)
    while st < en:
        mid = int((st + en) / 2)
        if removed_list[mid] >= target:
            en = mid
        else:
            st = mid + 1
    return st


res = []
for item in input_list:
    res.append(upper_index(item))

print(' '.join(str(e) for e in res))