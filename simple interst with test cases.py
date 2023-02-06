p=int(input("enter the principal amount: "))
t=int(input("enter number of years: "))
s=input("is the customer senior citizen: ")
y="yes"
n="no"
if(s==y):
    simple_interst=(p*t*12)/100
    print("simple interst=",simple_interst)
elif(s==n):
    simple_interst=(p*t*10)/100
    print("simple interst=",simple_interst)
else:
    print("INVALID INPUT")
