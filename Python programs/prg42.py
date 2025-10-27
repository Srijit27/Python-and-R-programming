import numpy as np

#Creating a 1D, 2D and 3D array

a1=np.array([1, 2, 3, 4, 5, 6])
print("1D Array is:",a1)
print("Shape is:",a1.shape)
print("Dimension is:",a1.ndim)
print("Data Type is:",a1.dtype)
print("-" * 30)

a2=np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array is:\n",a2)
print("Shape is:",a2.shape)
print("Dimension is:",a2.ndim)
print("Data Type is:",a2.dtype)
print("-" * 40)

a3=np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])
print("3D Array is:",a3)
print("Shape is:",a3.shape)
print("Dimension is:",a3.ndim)
print("Data Type is:",a3.dtype) 
print("-" * 40)


# 1D to 2D conversion
n1 = a1.reshape(2,3)
print("Reshaped 1D to 2D Array is:",n1)
print("Shape:",n1.shape)
print("-" * 40)

# 2D to 3D conversion
n2 = a2.reshape(1, 2, 3)
print("Reshaped 2D to 3D Array is:",n2)
print("Shape:",n2.shape)
print("-" * 40)

# 2D to a mxn dimension (say 3x2)
n3=a2.reshape(3, 2)
print("Reshaped 2D (different shape) is:",n3)
print("Shape:",n3.shape)
print("-" * 40)
