import sys
input = sys.stdin.readline

input_str = input()

total = 0
temp = ''
is_minus = False

for char in input_str:

    if char.isdigit():
        temp += char
    elif char == '-':
        if is_minus == True:
            total -= int(temp)   
            temp = '' 
        else:
            total += int(temp)
            temp = ''
            is_minus = True
    else:
        if is_minus == False:
            total += int(temp)
            temp = ''
        else:
            total -= int(temp)
            temp = ''
print(total)
