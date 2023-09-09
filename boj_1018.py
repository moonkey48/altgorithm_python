import sys

input = sys.stdin.readline

n, m = list(map(int, input().split(" ")))
board = []

for _ in range(n):
    board.append(list(input().rstrip()))

def findCount(row,col):
    global board
    firstCount = 0
    nextColor = ''
    nextColor = 'W'
    
    for r in range(row, row + 8):
        for c in range(col, col + 8):
            if board[r][c] != nextColor:
                firstCount += 1
            if nextColor == 'B':
                nextColor = 'W'
            else:
                nextColor = 'B'
        if nextColor == 'B':
            nextColor = 'W'
        else:
            nextColor = 'B'
    secondCount = 0
    nextColor = 'B'
    for r in range(row, row + 8):
        for c in range(col, col + 8):
            if board[r][c] != nextColor:
                secondCount += 1
            if nextColor == 'B':
                nextColor = 'W'
            else:
                nextColor = 'B'
        if nextColor == 'B':
            nextColor = 'W'
        else:
            nextColor = 'B'
    
    return min(firstCount, secondCount)

smallCount = 64 
for row in range(n - 7):
    for col in range(m - 7):
        count = findCount(row, col)
        if count < smallCount:
            smallCount = count
print(smallCount)
