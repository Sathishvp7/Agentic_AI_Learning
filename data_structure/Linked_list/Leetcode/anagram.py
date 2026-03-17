"""
Docstring for Leetcode.anagram
What Is an Anagram?
Two strings are anagrams if:
They contain the same characters
With the same frequency
Order does NOT matter
"""
#Approach 1 — Using Sorting --Sorting each word takes: O(n log n) 
# Idea
# If two words are anagrams → their sorted form is same.

from collections import defaultdict

def groupAnagrams(strs):
    anagram_map = defaultdict(list)
    
    for word in strs:
        key = ''.join(sorted(word))
        anagram_map[key].append(word)
    
    return list(anagram_map.values())

strs = ["eat","tea","tan","ate","nat","bat"]
output = groupAnagrams(strs)
print(output)

# Approach 2 — Using Character Count (O(n*k)) --> Faster
# Instead of sorting,
# create a 26-length count array (for lowercase letters).

from collections import defaultdict

def groupAnagrams(strs):
    anagram_map = defaultdict(list)
    
    for word in strs:
        count = [0] * 26
        
        for char in word:
            count[ord(char) - ord('a')] += 1
        
        key = tuple(count)
        anagram_map[key].append(word)
    
    return list(anagram_map.values())

strs = ["eat","tea","tan","ate","nat","bat"]
output = groupAnagrams(strs)