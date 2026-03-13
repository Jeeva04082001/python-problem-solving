# You are given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.

# Example 1:

# Input: nums1 = [1,2,3], nums2 = [2,4,6]

# Output: [[1,3],[4,6]]


nums1 = [1,2,3]
nums2 = [2,4,6]
a=set(nums1)
b=set(nums2)
l1,l2 = [],[]

for x in a:
    if x not in b:
        l1.append(x)
for y in b:
    if y not in a:
        l2.append(y)        

print([l1,l2])


# ==============================================================================


# class Solution:
#     def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
#         a,b=set(nums1),set(nums2)
#         l1,l2=[],[]
#         for x in a:
#             if x not in b:
#                 l1.append(x)
#         for y in b:
#             if y not in a:
#                 l2.append(y)

#         return [l1,l2]       
