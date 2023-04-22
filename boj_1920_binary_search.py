import sys
input = sys.stdin.readline

n = int(input())
a_list = list(map(int, input().strip().split(" ")))
a_list.sort()

m = int(input())
check_list = list(map(int, input().strip().split(" ")))

def b_search(value):
    res = 0
    st = 0
    en = len(a_list) - 1
    while st <= en:
        mid = int((st + en)/2)
        # print([value,st,mid,en])
        if a_list[mid] == value:
            res = 1
            break
        elif a_list[mid] < value:
            st = mid + 1
            continue
        elif a_list[mid] > value:
            en = mid - 1
    
    return res

for item in check_list:
    result = b_search(item)
    print(result)

