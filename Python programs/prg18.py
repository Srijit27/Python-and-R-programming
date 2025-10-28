import os
cl=0
cc=0
file_path = os.path.join(os.path.dirname(__file__), "sample.txt")
with open(file_path,'r') as f1:
    for line in f1.readlines():
        cl+=1
with open(file_path,'r') as f2:
    for line in f2.read():
        cc+=1
print("No of lines:",cl)
print("No of characters:",cc)
