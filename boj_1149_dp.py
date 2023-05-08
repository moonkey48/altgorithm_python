import sys
input = sys.stdin.readline

n = int(input())
price_list = []
for i in range(n):
    price_list.append(list(map(int, input().rstrip().split(" "))))
for i in range(1,len(price_list)):
    price_list[i][0] = min(price_list[i - 1][1], price_list[i - 1][2]) + price_list[i][0]
    price_list[i][1] = min(price_list[i - 1][0], price_list[i - 1][2]) + price_list[i][1]
    price_list[i][2] = min(price_list[i - 1][0], price_list[i - 1][1]) + price_list[i][2]
print(min(price_list[n - 1][0], price_list[n - 1][1], price_list[n - 1][2]))