arr = [1,0,2,0,3,0]
k=0
for x in range(len(arr)):
    if arr[x] != 0:
        arr[k],arr[x]=arr[x],arr[k]
        k+=1
print(arr)        











