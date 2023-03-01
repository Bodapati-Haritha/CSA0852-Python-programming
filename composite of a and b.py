a=int(input("Enter the Value of a:"))
b=int(input("Enter the Value of b:"))
for i in range(a+1,b+1):
    comp=0
    for j in range(1,b+1):
        if(i%j==0):
            comp=comp+1
    if(comp>2):
        print(i,end=" ")
