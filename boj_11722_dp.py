import sys
input = sys.stdin.readline

num_of_sequence = int(input())

sequence_list = list(map(int, input().rstrip().split(" ")))
print(sequence_list)

long_sequence = [0] * 1001
max_num = 0
for i in reversed(sequence_list):
    print(i)

    if i > max_num:
        
        max