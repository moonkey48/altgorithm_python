import sys
sys.setrecursionlimit(100000)
a = str(sys.stdin.readline().rstrip())

max_num = ""
min_num = ""

def find_max(index, m_length, sum):
    global max_num
    if index >= len(a):
        for _ in range(m_length):
            sum += "1"
        max_num = sum
        return
    if a[index] == "M":
        m_length += 1
    else:
        sum += "5"
        for _ in range(m_length):
            sum += "0"
        m_length = 0
    find_max(index + 1, m_length, sum)
    
def find_min(index, m_length, min_sum):
    global min_num
    if index >= len(a):
        if m_length > 0:
            min_sum += "1"
            for _ in range(m_length - 1):
                min_sum += "0"
        min_num = min_sum
        return
    if a[index] == "M":
        m_length += 1
    else:
        if m_length > 0:
            min_sum += "1"
            for _ in range(m_length - 1):
                min_sum += "0"
        min_sum += "5"
        m_length = 0
    find_min(index + 1, m_length, min_sum)

find_max(0,0,"")
print(max_num)

find_min(0,0,"")
print(min_num)