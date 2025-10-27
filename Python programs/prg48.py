import numpy as np

a1=np.array([10, 20, 30, 40, 50])
a2=np.array([15, 20, 25, 40, 55])

print("Array 1 is:",a1)
print("Array 2 is:",a2)

print("Equality result:",np.equal(a1,a2))
print("Non-Equality result:",np.not_equal(a1,a2))
print("Greater than Equal result:",np.greater_equal(a1,a2))
print("Greater than result:",np.greater(a1,a2))
print("Less than result:",np.less(a1,a2))