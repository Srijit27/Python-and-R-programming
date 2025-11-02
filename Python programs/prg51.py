class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

class Publication:
    def __init__(self,no_rp,no_book,no_art):
        self.no_rp=no_rp
        self.no_book=no_book
        self.no_art=no_art

class Faculty(Person,Publication):
    def __init__(self,name,age,gender,no_rp,no_book,no_art,desig,dept):
        Person.__init__(self,name,age,gender)
        Publication.__init__(self,no_rp,no_book,no_art)
        self.desig=desig
        self.dept=dept
    
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)
        print("No of research published:",self.no_rp)
        print("No of books published:",self.no_book)
        print("No of articles published:",self.no_art)
        print('*'*30)
    
f1=Faculty('SM',54,'M',44,56,62,"HOD","CSE")
f2=Faculty('DB',65,'M',49,65,82,"Professor","CSE")
f1.display()
f2.display()