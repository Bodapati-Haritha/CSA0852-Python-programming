l=[]
m=[]
for i in range(3):
    print("enter the sentence:")
    l.append(input())
    m.append(len(l[i].split()))
print(max(m))
