import math
def check_range(x):
    if(x<1 or x>255):
        print("Out of range")
        return 0
    return 1
def check_bits(x):
    if(check_range(x)):
        n=math.log(x,2)
        a=(int)(n)
        if(a!=n):
            a+=1
        print("No of bits:",a)
while True:
    try:
        n=(int)(input("Enter the no of registers:"))
        r=(int)(n)
    except ValueError:
        print("Enter an integer again")
    else:
        break
check_bits(r)