n=int(input("enter the no.of elements:"))
arr=[]
sum=0
for i in range(0,n):
    a=float(input("enter the elements:"))
    arr.append(a)
print(arr)
for i in range(0,n):
    for j in range(i+1,n):
        if(arr[i]>arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
for i in range(0,n):
    print(arr[i])
for i in range(0,n):
    sum=sum+arr[i]
    mean=sum/n
print("mean=",mean)
if(n%2==0):
    median1=arr[n//2]
    median2=arr[n//2-1]
    median=(median1+median2)/2
else:
    median=arr[n//2]
print("median=",str(median))
from collections import Counter
num=Counter(arr)
findMode=dict(num)
mode=[i for i,v in findMode.items() if v==max(list(num.values()))]
if(len(mode)==n):
    findMode="the group of numbers do not have any mode"
else:
    findMode="the mode of a number is:"+', '.join(map(str,mode))
print(findMode)
