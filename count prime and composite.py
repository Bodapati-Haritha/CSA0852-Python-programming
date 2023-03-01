mylist = []
try:
    n = int(input("enter length of list:"))
    for a in range(1,n+1):
        e = int(input("enter an element :"))
        mylist.append(e)
    print(mylist)
    i = len(mylist)
    prime = []
    composite = []
    for i in range(0,i):
        c=0
        for j in range(2,mylist[i]):
            if(mylist[i]%j==0):
                c=1
                break
        if(c==0):
            prime.append(mylist[i])
        else :
            composite.append(mylist[i])
    
    X = len(prime)
    print ("Number of Prime Numbers:",X)
    Y = len(composite)
    print ("Number of Composite Numbers:",Y)
except ValueError:
    print("enter integer number")
