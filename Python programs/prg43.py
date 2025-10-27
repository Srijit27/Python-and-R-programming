import numpy as np
import pandas as pd

# 1-D array of zeros 
zero=np.zeros(10)
print("1-D array of zeros:")
print(zero)
print("Shape:",zero.shape, "| Dimension:",zero.ndim, "| Data type:",zero.dtype)
print("-"*30)

# 2-D array of ones 
one=np.ones((2, 5),dtype=int)
print("2-D array of ones:")
print(one)
print("Shape:",one.shape, "| Dimension:",one.ndim, "| Data type:",one.dtype)
print("-"*30)

# 2-D array using arange(), total elements=3 rows×5 cols=15
myarray2=np.arange(4,4+4*15,4,dtype=float).reshape(3,5)
print("2-D array called myarray2 (using arange):")
print(myarray2)
print("Shape:",myarray2.shape, "| Dimension:",myarray2.ndim, "| Data type:",myarray2.dtype)
print("-"*30)

#Series object using np.tile() to create a base array and tile it multiple times
b_arr=np.array([1, 2, 3])
t_arr=np.tile(b_arr,4)  # repeats the array 4 times
series_obj=pd.Series(t_arr)

print("Series object created using np.tile() is:")
print(series_obj)
print("Data type of Series elements:",series_obj.dtype)
print("-"*30)
