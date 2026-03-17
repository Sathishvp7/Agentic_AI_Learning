class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

          
    def __r_insert(self, current_node, value):
        # If current_node is None, we have reached a leaf node and 
        # insert a new node with the given value.
        if current_node == None: 
            return Node(value)   
        # If the value is less than the value of the current_node, we insert
        # the value into the left subtree.
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        # If the value is greater than the value of the current_node, we insert
        # the value into the right subtree.
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value) 
        # Return the modified current_node after inserting the value.
        return current_node    
    
    def r_insert(self, value):
        # If the tree is empty, create a new node and make it the root node.
        if self.root == None: 
            self.root = Node(value)
        # Call the private helper method __r_insert with the root node and the value
        # to be inserted. 
        self.__r_insert(self.root, value) 


    def min_value(self, current_node):
        # Iterate until no left child is found
        while current_node.left is not None:
            # Move to the left child of current node
            current_node = current_node.left
        # Return the value of the leftmost node
        return current_node.value
        
    def __delete_node(self, current_node, value):
        # Return None if the current node is None
        if current_node == None:
            return None
        # Traverse the left subtree if value is smaller
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        # Traverse the right subtree if value is larger
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        # If value is found, delete the node
        else:
            # Case 1: No children, return None to delete
            if current_node.left == None and current_node.right == None:
                return None
            # Case 2: No left child, return right child
            elif current_node.left == None:
                current_node = current_node.right
            # Case 3: No right child, return left child
            elif current_node.right == None:
                current_node = current_node.left
            # Case 4: Two children, find min in right subtree
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        # Return the current node after deletion
        return current_node
    
    def delete_node(self, value):
        # Call the helper method to delete the node
        # You may see other implementations that write it this way:
        # self.__delete_node(self.root, value)
        # but that way will not work when removing the root node
        self.root = self.__delete_node(self.root, value)


##########################################################   
##   Test code below will print output to "User logs"   ##
##########################################################

def check(expect, actual, message):
    print(message)
    print("EXPECTED:", expect)
    print("RETURNED:", actual)
    print("PASS" if expect == actual else "FAIL", "\n")


# test_delete_node_no_children
print("\n----- Test: Delete node with no children -----\n")
bst = BinarySearchTree()
values = [5, 3, 8]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
bst.delete_node(3)
check(None, bst.root.left, "Left child of root after deleting 3:")


# test_delete_node_only_left_child
print("\n----- Test: Delete node with only left child -----\n")
bst = BinarySearchTree()
values = [5, 3, 8, 1]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
bst.delete_node(3)
check(1, bst.root.left.value, "Left child of root after deleting 3:")


# test_delete_node_only_right_child
print("\n----- Test: Delete node with only right child -----\n")
bst = BinarySearchTree()
values = [5, 3, 8, 9]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
bst.delete_node(8)
check(9, bst.root.right.value, "Right child of root after deleting 8:")


# test_delete_node_two_children
print("\n----- Test: Delete node with two children -----\n")
bst = BinarySearchTree()
values = [5, 3, 8, 1, 4, 7, 9]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
bst.delete_node(3)
check(4, bst.root.left.value, "Left child of root after deleting 3:")


# test_delete_root
print("\n----- Test: Delete root -----\n")
bst = BinarySearchTree()
values = [5, 3, 8]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
bst.delete_node(5)
check(8, bst.root.value, "Root value after deleting 5:")


# test_delete_non_existent_node
print("\n----- Test: Attempt to delete a non-existent node -----\n")
bst = BinarySearchTree()
values = [5, 3, 8]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
original_root_value = bst.root.value
bst.delete_node(10)
check(original_root_value, bst.root.value, "Root value after attempting to delete 10:")
