import sys
input = sys.stdin.readline
isFind = False
year = 0

e,s,m = list(map(int, input().rstrip().split(" ")))

while isFind == False:
    year += 1
    res_e = year % 15 if year % 15 != 0 else 15
    res_s = year % 28 if year % 28 != 0 else 28
    res_m = year % 19 if year % 19 != 0 else 19
    if res_e == e and res_s == s and res_m == m:
            isFind == True
            break

print(year)