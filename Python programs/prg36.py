s=(int)(input("Enter the size:"))
l=[int(input(f"Enter the element {i+1}:")) for i in range(s)]
no=(int)(input("Enter a value you want to search for:"))
ind=[i for i,val in enumerate(l) if val==no]
ind=list(map(lambda i:i+1,ind))
if(len(ind)>1):
    print(f"{no} occurs multiple times at indices",ind)
else:
    print(f"{no} doesn't occur multiple times")