S = input()


arr = []

for i in range(ord('a'), ord('z') + 1):
    num = 0
    for s in S:
        if ord(s) == i:
            num += 1
    arr.append(num)

print(' '.join(map(str, arr)))
