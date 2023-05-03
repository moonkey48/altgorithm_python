import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().rstrip().split(" ")))

st = 0
en = n - 1
min = 2_000_000_000
res_list = []

while st < en:
    gap = abs(num_list[st] + num_list[en])
    if gap <= min:
        min = gap
        res_list = [st, en]
    
    gap = num_list[st] + num_list[en]
    if gap < 0:
        st += 1
    else:
        en -= 1

print(str(num_list[res_list[0]]) + " " + str(num_list[res_list[1]]))