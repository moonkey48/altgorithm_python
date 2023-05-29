import sys
input = sys.stdin.readline

n = int(input().rstrip())

str_list = []

for _ in range(n):
    i = input().rstrip()
    if i in str_list:
        continue
    else: 
        str_list.append(i)

str_list.sort(key=lambda x : (len(x), x))

for i in str_list:
    print(i)