class Employee:
    noe=0 #counter for number of employees
    def __init__(self,name,desig,sal):
        self.name=name
        self.desig=desig
        self.sal=sal

        Employee.noe+=1

    def display(self):
        print("Employee name:",self.name)
        print("Employee designation:",self.desig)
        print("Employee salary:",self.sal)
    
e1=Employee("Srijit","HR",2500)
e2=Employee("Aryan","CEO",4000)
e3=Employee("Mohak","SDE",3800)

e1.display()
e2.display()
e3.display()

print("Total no of employees:",Employee.noe)
print("\n")