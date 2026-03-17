# Read this 
"""
Hash Table Explanation (Python: dict, set vs list)

A hash table is a data structure that stores data using a hash function.

Hash Function:
    Converts a key into an integer index.

    index = hash(key) % table_size

The computed index determines where the value is stored internally.
Because of direct index access, hash tables provide:

    • O(1) average time complexity for:
        - Search
        - Insert
        - Delete


Why `dict` is a Hash Table:
--------------------------------
Example:
    my_dict = {"apple": 10, "banana": 20}

When checking:
    "apple" in my_dict

Python:
    1. Computes hash("apple")
    2. Calculates index using modulo
    3. Directly accesses that location

It does NOT scan all keys.
Therefore, lookup is O(1) on average.


Why `set` is a Hash Table:
--------------------------------
Example:
    my_set = {1, 2, 3}

When checking:
    2 in my_set

Python:
    1. Computes hash(2)
    2. Maps to index
    3. Directly checks that position

Again, O(1) average lookup time.


Why `list` is NOT a Hash Table:
--------------------------------
Example:
    my_list = [10, 20, 30, 40]

When checking:
    30 in my_list

Python performs linear search:
    1. Compare with 10
    2. Compare with 20
    3. Compare with 30
    4. Stop

This requires scanning elements one by one.

Time Complexity:
    O(n)


Summary:
--------------------------------
dict  → Hash table (O(1) average lookup)
set   → Hash table (O(1) average lookup)
list  → Dynamic array (O(n) lookup)

Hash tables provide faster membership testing because
they compute an index using a hash function instead
of scanning elements sequentially.
"""


class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
      
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash  

    def print_table(self):
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys


my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)

print('Bolts:', my_hash_table.get_item('bolts'))
print('Washers:', my_hash_table.get_item('washers'))
print('Lumber:', my_hash_table.get_item('lumber'))

print(my_hash_table.keys())

"""
    EXPECTED OUTPUT:
    ----------------
    Bolts: 1400
    Washers: 50
    Lumber: None

"""