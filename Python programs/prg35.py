Lst=[100,50,65,82,95]
for i in range(len(Lst)):
    for j in range(len(Lst)-1-i):
        if abs(Lst[j]-50)>abs(Lst[j+1]-50):
            Lst[j],Lst[j+1]=Lst[j+1],Lst[j]
print("Final list is:",Lst)