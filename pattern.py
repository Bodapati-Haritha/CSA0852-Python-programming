n=int(input("rows="))
for i in range(0,n+1):
    print(end="")
    k=0.1
    for j in range(0,i):
        print("{:.1f}".format(k),end=" ")
        k=k+0.1
    print("\r")
