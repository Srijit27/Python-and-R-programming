a=(int)(input("Enter 1st no:"))
b=(int)(input("Enter 2nd no:"))
def gcd(x,y):
    if(y==0):
        return x
    else:
        return gcd(y,x%y)
print("GCD value is:",gcd(a,b))