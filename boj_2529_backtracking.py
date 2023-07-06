import sys
input = sys.stdin.readline

n = int(input().rstrip())
signs = list(map(str, input().rstrip().split(" ")))

min_list = []
max_list = [-1 for _ in range(n + 1)]
num_used = [False for _ in range(10)]
res = []
def find_min(count):
    global min_list
    if count == n + 1:
        res.append(''.join(str(e) for e in min_list))
        return
    for num in range(10):
        if num_used[num] == True:
            continue
        if count == 0:
            min_list.append(num)
            num_used[num] = True
            find_min(count + 1)
            min_list.pop()
            num_used[num] = False
        else:
            if signs[count - 1] == ">" and min_list[count - 1] > num:
                min_list.append(num)
                num_used[num] = True
                find_min(count + 1)
                min_list.pop()
                num_used[num] = False
            elif signs[count - 1] == "<" and min_list[count - 1] < num:
                min_list.append(num)
                num_used[num] = True
                find_min(count + 1)
                min_list.pop()      
                num_used[num] = False  
find_min(0)
print(max(res))
print(min(res))
