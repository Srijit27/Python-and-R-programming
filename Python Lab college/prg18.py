cl=0
cc=0
with open("sample.txt",'r') as f1:
    for line in f1.readlines():
        cl+=1
f1.close()
with open("sample.txt",'r') as f2:
    for line in f2.read():
        cc+=1
f2.close()
print("No of lines:",cl)
print("No of characters:",cc)