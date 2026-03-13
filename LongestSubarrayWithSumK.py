# Input: arr = [10, 5, 2, 7, 1, -10], k = 15
# Output: 6
# Explanation: Subarrays with sum = 15 are [5, 2, 7, 1], [10, 5] and [10, 5, 2, 7, 1, -10]. 
# The length of the longest subarray with a sum of 15 is 6.




arr = [10, 5, 2, 7, 1, -10]
k = 15
max_len=0
for x in range(len(arr)):
    total=0
    for y in range(x,len(arr)):
        total += arr[y]
        if total == k:
            length = y-x + 1
            max_len=max(length,max_len)
print(max_len)













# max_len=0
# for x in range(len(arr)):
#     # print(x)
#     total = 0
#     for y in range(x,len(arr)):
#         print(y)
#         total += arr[y]
#         if total == k:
#             length = y-x+1
#             max_len= max(max_len,length)
            
# print(max_len)    


    




