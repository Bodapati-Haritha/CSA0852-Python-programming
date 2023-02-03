pos_num=0
no_pos_num=0
neg_num=0
no_neg_num=0
arr=[]
tot=0
print("ENTER -1 TO EXIT")
while(arr!=-1):
    arr=int(input("ENTER THE ELEMENTS- "))
    if(arr==-1):
        print("end of program")
        break
    if(arr==0):
        print("NEITHER POSITIVE NOR NEGATIVE")
    elif(arr>0):
        pos_num=pos_num+arr
        no_pos_num+=1
        avg=pos_num/no_pos_num
    else:
        neg_num=neg_num+arr
        no_neg_num+=1
        avgn=neg_num/no_neg_num
print("AVERAGE OF POISTIVE OF NUMBERS- ",avg)
print("AVERAGE OF NEGATIVE NUMBERS- ",avgn)
