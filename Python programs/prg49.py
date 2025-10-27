import numpy as np

print("Enter elements for Matrix A (3x3):")
A=[]
for i in range(3):
    r=list(map(int,input(f"Enter 3 elements for row {i+1} of Matrix A (space separated):").split()))
    A.append(r)
A=np.array(A)

print("Enter elements for Matrix B (3x3):")
B=[]
for i in range(3):
    r=list(map(int,input(f"Enter 3 integers for row {i+1} of Matrix B (space separated):").split()))
    B.append(r)
B=np.array(B)

print("Matrix A is:\n", A)
print("Matrix B is:\n", B)

print("Addition result is:-\n",np.add(A, B))
print("Subtraction result is:-\n",np.subtract(A, B))
print("Element-wise Multiplication result is:-\n",np.multiply(A, B))
print("Element-wise Division result is:-\n",np.divide(A, B))
print("Matrix Multiplication result is:-\n",np.dot(A, B))
print("Transpose of Matrix A is:-\n",A.T)
print("Transpose of Matrix B is:-\n",B.T)
