import sys
from collections import deque
input = sys.stdin.readline

n, m = list(map(int, input().rstrip().split(" ")))
graph = [[] for i in range(int(n + 1))]
for i in range(m):
    from_person, to_person = list(map(int, input().rstrip().split(" ")))
    graph[from_person].append(to_person)
    graph[to_person].append(from_person)

print(graph)
# 1부터 n까지 돌면서 자신을 뺀 수만큼 돌려서 이동 가능 횛수 더해서 출력
def bfs(st):
    que = deque()
    total_count = 0
    
    for i in range(1, n + 1):  
        if i == st:
            continue
        visited = [False] * (n + 1)    
        distance = [0] * ( n + 1)
        distance[st] = 0
        visited[st] = True
        
        for k in graph[st]:
            distance[k] = distance[st] + 1
            que.append(k)
        
        while len(que) != 0:
            node = que.popleft()
            
            if visited[node] == True:
                continue
            
            visited[node] = True
            
            if node == i:
                total_count += distance[node]
                break
            for j in graph[node]:
                distance[j] = distance[node] + 1
                que.append(j)
                
        print([st, i, total_count])
    return total_count

sum_list = []
for i in range(1,n + 1):
    # 한사람씩
    sum = bfs(i)
    sum_list.append(sum)

    
print(min(sum_list))

