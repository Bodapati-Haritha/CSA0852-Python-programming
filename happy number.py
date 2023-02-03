def isHappyNumber(num):
    rem=sum=0
    while(num>0):
        rem=num%10
        sum+=(rem*rem)
        num//=10
    return sum
num=int(input("enter number:"))
result=num
while(result!=1 and result!=4):
    result=isHappyNumber(result)
if(result==1):
    print(str(num) + " is True")
elif(result==4):
    print(str(num) + " is False")
