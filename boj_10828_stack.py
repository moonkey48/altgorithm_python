import sys


class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, val):
        self.stack.append(val)
    def pop(self):
        if len(self.stack) == 0:
            print(-1)
        else:
            print(self.stack.pop())
    def size(self):
        print(len(self.stack))
    def empty(self):
        if len(self.stack) == 0:
            print(1)
        else:
            print(0)
    def top(self):
        if len(self.stack) == 0:
            print(-1)
        else:
            print(self.stack[len(self.stack) -1])



input_length = input()
    
input_list = [sys.stdin.readline().strip() for _ in range(int(input_length))]

stack = Stack()


for item in input_list:
    splited = item.split(' ')
    if splited[0] == 'push':
        stack.push(int(splited[1]))
    elif splited[0] == 'pop':
        stack.pop()
    elif splited[0] == 'size':
        stack.size()
    elif splited[0] == 'empty':
        stack.empty()
    elif splited[0] == 'top':
        stack.top()
