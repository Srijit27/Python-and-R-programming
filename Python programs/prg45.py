import numpy as np

r=int(input("Enter number of rows:"))
c=int(input("Enter number of columns:"))

print(f"Enter {r*c} integer elements:")
ele=[]
for i in range(r*c):
    val=int(input(f"Element {i+1}:"))
    ele.append(val)

# Convert list into NumPy matrix
m=np.array(ele).reshape(r,c)
print("\nOriginal Matrix is:\n",m)

# Sort the elements row-wise 
n=np.sort(m,axis=1)
print("\nMatrix after sorting each row is:\n",n)

# Sort elements column-wise 
p=np.sort(n,axis=0)
print("\nMatrix after sorting each column is:\n",p)

# Perform statistical operations 
print("\nChoose a statistical operation:")
print("Options → min, max, range, percentile, mean, median, variance, std")

ch=input("Enter your choice:").strip().lower()

# Flatten matrix for global statistics
flat_p=p.flatten()

if(ch=='Min'):
    print("Minimum value:",np.min(flat_p))
elif(ch=='Max'):
    print("Maximum value:",np.max(flat_p))
elif(ch=='Range'):
    print("Range:",np.max(flat_p)-np.min(flat_p))
elif(ch=='Percentile'):
    print("70th Percentile:",np.percentile(flat_p,70))
elif(ch=='Mean'):
    print("Mean:",np.mean(flat_p))
elif(ch=='Median'):
    print("Median:",np.median(flat_p))
elif(ch=='Variance'):
    print("Variance:",np.var(flat_p))
elif(ch=='std'):
    print("Standard Deviation:",np.std(flat_p))
else:
    print("Invalid choice! Please enter one from the given options")