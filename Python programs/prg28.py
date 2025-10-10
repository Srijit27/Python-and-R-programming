def mean_func(lst):
    s=0
    l=len(lst)
    if l!=0:
        for i in lst:
            s+=i
        return s/l
    return None

def median_func(lst):
    l=len(lst)
    if l!=0:
        if(l%2==0):
            return (lst[1//2-1]+lst[1//2])/2
        return lst[1//2]
    return None

def mode_func(lst):
    l=len(lst)
    if l!=0:
        mod=lst[0]
        max=lst.count(mod)
        for i in lst:
            f=lst.count(i)
            if(f>max):
                max=f
                mod=i
            return mod
        return None
    
Lst=[10,5,4,1,8,9,7,6,3,2]
sort=sorted(Lst)
print("Original list is:",Lst)
print("Mean of list is:",mean_func(Lst))
print("Meadian of list is:",median_func(Lst))
print("Mode of list is:",mode_func(Lst))