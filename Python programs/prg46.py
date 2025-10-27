import numpy as np

r=int(input("Enter number of rows:"))
c=int(input("Enter number of columns:"))

print(f"Enter {r*c} integer elements:")
ele=[]
for i in range(r*c):
    val=int(input(f"Element {i+1}:"))
    ele.append(val)

m=np.array(ele).reshape(r,c)
print("Original Matrix is:\n",m)

cm=np.mean(m, axis=0)
print("\nColumn Mean value is:\n",cm)
print("Shape of cm is:",cm.shape)

demeancol=m-cm
print("\nDemeaned Columns is:\n", demeancol)

print("\n--- Broadcasting Explanation ---")
print("Matrix m shape:",m.shape)
print("Column mean cm shape:",cm.shape)
print("\nAccording to NumPy broadcasting rules:")
print("Shapes are compared element-wise from the trailing dimensions.")
print("The column mean array (cm) with shape (cols,) is 'stretched' across all rows.")
print("Hence, for every column j, cm[j] is subtracted from each row element in that column.")
print("\nMathematically:demeancol[i][j]=m[i][j]-cm[j]")
