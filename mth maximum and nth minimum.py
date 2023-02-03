n=int(input("enter the number: "))
l=[]
for i in range(n):
    l.append(int(input("enter the elements: ")))
a=int(input("enter the value of m: "))
b=int(input("enter the value of n: "))
l=sorted(l)
print("mth maximum=",l[-a])
print("nth minimum=",l[b-1])
print("sum=",l[b-1]+l[-a],"sub=",l[-a]-(l[b-1]))



