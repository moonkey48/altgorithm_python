import sys

input = sys.stdin.readline

class Queue:
    def __init__(self):
        self.q = [0] * 10_001
        self.f = 0
        self.r = 0  
    def push(self, val):
        self.q[self.r] = val
        self.r += 1
    def pop(self):
        if self.f != self.r:
            print(self.q[self.f], end="\n")
            self.f += 1
        else:
            print(-1, end="\n")
    def size(self):
        print(self.r - self.f, end="\n")
    def empty(self):
        if self.f == self.r:
            print(1, end="\n")
        else:
            print(0, end="\n")
    def front(self):
        if self.f == self.r:
            print(-1, end="\n")
        else: 
            print(self.q[self.f], end="\n")
    def back(self):
        if self.f == self.r:
            print(-1, end="\n")
        else:
            print(self.q[self.r - 1], end="\n")

input_length = int(input())
queue = Queue()
input_list = [sys.stdin.readline() for _ in range(input_length)]

for i in input_list:
    o = i.split()
    if(o[0] == 'push'):
        queue.push(o[1])
    elif(o[0] == 'front'):
        queue.front()
    elif(o[0] == 'back'):
        queue.back()
    elif(o[0] == 'size'):
        queue.size()
    elif(o[0] == 'empty'):
        queue.empty()
    elif(o[0] == 'pop'):
        queue.pop()  
        
