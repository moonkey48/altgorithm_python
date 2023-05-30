import sys
import math
input = sys.stdin.readline

x1, y1 = list(map(int, input().rstrip().split(" ")))
x2, y2 = list(map(int, input().rstrip().split(" ")))

x1 = x1 * y2
x2 = x2 * y1
y1 = y1 * y2
y2 = y2 * y1

m = y1
n = x1 + x2


count = 2
max_num = int(math.sqrt(m)) + 1
while count <= max_num:
    if n % count == 0 and m % count == 0:
        n = int(n / count)
        m = int(m / count)
        count = 2
    else:
        count += 1

print(str(n) + ' ' + str(m))

