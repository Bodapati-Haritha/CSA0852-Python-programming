a=int(input("enter the number of fresh loaves purchased:"))
b=int(input("enter the number of old loaves purchased:"))
price=185
fresh=a*price
old=b*0.6*price
total=fresh+old
if(a<0):
    print("invalid input")
elif(b<0):
    print("invlid input")
else:
    print("regular price",price)
    print("amount of fresh loaves",fresh)
    print("amount of old loaves",old)
    print("total",total)
    
    
