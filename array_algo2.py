
# 1차 풀이
# O(N2)라서 시간 복잡도가 너무 오래걸린다.
# arr = [1,99,32]
# res = 0

# for num in arr:
#     if 100-num in arr:
#         res = 1

# print(res)


# 2차 풀이
# 1-99까지 배열의 index에 0을 넣어서 각 숫자바다 카운터 값이 있는지 여부만 체크
# O(N)
arr2 = [0] * 100
input_arr = [1,5,92,23,41]
res = 0

for i in input_arr:
    if arr2[100 - i] == 1:
        res =1
        break
    else:
        arr2[i] = 1

print(res)
