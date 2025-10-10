import random

def unique(lst):
    result=[]
    for item in lst:
        if(lst.count(item)==1):
            result.append(item)
    return result

def duplicate(lst):
    result={}
    for item in lst:
        if(lst.count(item)>1):
            result[item]=lst.count(item)
    return result

def create_unique(lst):
    result=[]
    for item in lst:
        if item not in result:
            result.append(item)
    return result

print("The execution is as follows:-\n")
Lst=[random.randint(1,10) for _ in range(20)]
print("Original List is:",Lst)
print("Unique list is:",unique(Lst))
print("Duplicate list is:",duplicate(Lst))
print("Created unique list is:",create_unique(Lst))