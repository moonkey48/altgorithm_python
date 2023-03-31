
input  = '''abcd
3
P x
L
P y'''

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def printNodes(node:ListNode):
    crnt_node = node
    while crnt_node is not None:
        print(crnt_node.val, end=' ')
        crnt_node = crnt_node.next

class SLinkedList:
    def __init__(self):
        self.head = ListNode('')
        
    def addAtHead(self, val): #O(1)
        node = ListNode(val)
        node.next = self.head
        self.head = node

    #but when the list
    def addBack(self, val): #O(n)
        node = ListNode(val)
        crnt_node = self.head
        while crnt_node.next:
            crnt_node = crnt_node.next
        crnt_node.next = node

    def findNode(self, val): #O(n)
        crnt_node = self.head
        while crnt_node is not None:
            if crnt_node.val == val:
                return crnt_node
            crnt_node = crnt_node.next
        raise RuntimeError('Node not found')

    def addAfter(self, node, val): #O(1)
        new_node = ListNode(val)
        new_node.next = node.next
        node.next = new_node

    def deleteAfter(self, prev_node): #O(1)
        if prev_node.next is not None:
            prev_node.next = prev_node.next.next
            
linked_list = SLinkedList()

arr = list(map(str, input.split('\n')))

base_str = arr[0]
input_length = arr[1]
cursor = len(base_str)

for i in list(base_str):
    linked_list.addBack(i)
    

for pos in range(2,int(input_length)+2):
    command = arr[pos].split(' ')
    
    if command[0] == 'L':
        if cursor != 0:
            cursor -= 1
    elif command[0] == 'D':
        if cursor != len(base_str):
            cursor += 1
    elif command[0] == 'B':
        print('delete')
    
        
            
        

# L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
# D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
# B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
# 삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
# P $	$라는 문자를 커서 왼쪽에 추가함