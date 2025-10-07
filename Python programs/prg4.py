import sys
if(len(sys.argv)==4):
    a=(int)(sys.argv[1])
    b=(int)(sys.argv[2])
    ch=sys.argv[3]
    string="AEIOU"
    print("Relational operators:-")
    print("a<b:",a<b)
    print("a<=b:",a<=b)
    print("a>b:",a>b)
    print("a>=b:",a>=b)
    print("a==b:",a==b)
    print("a!=b:",a!=b)
    print("Identity operators:-")
    print("Address of a is:",id(a))
    print("Address of b is:",id(b))
    print("a is b:",a is b)
    print("a is not b:",a is not b)
    print("Membership operators:-")
    print("ch in string:",ch in string)
    print("ch not in string:",ch not in string)
else:
    print("Invalid number of arguments")
    