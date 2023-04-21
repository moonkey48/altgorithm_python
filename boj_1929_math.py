import sys
input = sys.stdin.readline
min, max = list(map(int, input().rstrip().split(" ")))

state = [True] * 1_000_001
def sleve(n):
    state[1] = False
    for i in range(2,n + 1):
        if state[i] == False:
            continue
        count = i * i
        for _ in range(i*i, n+1):
            state[count] = False
            if count >= n:
                break
            count += i

sleve(max)
for i in range(min, max + 1):
    if state[i] == True:
        print(i)