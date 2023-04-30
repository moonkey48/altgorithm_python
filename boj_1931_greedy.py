import sys
input = sys.stdin.readline

n = int(input())
time_table = []
for i in range(n):
    time_table.append(list(map(int, input().rstrip().split(" "))))

time_table.sort(key = lambda x : x[1])
# print(time_table)

meeting_count = 0
end_time = False
cur_time = 0
pos = 0
st = 0
en = 0

# print(time_table)
while end_time == False:
    print("--")
    print([st,en,pos,meeting_count])
    print(time_table[pos])
    cur_time += 1
    if st < cur_time and cur_time < en:
        continue
    if pos == len(time_table) - 1:
        end_time = True
    
    last_meeting_time = time_table[pos][1]
    same_meetings = []
    same_meetings.append(time_table[pos][0])
    
    for i in range(pos + 1, len(time_table)):
        if time_table[i][1] == last_meeting_time:
            same_meetings.append(time_table[i][0])
        else:
            break
    
    for time in same_meetings:
        if time > en:
            st = time
            en = last_meeting_time
            meeting_count += 1
            break
    print([pos, cur_time, meeting_count])
    pos +=1

print(meeting_count)




