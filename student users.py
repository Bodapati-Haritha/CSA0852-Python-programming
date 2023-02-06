t=int(input("Total Users:"))
if(t<=0):
      print("INVALID INPUT")
s=int(input("Staff Usres:"))
n=s/3
if(s<t):
      print("Non-Teaching Staff Users:",n)
      S=t-s-n
      print("Student Users:",S)
else:
      print("INVALID INPUT")
