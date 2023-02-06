try:
    y=int(input("Enter the Year:"))
    if(y>0):
        if(y%100==0):
            print("The Given Value is Not a Leap Year")
        elif(y%400==0):
            print("The Given Year is a Leap Year")
        elif(y%4==0):
            print("The Given Year is a Leap Year")
        else:
            print("Not a Leap Year")
            for i in range(y-4,y):
                if(i%4==0):
                    print("Leap Year=",i)
    else:
        print("ENTER A VALID INPUT")
except ValueError:
    print("INVALID INPUT")
