def fact(n):
    a=1
    for i in range(2,n+1):
        a*=i
    return a
l=[]
v=0
n=int(input("Enter the number of rows: "))
r=int(input("Enter the row number: "))
for i in range(n):
    for j in range(n-1-i):
        print(end=" ")
    for j in range(i+1):
        v=fact(i)//(fact(j)*fact(i-j))
        print(v,end=" ")
        if(i==r-1):
            l.append(v)
    print("\n")
print("sum of elements in the row: ",sum(l))
