lst = [55,77,24,96,78,99,108,10,20,50]

# s=sorted(lst)
# print(s)
first =0
second=0

for x in lst:
    if x>first:
        second=first
        first=x
    elif x > second and  x != first:
        second = x
print(second)  