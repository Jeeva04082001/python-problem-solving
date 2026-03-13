# Products of Array Except Self

# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

# Follow-up: Could you solve it in 
# O
# (
# n
# )
# O(n) time without using the division operation?

# Example 1:

# Input: nums = [1,2,4,6]

# Output: [48,24,12,8]

# nums = [1,2,4,6]
# res=[]
# for x in nums:
#     prod=1
#     for y in nums:
#         if x == y:
#             continue
#         prod*=y
#     res.append(prod)    
# print(res)



# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         res=[]
#         for x in nums:
#             prod=1
#             for y in nums:
#                 if x==y:
#                     continue
#                 prod *=y
#             res.append(prod)  
#         return res 



# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n=len(nums)
#         res=[]
#         for x in range(n):
#             prod=1
#             for y in range(n):
#                 if x == y:
#                     continue
#                 prod *= nums[y]
#             res.append(prod)
#         return res  



# ================================================================================

# nums = [1,2,4,6]
# res=[]
# for x in nums:
#     prod=1
#     for y in nums:
#         if x == y:
#             continue
#         prod *=y
#     res.append(prod)    
# print(res)

