import sys

input = sys.stdin.readline()
n = int(input)
answer = 0
    

cur = []
total = 0

def find_num(num_before, count, max_count):
    global total
    global answer
    
    if count == max_count:
        joined = int(''.join(str(e) for e in cur))
        total += 1
        # print([total, joined])
        if total == n:
            answer = joined 
        return
    else:
        for i in range(10):
            if i < num_before:
                cur.append(i)
                find_num(i, count + 1, max_count)
                cur.pop()


for j in range(1, 11):
    for k in range(10):
        if j == 1 and k == 0:
            continue
        cur.append(k)
        find_num(k ,1, j)
        cur.pop()    

if answer == 0:
    if n != 0:
        print(-1)
    else:
        print(0)
else:
    print(answer)