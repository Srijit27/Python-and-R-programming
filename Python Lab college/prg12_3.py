l=[]
def gcd(x,y):
    if(y==0):
        return x
    else:
        return gcd(y,x%y)
n=(int)(input("Enter the value of n:"))
for i in range(n):
    num=(int)(input("Enter the value:"))
    l.append(num)
result=l[0]
for i in range(1,n):
    result=gcd(result,l[i])
print("GCD value is:",result)