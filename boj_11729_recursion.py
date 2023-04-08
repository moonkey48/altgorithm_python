# - n-1 개의 원판을 기둥 1에서 기둥 2로 옮긴다.
# - n번의 원판을 기둥 1에서 기둥 3으로 옮긴다.
# - n-1개의 원판을 기둥 2에서 기둥 3으로 옮긴다.
# - ⇒ 원판이 n-1개일 때 옮길 수 있다면 원판이 n개일 때고 옮길 수 있다.

# - 원판이 1개일 때 원판을 내가 원하는 곳으로 옮길 수 있다.
# - 원판이 k개일 때 옮길 수 있으면 원판이 k+1개일 대에도 옮길 수 있다.
# 1. 함수의 정의
# ~~원판 n개를 1번 기둥에서 3번기둥으로 옮기는 방법을 출력하는 함수~~
# 원판 n개를 a번 기둥에서 b번 기둥으로 옮기는 방법을 출력하는 함수
# 2. base condition
# n이 1일 때 a에서 b로 옮긴다. 
# 3. 재귀 식
# n-1개의 원판을 기둥 a에서 기둥 6-a-b로 옮긴다
# n번의 원판을 기둥 a에서 기둥 b로 옮긴다
# n-1개의 원판을 기둥 6-a-b에서 기둥 b로 옳긴다.

def move(a,b, n):
    if n == 1:
        print(f"{a} {b}")
    move(a, 6-a-b, n-1)
    print(f"{a} {b}")
    move(6-b-a,b,n-1)
    
move(1,3,3)