# import sys
# input = sys.stdin.readline

# number_of_meeting = int(input())
# meetings = []

# for i in range(number_of_meeting):
#     item = list(map(int, input().rstrip().split(" ")))
#     meetings.append(item)
    

# print(meetings)
# meetings.sort(key= lambda x: (x[1], -x[0]))
# print(meetings)

# meeting_opened = []
# max_hour = meetings[len(meetings) -1][1]

    

# for i in range(max_hour + 1):
#     meeting_count = 0
#     for meeting in meetings:
#         if meeting[0] <=