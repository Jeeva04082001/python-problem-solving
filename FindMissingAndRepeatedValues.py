# You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, (n^2)]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.

# Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

# Example 1:

# Input: grid = [[1,3],[2,2]]

# Output: [2,4]



# grid = [[1,3],[2,2]]
# lst=[]
# seen=set()
# rep,mis=0,0
# for x in grid:
#     for y in x:
#         lst.append(y)
# for i in range(1,len(lst)+1):
#     if i not in lst:
#         mis=i

# for j in lst:
#     if j in seen:
#         rep=j
#     seen.add(j)
# print([rep,mis])



# grid = [[1,3],[2,2]]
# lst=[]
# seen=set()
# repeat,missing = 0,0

# for row in grid:
#     for num in row:
#         if num in seen:
#             repeat = num
#         seen.add(num)    
#         lst.append(num)

# for i in range(1,len(lst)+1):
#     if i not in seen:
#         missing = i
# print([repeat,missing])        

# ======================================================================================


# class Solution:
#     def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

#         seen= set()
#         lst=[]
#         repeat,missing=0,0
#         for row in grid:
#             for num in row:
#                 if num in seen:
#                     repeat=num
#                 seen.add(num) 
#                 lst.append(num)   
        
#         for i in range(1,len(lst)+1):
#             if i not in seen:
#                 missing = i

#         return [repeat,missing]  





