def group_anagrams(list1):
    my_dict = {}
    for i in list1:
        count = [0]*26
        for char in i:
            count[ord(char) - ord('a')] += 1
        
        key = tuple(count)
        if key not in my_dict:
            my_dict[key] = []
        my_dict[key].extend([i])

    return list(my_dict.values())



print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""




my_dict = {1:2,13:4,5:6}