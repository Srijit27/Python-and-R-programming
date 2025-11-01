def decorator(func):
    def wrapper(a,b):
        if(a<0):
            a=0
        elif(b<0):
            b=0
        return func(a,b)
    return wrapper
@decorator #add=decorator(add)
def add(a,b):
    return a+b
print("Without decorator:",(lambda x,y:x+y)(-50,60))
print("With decorator:",add(-50,60))