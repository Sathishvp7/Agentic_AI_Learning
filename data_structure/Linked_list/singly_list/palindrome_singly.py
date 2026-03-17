class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        self.length += 1

    def is_palindrome(self):
        if not self.head or not self.head.next:
            return True

        # Step 1: Find middle
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev = None
        current = slow

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Step 3: Compare halves
        first_half = self.head
        second_half = prev

        while second_half:
            if first_half.value != second_half.value:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True


linked_list = SinglyLinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(2)
linked_list.append(1)

#Is palindrome
print(linked_list.is_palindrome())