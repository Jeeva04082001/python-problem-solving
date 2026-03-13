# You are given an array of positive integers nums, return the maximum possible sum of an strictly increasing subarray in nums.

# A subarray is defined as a contiguous sequence of numbers in an array.

# Note: An array is said to be strictly increasing if each element is strictly greater than its previous one (if exists).

# Example 1:

# Input: nums = [10,20,30,5,10,50]

# Output: 65
# Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.


# nums = [10,20,30,5,10,50]
# total=0
# res=0

# for i in range(1,len(nums)):
#     if nums[i] > nums[i-1]:
#         total+=nums[i]
#     else:
#         total=nums[i]    

#     res=max(res,total)
# print(res)













# class Solution:
#     def maxAscendingSum(self, nums: List[int]) -> int:
        
#         res=0
#         for x in range(len(nums)):
#             sum=nums[x]
#             for y in range(x+1,len(nums)):
#                 if nums[y] > nums[y-1]:
#                     sum += nums[y] 
#                 else:
#                     break
#             res=max(sum,res)
#         return res
    


# class Solution:
#     def maxAscendingSum(self, nums: List[int]) -> int:
#         res=nums[0]
#         total=nums[0]

#         for x in range(1,len(nums)):
#             if nums[x] > nums[x-1]:
#                 total += nums[x]
#             else:
#                 total = nums[x]

#             res=max(res,total)
#         return res     

