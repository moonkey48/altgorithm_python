class ListNode:
    def __init__(self,val): 
        self.val =  val
        self.next = None
def printNodes(node: ListNode):
    current_node = node
    while current_node.next is not None:
        print(current_node.val, end=' ')
        current_node = current_node.next

class LinkedList:
    def __init__(self):
        self.head = None
    def addAtHead(self, val):
        node = ListNode(val)
        node.next = self.head
        self.head = node
    def addBack(self, val):
        node = ListNode(val)
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = node
    def findNode(self, val):
        current_node = self.head
        while current_node is not None:
            if current_node.val == val:
                return current_node
            current_node = current_node.next
        raise RuntimeError('Node Not Found')
    def addAfter(self, node, val):
        new_node = ListNode(val)
        new_node.next = node.next
        node.next = new_node
    def deleteAfter(self, prev_node):
        if prev_node.next is not None:
            prev_node.next = prev_node.next.next