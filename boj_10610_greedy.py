import sys

n = str(sys.stdin.readline().rstrip())

if '0' not in n:
    print(-1)
else:
    sum = 0
    for num in n:
        sum += int(num)
    if (sum % 3) == 0:
        seperated = []
        for i in n:
            seperated.append(int(i))
        seperated.sort(reverse=True)
        print(int(''.join(str(e) for e in seperated)))
    else:
        print(-1)
        
        