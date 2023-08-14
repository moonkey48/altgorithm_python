import sys
input = sys.stdin.readline
k = 80
dungeons = [[80,20],[50,40],[30,10]]

visited = [False for _ in range(len(dungeons))]
max_dungeons = 0

def goDungeon(life,currentDungeon, count):
    global max_dungeons
    for j in range(len(dungeons)):
        if visited[j] == True:
            continue
        if life < dungeons[j][0]:
            max_dungeons = max(max_dungeons, count)
            continue
        visited[j] = True
        goDungeon(life - dungeons[j][1],dungeons[j], count + 1)
        visited[j] = False
    

for i in range(len(dungeons)):
    if k >= dungeons[i][0]:
        visited[i] = True
        goDungeon(k - dungeons[i][1],dungeons[i], 1)
        visited[i] = False
    
print(max_dungeons)