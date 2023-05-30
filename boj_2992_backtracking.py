import sys

input_str = sys.stdin.readline().rstrip()
input_list = list(input_str)
input_num = int(input_str)

cur = []
cur_list = []
max_nums = []


def find_num(count):
    if count == len(input_list):
        joined = int(''.join(str(e) for e in cur))
        if joined > input_num:
            max_nums.append(joined)
        return
    for i in range(len(input_list)):
        if i in cur_list:
            continue
        cur.append(input_list[i])
        cur_list.append(i)
        find_num(count + 1)
        cur.pop()
        cur_list.pop()

for i in range(len(input_list)):
    cur.append(input_list[i])
    cur_list.append(i)
    find_num(1)
    cur_list.pop()
    cur.pop()
if len(max_nums) == 0:
    print(0)
else:
    print(min(max_nums))