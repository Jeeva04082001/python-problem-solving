# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# nums = [1, 2, 3, 3]

# Example 1:
# Input: nums = [1, 2, 3, 3]
# Output: true

# Example 2:
# Input: nums = [1, 2, 3, 4]
# Output: false

# def hasDuplicate(nums):

#     seen=set()
#     for x in nums:
#         if x in seen:
#             return True
#         seen.add(x)
#     return False 
# nums = [1, 2, 3, 3]
# print(hasDuplicate(nums))  




# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         dub = []
#         for x in nums:
#             if x in dub:
#                 return True
#             dub.append(x)    
#         return False    



# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         seen = set()
#         for x in nums:
#             if x in seen:
#                 return True
#             seen.add(x)
#         return False 
        

















