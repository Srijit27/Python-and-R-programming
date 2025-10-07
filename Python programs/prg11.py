a=(eval)(input("Enter 1st number:"))
b=(eval)(input("Enter 2nd number:"))
ch=input("Enter the operation sign:")
if(ch=='+'):
    print("Sum is:",a+b)
elif(ch=='-'):
    print("Difference is:",a-b)
elif(ch=='*'):
    print("Product is:",a*b)
elif(ch=='/'):
    print("Quotient is:",a/b)
elif(ch=='%'):
    print("Remainder is:",a%b)
else:
    print("Enter correct symbol")
