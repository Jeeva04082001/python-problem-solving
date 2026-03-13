
# You are given an array of string words, return all strings in words that are a substring of another word. You can return the answer in any order.

# Note: A substring is a contiguous non-empty sequence of characters within a string.

# Example 1:

# Input: words = ["mass","as","hero","superhero"]

# Output: ["as","hero"]

# words = ["mass","as","hero","superhero"]
# res=[]
# for x in words:
#     for y in words:
#         if x == y:
#             continue
#         if x in y:
#             res.append(x)
#             break
# print(res)





# ===========================================================================


# class Solution:
#     def stringMatching(self, words: List[str]) -> List[str]:
#         res=[]
#         for x in words:
#             for y in words:
#                 if x == y:
#                     continue
#                 if x in y:
#                     res.append(x)
#                     break
#         return res 


# class Solution:
#     def stringMatching(self, words: List[str]) -> List[str]:
#         res=[]
#         for x in range(len(words)):
#             for y in range(len(words)):
#                 if x == y:
#                     continue
#                 if words[x] in words[y]:
#                     res.append(words[x])
#                     break
#         return res 





















