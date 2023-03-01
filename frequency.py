n=int(input("enter number of elements="))
arr=[]
for i in range(0,n):
    a=input("enter the elements=")
    arr.append(a)
print(arr)
fr=[None]*len(arr);
visited=-1;
for i in range(0,len(arr)):
    count=1;
    for j in range(i+1,len(arr)):
        if(arr[i]==arr[j]):
            count=count+1;
            fr[j]=visited;
        if(fr[i]!=visited):
            fr[i]=count;
print("_________");
print("Element|Frequency");
print("_________");
for i in range(0,len(fr)):
    if(fr[i]!=visited):
        print(" "+str(arr[i])+"  |  "+str(fr[i]));
print("________")
