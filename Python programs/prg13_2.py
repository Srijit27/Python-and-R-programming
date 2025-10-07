n=(int)(input("Enter the no:"))
def fact(x):
    if(x==1):
        return 1
    else:
        return x*fact(x-1)
print("Factorial is:",fact(n))