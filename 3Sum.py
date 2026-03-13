# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]

# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].


# nums = [-1,0,1,2,-1,-4]
# res=[]
# for x in range(len(nums)):
#     for y in range(x+1,len(nums)):
#         for z in range(y+1,len(nums)):
#             if nums[x] + nums[y] + nums[z] == 0:
#                 val = sorted([nums[x],nums[y],nums[z]])
#                 if val not in res:
#                     res.append(val)

# print(res)




# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 for k in range(j+1, len(nums)):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         triple = sorted([nums[i],nums[j],nums[k]])
#                         if triple not in res:
#                             res.append(triple)
#         return res



















