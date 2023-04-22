import sys
input = sys.stdin.readline

n, m = list(map(int, input().strip().split(" ")))

numA = 1
for i in range(1,n+1):
    
    numA *= i
dividerA = 1
for i in range(1,n - m + 1):
    print(i)
    dividerA *= i
dividerB = 1
for i in range(1,m + 1):
    dividerB *= i
    
print(int(numA / dividerA / dividerB))