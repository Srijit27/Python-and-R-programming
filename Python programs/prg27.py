Lst=[10,5,4,1,8,9,7,6,3,2]
rotate=[]
rotate.append(Lst[-1])
for i in range(len(Lst)-1):
    rotate.append(Lst[i])
print("Original list is:",Lst)
print("Rotated list is:",rotate)