class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Single_linked_list:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        output = []
        temp = self.head
        while temp:
            output.append(str(temp.value))
            temp = temp.next
        
        print("-> ".join(output))
    
    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


linked_list = Single_linked_list(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
print('Before:')
linked_list.print_list()
linked_list.reverse()
print('After:')
linked_list.print_list()

########################################################################################################################

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class Double_list:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self,value):
        new_node= Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length +=1 

    def double_print(self):
        output = []
        temp = self.head
        while temp:
            output.append(str(temp.value))
            temp = temp.next
        
        print("<->".join(output))

    def reverse(self):
        temp = self.head
        while temp:
            temp.prev , temp.next = temp.next, temp.prev
            temp = temp.prev
        
        self.head, self.tail = self.tail, self.head

    

linked_list = Double_list(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
print('Before:')
linked_list.double_print()
linked_list.reverse()
print('After:')
linked_list.double_print()