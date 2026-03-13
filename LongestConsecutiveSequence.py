# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [2,20,4,10,3,4,5]

# Output: 4
# Explanation: The longest consecutive sequence is [2, 3, 4, 5].



# nums = [2,20,4,10,3,4,5]
# seen = set(nums)
# count=0
# for x in nums:
#     if x-1 not in seen:
#         curr =1
#         while x+curr in seen:
#             curr+=1
#         count = max(curr,count)    
# print(count)


# nums = [2,20,4,10,3,4,5]
# seen = set(nums)
# length=0
# for x in nums:
#     if x-1 not in seen:
#         curr =x
#         length =1
#         while x+curr in seen:
#             curr+=1
#             length+=1
#         length = max(curr,length)    
# print(length)


# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         seen=set(nums)
#         print(seen)
#         count=0
#         for x in seen:
#             if x-1 not in seen:
#                 curr=1
#                 while x+curr in seen:
#                     curr +=1
#                 count=max(count,curr)   
#         return count  

# ====================================================================

nums = [2,20,4,10,3,4,5]
seen = set(nums)
count = 0
for x in nums:
    if x-1 not in seen:
        curr =1
        while x+curr in seen:
            curr+=1
        count = max(curr,count)
print(count)


