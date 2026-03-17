"""
Bubble Sort of LL ( ** Interview Question)
Assignment:

Your task is to implement the bubble_sort method within the LinkedList class. 
The bubble_sort method should sort the elements of the linked list in ascending order based on their values. 
The sorting should be done in-place, meaning you should not create a new linked list but rather modify the existing one.

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
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
            self.tail = new_node
        self.length += 1

    def bubble_sort(self):

        if self.length < 2:
            return None
        
        for i in range(self.length - 1, 0, -1):
            current_node = self.head
            for j in range(i):
                next_node = current_node.next

                if current_node.value > next_node.value:
                    current_node.value, next_node.value = next_node.value, current_node.value
                
                current_node = current_node.next





my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.bubble_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""

