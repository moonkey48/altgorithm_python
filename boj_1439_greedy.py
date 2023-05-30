import sys

n = list(map(int, input().rstrip()))

cur_num = n[0]
count_zero = 0
count_one = 0

if cur_num == 0:
    count_zero += 1
else:
    count_one += 1

for i in n:

    if cur_num != i:
        if cur_num == 0:
            count_one += 1
            cur_num = 1
        else:
            count_zero += 1
            cur_num = 0
print(min(count_one, count_zero))