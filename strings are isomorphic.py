def isIsomorphic(str1,str2):
    if(len(str1)!=len(str2)):
        return False
    x=[str1.count(char1) for char1 in str1]
    y=[str2.count(char1) for char1 in str2]
    return x==y
string1=input("Enter the string:")
string2=input("Enter the string:")
print(isIsomorphic(string1,string2))
    
