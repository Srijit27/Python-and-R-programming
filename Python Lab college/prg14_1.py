n=(int)(input("Enter the value of n:"))
x=0
y=1
print("Fibonacci series is:-")
print(x,end=' ')
print(y,end=' ')
for i in range(2,n):
    t=x+y
    print(t,end=' ')
    x=y
    y=t
