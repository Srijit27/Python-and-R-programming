import random
from functools import reduce
Lst=[random.randint(1,10) for _ in range(20)]
print("Random list is:",Lst)
d=filter(lambda x:x%3==0 and x%5==0,Lst)
d_list=list(d)
print("Numbers divisible by 3 and 5 are:",d_list)
sq=map(lambda x:x**2,Lst)
sq_list=list(sq)
print("Squared list is:",sq_list)
cb=map(lambda x:x**3,Lst)
cb_list=list(cb)
print("Cubed list is:",cb_list)
Lst=[]
for i in range(0,5):
    n=(int)(input("Enter a number:"))
    Lst.append(n)
p=reduce(lambda x,y:x*y,Lst)
print("Product is:",p)