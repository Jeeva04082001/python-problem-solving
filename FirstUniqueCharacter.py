# s = "neetcodeneet"
# uniq=""
# seen=set()
# for x in range(len(s)):
#     if x not in seen:
#         print(x)
#         break
    






s = "baab"
freq={}

for x in s:
    freq[x] = freq.get(x,0)+1

for i in range(len(s)):
    if freq[s[i]] == 1:
        print(i)
        break
else:
    print(-1)




