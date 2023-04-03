import sys

input = sys.stdin.readline
input_list = []

while True:
    val = input().rstrip()
    if str(val) == '.':
        break
    input_list.append(val)

for input_str in input_list:
    res = 'yes'

    stack = []
    for char in input_str:
        if char == '(' or char == '[':
            stack.append(char)        
        elif char == ')':
            if len(stack) == 0:
                res = 'no'
            elif stack[len(stack) - 1] == '[':
                res = 'no'
            elif stack[len(stack) - 1] == '(':
                stack.pop()
        elif char == ']':
            if len(stack) == 0:
                res = 'no'
            elif stack[len(stack) - 1] == '(':
                res = 'no'
            elif stack[len(stack) - 1] == '[':
                stack.pop()
    if len(stack) != 0:
        res = 'no'
    print(res)
                
    
