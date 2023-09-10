import sys
input = sys.stdin.readline
commands = int(input())

nums = set()
results = []

for _ in range(commands):
    command = list(map(str, input().rstrip().split(" ")))
    if command[0] == 'add':
        if int(command[1]) not in nums:
            nums.add(int(command[1]))
    elif command[0] == 'check':
        print(1 if int(command[1]) in nums else 0)
    elif command[0] == 'remove':
        nums.discard(int(command[1]))
    elif command[0] == 'toggle':
        if int(command[1]) in nums:
            nums.discard(int(command[1]))
        else:
            nums.add(int(command[1]))
    elif command[0] == 'all':
        nums = set([i for i in range(1,21)])
    elif command[0] == 'empty':
        nums = set()