# You are given an integer array nums of size n, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

# Note: [1,0,3,2] and [3,0,1,2] are considered as same quadruplets.

# Example 1:

# Input: nums = [3,2,3,-3,1,0], target = 3

# Output: [[-3,0,3,3],[-3,1,2,3]]


nums = [3,2,3,-3,1,0]
target = 3
res=[]
for w in range(len(nums)):
    for x in range(w+1,len(nums)):
        for y in range(x+1,len(nums)):
            for z in range(y+1,len(nums)):
                if nums[w]+nums[x]+nums[y]+nums[z]==target:
                    val=sorted([nums[w],nums[x],nums[y],nums[z]])
                    if val not in res:
                        res.append(val)
print(res)


# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         res=[]
#         for w in range(len(nums)):
#             for x in range(w+1,len(nums)):
#                 for y in range(x+1,len(nums)):
#                     for z in range(y+1,len(nums)):
#                         if nums[w] + nums[x] + nums[y] + nums[z] == target:
#                             val = sorted([nums[w],nums[x],nums[y],nums[z]])
#                             if val not in res:
#                                 res.append(val)
#         return res                    














