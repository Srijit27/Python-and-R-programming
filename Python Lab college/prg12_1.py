a=(int)(input("Enter 1st no:"))
b=(int)(input("Enter 2nd no:"))
def gcd(x,y):
    while(y!=0):
        t=y
        y=x%y
        x=t
    return x
print("GCD value is:",gcd(a,b))