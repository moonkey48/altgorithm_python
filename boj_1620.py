import sys
input = sys.stdin.readline

n, m = list(map(int, input().split(" ")))
pocketmonIdToName = {}
pocketmonNameToId = {}
for i in range(1,n + 1):
    pocketMon = input().rstrip()
    pocketmonIdToName[i] = pocketMon
    pocketmonNameToId[pocketMon] = i
res = []
for _ in range(m):
    question = input().rstrip()
    if question.isnumeric():
        res.append(pocketmonIdToName[int(question)])
    else:
        res.append(pocketmonNameToId[question])
        

for r in res:
    print(r)
