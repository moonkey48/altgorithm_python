import sys
input = sys.stdin.readline

n, min_sum = list(map(int, input().rstrip().split(" ")))

num_list = list(map(int, input().rstrip().split(" ")))

length = 1
st = 0
en = 1
min_length = n -1
temp_sum = num_list[st] + num_list[en]
not_solved = True


while st < n  or n != 1:
    # print([st,en,min_length, temp_sum])
    length = en - st
    
    if st == n:
        break
    if num_list[st] >= min_sum or num_list[en] >= min_sum:
        not_solved = False
        min_length = 0
        break
    elif temp_sum < min_sum:
        if en < n - 1:
            en += 1
            temp_sum += num_list[en]
        else:
            temp_sum -= num_list[st]
            st += 1
            if min_length >= length and temp_sum >= min_sum:
                min_length = length
    else:
        if min_length >= length and temp_sum >= min_sum:
            not_solved = False
            min_length = length
        temp_sum -= num_list[st]
        st += 1
        
        
if not_solved:
    if n == 1:
        print(num_list[0])
    else:
        print(0)
else:
    print(min_length + 1)


