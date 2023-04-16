import sys
input = sys.stdin.readline
n, total = list(map(int,input().split(" ")))

coin_list = []
for i in range(n):
    coin_list.append(int(input()))

current_coin = n - 1
count = 0 
while total > 0:
    if  total - coin_list[current_coin] < 0:
        current_coin -= 1
    elif total - coin_list[current_coin] >= 0:
        total -= coin_list[current_coin]
        count += 1

print(count)
