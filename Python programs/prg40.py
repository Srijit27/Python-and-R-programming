import re
sent="""This is my 8th lab day in Python
I am going to perform Regex today
I am very excited about it"""

with open('source.txt','w') as file:
    file.write(sent)
patt=re.compile(r'^This')
with open('source.txt','r') as infile, open('desti.txt','w') as outfile:
    for line in infile:
        if patt.match(line):
            modify=re.sub(r'^This','That',line)
            outfile.write(modify)

print("The modification is done")
