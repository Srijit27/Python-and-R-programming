Lst=[4,3,5,10,9,17,18]
def is_prime(n):
    if(n<=1):
        return False
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return False
    return True
for x in Lst:
    if is_prime(x):
        print("First Prime is:",x)
        break