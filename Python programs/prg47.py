import numpy as np
arr=np.array(['Python','NumPy','Array','Example'])
print("Original Array:\n",arr)
new_arr=np.char.join(' ',arr)
print("\nArray after inserting spaces between characters:\n",new_arr)
