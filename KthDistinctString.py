# Kth Distinct String in an Array


# A distinct string is a string that is present only once in an array.

# You are given an array of strings arr, and an integer k, return the k-th distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

# Note that the strings are considered in the order in which they appear in the array.

# Example 1:

# Input: arr = ["d","b","c","b","c","a"], k = 2

# Output: "a"


# Explanation: The only distinct strings in arr are "d" and "a".
# "d" appears 1st, so it is the 1st distinct string.
# "a" appears 2nd, so it is the 2nd distinct string.
# Since k == 2,"a" is returned.




# arr = ["d","b","c","b","c","a"]
# k = 2
# res={}
# uniq=[]
# for x in arr:
#     res[x]=res.get(x,0)+1
# for key,val in res.items():
#     if val == 1:
#         uniq.append(key)
# if k <= len(uniq):
#     print(uniq[k-1])
    
# ===================================================

# arr = ["d","b","c","b","c","a"]
# k = 2
# res={}
# uniq=[]
# for x in arr:
#     res[x]=res.get(x,0)+1
# for key,val in res.items():
#     if val == 1:
#         uniq.append(key)
# print(uniq[0])





# =====================================================================================

# class Solution:
#     def kthDistinct(self, arr: List[str], k: int) -> str:

#         res={}
#         uniq=[]
#         for x in arr:
#             res[x]=res.get(x,0)+1

#         for key,val in res.items():
#             if val == 1:
#                 uniq.append(key)   
#         if k <= len(uniq):
#             return uniq[k-1]
#         return ""    
        









