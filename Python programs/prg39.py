import re
txt="Hello, I study BTech CSE at HITK, hence I am an Engineer"

r1=re.findall(r'[a-m]',txt)
print("Lower case letters between a-m are:",r1)

r2=re.findall(r'[n-z]',txt)
print("Remaining letters are:",r2)

r3=re.findall(r'\d',txt)
print("Numeric characters are:",r3)

r4=re.findall(r'He..o',txt)
print("Sequence starting with He followed by 2 characters & ending with an o",r4)

r5=re.findall(r'He.*o',txt)
print("Sequence starting with He followed by 1 character & ending with an o",r5)

r6=re.findall(r'He.+o',txt)
print("Sequence starting with He followed by 1 character & ending with an o",r6)

r7=re.findall(r'he..o',txt)
print("Sequence starting with he followed by 2 characters & ending with an o",r7)
