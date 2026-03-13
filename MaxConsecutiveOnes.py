# You are given a binary array nums, return the maximum number of consecutive 1's in the array.

# Example 1:

# Input: nums = [1,1,0,1,1,1]

# Output: 3


# nums = [1,1,0,1,1,1]
# res = count = 0

# for x in nums:
#     count= count + 1 if x == 1 else 0
#     res=max(res,count)
# print(res)    

# ===================================================

# nums = [1,1,0,1,1,1]
# res = count = 0
# for x in nums:
#     if x==1:
#         count+=1
#     else:
#         count=0
#     res=max(count,res)
# print(res)            


# ===================================================================

# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         res = count=0
        
#         for x in nums:
#             count = count + 1 if x == 1 else 0
#             res = max(res,count)
#         return res    


# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         res=count=0
#         for num in nums:
#             if num == 1:
#                 count += 1
#                 res = max(res,count)
#             else:
#                 count = 0
#         return res


















