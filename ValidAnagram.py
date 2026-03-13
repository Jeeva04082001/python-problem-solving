# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"
# Output: true

# Example 2:
# Input: s = "jar", t = "jam"

# Output: false


s = "racecar" 
t = "carrace"

res1,res2={},{}
for x in s:
    res1[x]= res1.get(x,0)+1

for y in t:
    res2[y]=res2.get(y,0)+1

if res1 == res2:
    print(True)
else:
    print(False)


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         countS, countT = {},{}

#         for x in range(len(s)):

#             countS[s[x]] = countS.get(s[x],0) + 1
#             countT[t[x]] = countT.get(t[x],0) + 1

#         return countS == countT  






