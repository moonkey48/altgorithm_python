import sys

num = int(sys.stdin.readline())
count  = 1
num -= 1

for i in range(1, 1_000_000_000):
    if num <= 0:
        break
    num -= 6 * i
    count += 1
        
print(count)
