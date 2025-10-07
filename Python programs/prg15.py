import sys
if(len(sys.argv)==2):
    n=(int)(sys.argv[1])
    s=0
    while(n!=0):
        r=n%10
        s=s+r
        n=n//10
    print("Sum of digits:",s)
else:
    print("Invalid no of arguments")    