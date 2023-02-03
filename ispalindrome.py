def ispalindrome(s):
    rev=''.join(reversed(s))
    if(s==rev):
        return True
    return False
s=input("enter the string:")
ans=ispalindrome(s)
if(ans):
    print("True")
else:
    print("False")
