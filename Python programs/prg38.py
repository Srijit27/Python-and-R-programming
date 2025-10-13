import re
def count_sub(file):
    patt1=re.compile(r'\Adef')
    patt2=re.compile(r'\Afor')
    c=0
    with open(file,'r') as f:
        for line in f:
            if patt1.search(line) or patt2.search(line):
                c=c+1
    return c
f_name="Python programs/prg37.py"
print("No of lines containing def/for is:",count_sub(f_name))