import re
def check(pword):
    error=[]
    if(len(pword)<0):
        error.append("The password has less than 8 characters")
    if not re.search(r'[a-z]',pword):
        error.append("The password should contain at least one lower case letters")
    if not re.search(r'[A-Z]',pword):
        error.append("The password should contain at least one upper case letters")
    if not re.search(r'\d',pword):
        error.append("The password should contain at least one numeric character")
    if not re.search(r'[^\w]',pword):
        error.append("The password should contain at least one special character")
    return error
password=input("Enter a password:")
errors=check(password)
if not errors:
    print("Password is valid")
else:
    print("Password is invalid for the given causes:")
    for error in errors:
        print('*'+error)