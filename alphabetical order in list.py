my_str = input("Enter a string:")
o=input("Order(A/D):")
asc_order='A'
des_order='D'
words = my_str.split()
if(o==asc_order):
    words.sort()
    for i in words:
        print(i)
elif(o==des_order):
    words.sort(reverse=True)
    for i in words:
        print(i)
