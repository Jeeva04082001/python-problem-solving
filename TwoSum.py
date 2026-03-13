# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

# Example 1:

# Input: 
# nums = [3,4,5,6], target = 7

# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].



# nums = [3,4,5,6]
# target = 7

# for x in range(len(nums)):
#     for y in range(x+1,len(nums)):
#         if nums[x] + nums[y] == target:
#             print([x,y])




# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for x in range(len(nums)):
#             for y in range(x+1, len(nums)):
#                 if nums[x] + nums[y] == target:
#                     return [x,y]












