# You are given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

# Return the sorted array.

# Example 1:

# Input: nums = [1,1,2,2,2,3]

# Output: [3,1,1,2,2,2]
# Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.



# nums = [1,1,2,2,2,3]
# res={}
# for x in nums:
#     res[x]=res.get(x,0)+1
#     # print(res)
# freq=sorted(nums, key= lambda x : (res[x],-x))
# print(freq)




# class Solution:
#     def frequencySort(self, nums: List[int]) -> List[int]:
#         res={}
#         for x in nums:
#             res[x]=res.get(x,0)+1
#         print(res)   
        
#         sortlist=sorted(nums,key=lambda x: (res[x],-x)) 
#         return sortlist
        



# Why this works on examples

# Example 1: nums = [1,1,2,2,2,3]
# counts: {1:2, 2:3, 3:1}
# sort by (freq, -value):
# 3 → (1, -3)
# 1 → (2, -1)
# 2 → (3, -2)
# Result: [3, 1, 1, 2, 2, 2]
# Example 2: nums = [2,3,1,3,2]
# counts: {2:2, 3:2, 1:1}
# sort: 1 first (freq 1), then 3 and 2 (freq 2) with larger values first → [1, 3, 3, 2, 2]
# If you want, I can walk through how to debug a failing case or adapt the code for other tie-break rules.




