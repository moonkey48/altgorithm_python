import sys
input = sys.stdin.readline

n = int(input())
num_list = []

for i in range(n):
    num_list.append(int(input()))

fibo_arr = [[0,0]] * 41

count_zero = 0
count_one = 0

    
fibo_arr[0] = [1,0]
fibo_arr[1] = [0,1]

for number in range(2,41):
    count_one = 0
    count_zero = 0
    fibo_arr[number] = [
        fibo_arr[number - 1][0] + fibo_arr[number - 2][0], 
        fibo_arr[number - 1][1] + fibo_arr[number - 2][1], 
        ]

for num in num_list:
    print(str(fibo_arr[num][0]) + " " + str(fibo_arr[num][1]))   


    
# 1 0
# 0 1
# 1 1
# 1 2
# 2 3
