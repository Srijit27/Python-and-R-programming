def prime_generate(n):
    c,x=0,2
    while(c<n):
        for i in range(2,int(x**0.5)+1):
            if(x%i==0):
                break
        else:
            yield x
            c+=1
        x+=1
print("The prime numbers are:-")
for p in prime_generate(10):
    print(p,end=" ")