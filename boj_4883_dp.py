import sys
input = sys.stdin.readline

k = 0

while True:
    k += 1
    n = int(input())
    if n == 0:
        break
    
    graph = [[0,0,0]]
    sum_list = [[0 for i in range(3)] for j in range(n + 1)]
    for i in range(n):
        input_line = list(map(int, input().rstrip().split(" ")))
        graph.append(input_line)

    sum_list[2][0] = graph[2][0] + graph[1][1]
    sum_list[2][1] = graph[2][1] + min(sum_list[2][0], graph[1][1], graph[1][1] + graph[1][2])
    sum_list[2][2] = graph[2][2] + min(sum_list[2][1], graph[1][1], graph[1][1] + graph[1][2])
   
    for i in range(3, n + 1):
        for j in range(3):
            if j == 0:
                min_value = min(sum_list[i - 1][j], sum_list[i - 1][j + 1]) 
            elif j == 1:
                min_value = min(sum_list[i][j - 1], sum_list[i - 1][j - 1], sum_list[i - 1][j], sum_list[i - 1][j + 1])                
            else:
                min_value = min(sum_list[i][j - 1], sum_list[i - 1][j - 1], sum_list[i - 1][j])
            
            sum_list[i][j] = graph[i][j] + min_value
    print(str(k) + '. ' + str(sum_list[-1][1]))



