import numpy as np

while True:
    # Create a 2x3 array of random numbers
    rand_arr=np.random.rand(2,3)
    print("Random Array is:\n",rand_arr)
    
    # Create another 2x3 array of all 1's
    one_arr=np.ones((2,3))
    print("\nArray of ones is:\n",one_arr)
    
    # Generate a boolean array of values>0.5
    bool_arr=rand_arr>0.5
    print("\nBoolean Array is:\n",bool_arr)
    print("Shape is:",bool_arr.shape)
    
    # Boolean index one_arr using bool_arr
    new_arr=one_arr[bool_arr]
    print("\nNew Array after boolean indexing is:\n",new_arr)
    print("Shape is:",new_arr.shape)

    ch=input("Press 'Y' to continue else terminate the process:").strip().lower()
    if(ch!='Y' and ch!='y'):
        break
    print("-"*40)