class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None 
        else:       
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head =new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev  
        return temp
    
    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert_value(self,index,value):
        if index < 0  or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        new_node = Node(value)
        # get Index previous Node
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next.prev = new_node
        new_node.prev = temp
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
 
        temp = self.get(index)
        
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
 
        self.length -= 1
        return temp

        

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)


# (2) Items - Returns 2 Node
print(my_doubly_linked_list.pop().value)
# (1) Item -  Returns 1 Node
print(my_doubly_linked_list.pop().value)
# (0) Items - Returns None
print(my_doubly_linked_list.pop())

# prepend
print('\n Before Prepend')
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.print_list()
print('\nAfter Prepend')
my_doubly_linked_list.prepend(100)
my_doubly_linked_list.print_list()

#Pop First
print('\n Before Pop first')
my_doubly_linked_list.print_list()
print('\nAfter Pop first')
my_doubly_linked_list.pop_first()
my_doubly_linked_list.print_list()

# get value by index
print('get of index 1: ',my_doubly_linked_list.get(1).value)
print('get of index 2: ',my_doubly_linked_list.get(2).value)

# set by value
print('\n Before Set Value')
my_doubly_linked_list.print_list()
print('\nAfter Set Value')
my_doubly_linked_list.set_value(2,33)
my_doubly_linked_list.print_list()

#insert_value
print('\n Before insert_value')
my_doubly_linked_list.print_list()
print('\nAfter insert_value')
my_doubly_linked_list.insert_value(2,30)
my_doubly_linked_list.print_list()

# Remove
print('\n Before Remove')
my_doubly_linked_list.print_list()
print('\nAfter Remove')
my_doubly_linked_list.remove(1)
my_doubly_linked_list.print_list()

