def add(a,b):
    return a+b
def add_decorator(a,b):
    if(a<0):
        a=0
    if(b<0):
        b=0
    return a+b
print("Without decorator:",add(-50,60))
print("With decorator:",add_decorator(-50,60))