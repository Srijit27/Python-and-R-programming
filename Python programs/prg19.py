city_name=input("Enter the source file name:")
dest_name=input("Enter the destination file name:")
try:
    r1=open(city_name,'r')
    r2=open(dest_name,'w')
    for line in r1.readlines():
        r2.write(line)
    r1.close()
    r2.close()
    print("Write operation successful")
except FileNotFoundError:
    print("The file is not present..!!")