import sys
input = sys.stdin.readline

k, n = list(map(int, input().rstrip().split(" ")))

ran_lines = []
for i in range(k):
    ran_lines.append(int(input()))
    

def check_line(length):
    count = 0
    for i in range(k):
        line = ran_lines[i]
        while line >= 0:
            line -= length
            if line >= 0:
                count += 1
    return count


res = []
st = 1
en = max(ran_lines)

while st <= en:
    mid = int( (st + en) / 2)
    line_able = check_line(mid)
    if n == line_able:
        res.append(mid)
        st = mid + 1
    elif n > line_able:
        en = mid - 1
    else:
        res.append(mid)
        st = mid + 1

print(max(res))


