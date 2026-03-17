"""
Write a function called first_non_repeating_char(string) that finds the first non-repeating character in the given string using a hash table (dictionary). If there is no non-repeating character in the string, the function should return None.

For example, if the input string is "leetcode", 
the function should return "l" because "l" is the first character that appears only once in the string. 
Similarly, if the input string is "hello", the function should return "h" because "h" is the first non-repeating character in the string.
"""

def first_non_repeating_char(strs):
    my_dict = {}
    for i in strs:
        my_dict[i] = my_dict.get(i,0)+1

    for key,value in my_dict.items():
        if value == 1:
            return key
        break
    
    return None

print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""