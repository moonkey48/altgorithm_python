import sys

l, c = list(map(int, input().rstrip().split(" ")))

alphabets = list(map(str, input().rstrip().split(" ")))
m_alphabets = ['a', 'e', 'i', 'o', 'u']

cur_arr = []
alphabets = sorted(alphabets)

def check_arr():
    vow_count = 0
    con_count = 0
    for a in cur_arr:
        if a in m_alphabets:
            vow_count += 1
        else:
            con_count += 1
    if vow_count >= 1 and con_count >= 2:
        print(''.join(e for e in cur_arr))

def find_alpha(count, idx):
    if count == l:
        check_arr()
        return
    for j in range(idx, c):
        cur_arr.append(alphabets[j])
        find_alpha(count + 1, j + 1)
        cur_arr.pop()

find_alpha(0,0)
