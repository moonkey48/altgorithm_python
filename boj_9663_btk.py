import sys

n = int(sys.stdin.readline())

isused_col = [False] * n 
isused_left = [False] * (2 * n -1)
isused_right = [False] * (2 * n  - 1)



def find_q(count):
    global method_count
    if count == n:
        method_count += 1
        return 
    for i in range(n):
        if isused_col[i] != False or isused_left[i + count] != False or isused_right[count - i + n -1] != False:
            continue
        isused_col[i] = True
        isused_left[count + i] = True
        isused_right[count - i + n -1] = True
        find_q(count + 1)            
        isused_col[i] = False
        isused_left[count + i] = False
        isused_right[count - i + n -1] = False
            
method_count = 0
find_q(0)
print(method_count)

