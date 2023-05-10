import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().rstrip().split(" ")))

person_list = []
for i in range(1,n + 1):
    person_list.append([i,num_list[i - 1]])

person_list.sort(key= lambda x: x[1])

total = 0
sum = 0
for person in person_list:
    sum = sum + person[1]
    total += sum
print(total)