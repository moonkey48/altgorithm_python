import sys
input = sys.stdin.readline

n = int(input())

size_list = []
for _ in range(n):
    size_list.append(list(map(int, input().rstrip().split(" "))))
    
scores = []
for i in range(len(size_list)):
    score = 1
    for j in range(len(size_list)):
        if i == j:
            continue
        else:
            if size_list[j][0] > size_list[i][0] and size_list[j][1] > size_list[i][1]:
                score  += 1
    scores.append(score)
print(" ".join(str(e) for e in scores))
