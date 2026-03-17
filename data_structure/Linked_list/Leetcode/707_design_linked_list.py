class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Helper function (optimized traversal)
    def _get_node(self, index):
        # If index is in first half → start from head
        if index < self.size // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        # If index is in second half → start from tail
        else:
            current = self.tail
            for _ in range(self.size - 1, index, -1):
                current = current.prev
        
        return current

    # Get value at index
    def get(self, index: int) -> int:
        print(index)
        if index < 0 or index >= self.size:
            return -1
        
        current = self._get_node(index)
        return current.val

    # Add at head
    def addAtHead(self, val: int) -> None:
        new_node = Node(val)

        if self.size == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.size += 1

    # Add at tail
    def addAtTail(self, val: int) -> None:
        new_node = Node(val)

        if self.size == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.size += 1

    # Add at index
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
            return
        
        if index == self.size:
            self.addAtTail(val)
            return

        new_node = Node(val)
        current = self._get_node(index)

        prev_node = current.prev

        prev_node.next = new_node
        new_node.prev = prev_node

        new_node.next = current
        current.prev = new_node

        self.size += 1

    # Delete at index
    def deleteAtIndex(self, index: int) -> None:
        
        if index < 0 or index >= self.size:
            return

        current = self._get_node(index)

        if self.size == 1:
            self.head = self.tail = None
        elif current == self.head:
            self.head = current.next
            self.head.prev = None
        elif current == self.tail:
            self.tail = current.prev
            self.tail.next = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev

        self.size -= 1

        
myLinkedList =  MyLinkedList()
myLinkedList.addAtHead(1)
myLinkedList.addAtTail(3)
myLinkedList.addAtIndex(1, 2)    # linked list becomes 1->2->3
myLinkedList.get(1)            #return 2
myLinkedList.deleteAtIndex(1)   # now the linked list is 1->3
myLinkedList.get(1)             # return 3

