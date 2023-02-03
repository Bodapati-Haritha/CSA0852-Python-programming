n=int(input("enter the number of elements: "))
l=[]
for i in range(n):
    a=int(input("enter the element: "))
    l.append(a)
def sumsquare(l):
    b=0
    c=0
    square=[]
    for j in l:
        if(j%2==0):
            b=b+(j*j)
        else:
            c=c+(j*j)
    square.append(c)
    square.append(b)
    print(square)
sumsquare(l)
