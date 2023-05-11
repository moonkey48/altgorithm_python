import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().rstrip().split(" ")))

# max_list = [max_num, count]
max_list = []
max_list.append([num_list[0], 1])

for i in range(1, n):
    for j in range(len(max_list)):
        if num_list[i] > max_list[j][0]:
            max_list[j][0] = num_list[i]
            max_list[j][1] += 1
        else:
            max_list.append([num_list[i], 1]) 
# max_list.sort(key = lambda x : x[1], reverse=True)
print(max_list)
print(max_list[0][1])
