import sys
input = sys.stdin.readline

count = int(input())

freq = [-1] * 2_000_001


for i in range(count):
    input_value = int(input())
    freq[input_value + 1_000_000] += 1


for i in range(len(freq)):
    if freq[i] != -1:
        for j in range(freq[i] + 1):
            print(i - 1_000_000)    
