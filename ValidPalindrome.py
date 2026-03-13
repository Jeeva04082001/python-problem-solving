# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

# Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

# Example 1:

# Input: s = "Was it a car or a cat I saw?"

# Output: true
# Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.



# s = "Was it a car or a cat I saw?"
# res=""
# for ch in s:
#     if ch.isalnum():
#         res+=ch.lower()
# print(res == res[::-1])





# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         newStr = ''
#         for c in s:
#             if c.isalnum():
#                 newStr += c.lower()
#         return newStr == newStr[::-1]






s = "Was it a car or a cat I saw?"
res=''
for x in s:
    if x.isalnum():
        res+=x.lower()
print(res == res[::-1])
  











