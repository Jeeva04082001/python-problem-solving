s = "abaGADAGdata"

res=[]
n=len(s)

for x in range(n):
    for y in range(x+3, n+1):
        sub=s[x:y]
        if sub == sub[::-1]:
            res.append(sub)
print(res)         






