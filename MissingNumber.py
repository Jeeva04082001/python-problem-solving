
# Given an array nums containing n integers in the range [0, n] without any duplicates, return the single number in the range that is missing from nums.

# Follow-up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

# Example 1:

# Input: nums = [1,2,3]

# Output: 0
# Explanation: Since there are 3 numbers, the range is [0,3]. The missing number is 0 since it does not appear in nums.


# Example 2:

# Input: nums = [0,2]

# Output: 1

# nums = [0,2]
# num_set=set(nums)
# n=len(nums)
# # print(n)
# for x in range(n+1):
#     # print(x)
#     if x not in num_set:
#         print(x)







# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n=len(nums)
#         nums.sort()
#         for x in range(n):
#             if nums[x] != x:
#                 return x
#         return n  



# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         num_set=set(nums)
#         n=len(nums)
#         for x in range(n+1):
#             if x not in num_set:
#                 return x
            


# nums = [0,2,4]
# n=len(nums)
# nums.sort()
# for x in range(n):
#     if nums[x] != x:
#         print(x)


nums = [0,2,4]
n=len(nums)
seen=set(nums)
for x in range(n+1):
    if x not in seen:
        print(x)






