upper, lower, num=0,0,0
print("enter * to exit")
while(str!='*'):
    str=input("enter the characters:")
    if(str=='*'):
        print("end of the program")
        break
    for i in range(len(str)):
        if(str[i]>='A' and str[i]<='Z'):
            upper+=1
        elif(str[i]>='a' and str[i]<='z'):
            lower+=1
        else:
            num+=1
print("Upper case letters: ",upper)
print("\nLower case letters: ",lower)
print("\nnumbers: ",num)
