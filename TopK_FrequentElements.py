# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

# Example 1:

# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]



# nums = [1,2,2,3,3,3]
# k = 2
# res={}
# for x in nums:
#     res[x]=res.get(x,0)+1
# lst=sorted(res,key=res.get, reverse=True)    
# print(lst[:k])



# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         res={}
#         for x in nums:
#             res[x] = res.get(x,0)+1
#         lst=sorted(res,key=res.get,reverse=True) 
#         return lst[:k]


# =============================================================================

nums = [1,2,2,3,3,3]
k=2
res={}
for x in nums:
    res[x]=res.get(x,0)+1
print(res)    

rev = sorted(res, key=res.get, reverse=True)
print(rev[:k])





