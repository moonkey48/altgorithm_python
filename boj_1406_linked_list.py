import sys
input = sys.stdin.readline

class DList:
    class Node:
        def __init__(self, item, prev, next):
            self.item = item
            self.prev = prev
            self.next = next
            
    def __init__(self):
        self.head = self.Node(None,None,None)
        self.tail = self.Node(None,self.head, None)
        self.head.next = self.tail
        self.cur = self.tail
        
    def insert(self, node, item):
        prevNode = node.prev
        new_node = self.Node(item, prevNode, node)
        node.prev = new_node
        prevNode.next = new_node
        
    def delete(self, node):
        prev_node = node.prev
        rear_node = node. next
        prev_node.next = rear_node
        rear_node.prev = prev_node
        
    def print_list(self):
        p = self.head.next
        while p != self.tail:
            if p.next != self.tail:
                print(p.item, end="")
            else:
                print(p.item)
            p = p.next

s = list(input().rstrip())
dl = DList()

for i in range(len(s)):
    dl.insert(dl.tail, s[i])

for i in range(int(input())):
    o = input().split()
    
    if(o[0] == "L"):
        if(dl.cur.prev.prev != None):
            dl.cur = dl.cur.prev
    elif(o[0] == "D"):
        if(dl.cur.next != None):
            dl.cur = dl.cur.next
    elif(o[0] == "B"):
        if(dl.cur.prev.prev != None):
            dl.delete(dl.cur.prev)
    else:
        dl.insert(dl.cur, o[1])
dl.print_list()