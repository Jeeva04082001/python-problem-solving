# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]


# strs = ["act","pots","tops","cat","stop","hat"]

# dic={}
# for x in strs:
#     key = "".join(sorted(x))
#     if key not in dic:
#         dic[key]=[]
#     dic[key].append(x)    
# print(dic.values())







# Imports you’ll need (at top of file):
# from collections import defaultdict
# from typing import List


# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         # print(strs)
#         d={}
#         for x in strs:
#             key="".join(sorted(x))
#             # print(key)
#             if key not in d:
#                 d[key]=[]
#             d[key].append(x) 
#         # print(d)     
#         return list(d.values())    


# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         d=defaultdict(list)
#         for x in strs:
#             key="".join(sorted(x))
#             d[key].append(x)
#         return list(d.values())    
        

# ========================================================================

# strs = ["act","pots","tops","cat","stop","hat"]

# anagram={}
# for x in strs:
#     key = "".join(sorted(x))
#     if key not in anagram:
#         anagram[key]=[]
#     anagram[key].append(x)
# print(list(anagram.values()))    


# from collections import defaultdict
# strs = ["act","pots","tops","cat","stop","hat"]
# anagram = defaultdict(list)
# for x in strs:
#     key = "".join(sorted(x))
#     anagram[key].append(x)
# print(list(anagram.values())) 













