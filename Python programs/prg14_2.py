n=(int)(input("Enter the value of n:"))
def fibo(x):
    if(x<=1):
        return x
    return fibo(x-1)+fibo(x-2)
print("Fibonacci series is:-")
for i in range(0,n):
    print(fibo(i),end=' ')
    