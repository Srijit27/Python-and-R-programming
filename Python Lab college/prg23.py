class Library:
    nob=0 #no of books
    nou=0 #no of users
    totp=0 #total price
    def __init__(self,b_name=None,b_price=0,u_name=None):
        self.b_name=None
        self.b_price=0
        self.u_name=None

        if b_name is not None and b_name.lower()!="null":
            self.b_name=b_name
            self.b_price=b_price
            Library.nob+=1
            Library.totp+=b_price

        if u_name is not None and u_name.lower()!="null":
            self.u_name=u_name
            Library.nou+=1
    
    def book_display(self):
        if self.b_name:
            print("Book name is:",self.b_name,"\n")
            print("Book price is:",self.b_price,"\n")
        else:
            print("No details is available for an instance\n")
    def user_display(self):
        if self.u_name:
            print("User name is:",self.u_name,"\n")
        else:
            print("No details is available for an instance\n")

books=[]
users=[]
no_of_books=(int)(input("Enter the no of books:"))
for i in range(no_of_books):
    bname=input(f"Enter the name of book {i+1}:")
    bprice=(eval)(input(f"Enter the price of book {i+1}:"))
    books.append(Library(b_name=bname,b_price=bprice))
no_of_users=(int)(input("Enter the no of users:"))
for i in range(no_of_users):
    uname=input(f"Enter the name of user {i+1}:")
    users.append(Library(u_name=uname))
print("Book details:-\n")
for b in books:
    b.book_display()
for u in users:
    u.user_display()
print("Library Summary:-\n")
print("Total no of books:",Library.nob)
print("Total no of users:",Library.nou)
print("Total price of books:",Library.totp)