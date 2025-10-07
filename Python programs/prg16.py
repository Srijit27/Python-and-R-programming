def max_min(*args):
    if not args:
        print("List is empty, enter a value again")
        return
    min=args[0]  
    max=args[0]
    for x in args[1:]:
        if x<min:
            min=x
        if x>max:
            max=x
    print("Maximum is:",max," & Minimum is:",min)
print("Enter the numbers:-")
num=list(map(int, input().split())) #take multiple inputs, each are space-separated, type-casted into int, stored in a list
max_min(*num)
