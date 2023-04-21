import sys

n = int(sys.stdin.readline())

divider = 2

while n >= divider:
    if n % divider == 0:
        n = n / divider
        print(divider)
        continue
    divider += 1
    