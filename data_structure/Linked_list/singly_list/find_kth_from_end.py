"""
LL: Find Kth Node From End ( ** Interview Question)
Implement the find_kth_from_end function, which takes the LinkedList (ll) and an integer k as input, and returns the k-th node from the end of the linked list WITHOUT USING LENGTH.



NOTE: This is a SEPARATE FUNCTION that is NOT a method within the LinkedList class.  This means you need to indent the function all the way to the LEFT. 



Given this LinkedList:

1 -> 2 -> 3 -> 4 -> 5

If k=1 then return the first node from the end (the last node) which contains the value of 5.

If k=2 then return the second node from the end which contains the value of 4, etc.

If the index is out of bounds, the program should return None.

The find_kth_from_end function should follow these requirements:

The function should utilize two pointers, slow and fast, initialized to the head of the linked list.

The fast pointer should move k nodes ahead in the list.

If the fast pointer becomes None before moving k nodes, the function should return None, as the list is shorter than k nodes.

The slow and fast pointers should then move forward in the list at the same time until the fast pointer reaches the end of the list.

The function should return the slow pointer, which will be at the k-th position from the end of the list.
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

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True  
 
  
def find_kth_from_end(self, k):
    slow = self.head
    fast = self.head

    # Move fast k steps ahead
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next

    # Move both pointers until fast reaches the end
    while fast:
        slow = slow.next
        fast = fast.next

    return slow




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4



"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""

