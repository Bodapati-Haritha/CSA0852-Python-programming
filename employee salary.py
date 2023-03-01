a=input("Enter the Grade of Employee:")
b=int(input("Enter the Employee Salary:"))
Grade_A='A'
Grade_B='B'
if(b<=0):
    print("INVALID INPUT")
else:
    if(a==Grade_A):
        if(b<10000):
            print("Salary:",b)
            c=0.7*b
            print("Bonus:",c)
        else:
            print("Salary:",b)
            c=0.5*b
            print("Bonus:",c)
        print("Total to be Paid:",b+c)
    elif(a==Grade_B):
        if(b<10000):
            print("Salary:",b)
            c=0.12*b
            print("Bonus:",c)
        else:
            print("Salary:",b)
            c=0.10*b
            print("Bonus:",c)
        print("Total to be Paid:",b+c)
