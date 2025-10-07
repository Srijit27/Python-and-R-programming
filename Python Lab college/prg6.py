a=(int)(input("Enter 1st number:"))
b=(int)(input("Enter 2nd number:"))
c=(int)(input("Enter 3rd number:"))
if(a>b):
    if(a>c):
        max=a
    else:
        max=c
else:
    if(b>c):
        max=b
    else:
        max=c
if(a<b):
    if(a<c):
        min=a
    else:
        min=c
else:
    if(b<c):
        min=b
    else:
        min=c   
print("Maximum is:",max)
print("Minimum is:",min)
print("Average is:",(a+b+c)/3)