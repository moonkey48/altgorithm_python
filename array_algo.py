# 1차
# S = input()

# arr = []

# for i in range(ord('a'), ord('z') + 1):
#     num = 0
#     for s in S:
#         if ord(s) == i:
#             num += 1
#     arr.append(num)

# print(' '.join(map(str, arr)))


# 2차 수정
# 기존에 26번을 도는 것이 아닌 문자열만 도는 것으로 변경
S = input()
arr = [0] * 26

for s in S:
    arr[ord(s) - 97] += 1

print(' '.join(map(str, arr)))
