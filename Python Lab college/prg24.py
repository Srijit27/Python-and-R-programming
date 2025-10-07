class Student:
    c_name=None
    s_count=0
    def __init__(self,stid,sname,smarks):
        self.stid=stid
        self.sname=sname
        self.smarks=smarks
        tot=0
        c=0
        for m in smarks:
            tot=tot+m
            c+=1
        self.avg=tot/3
        Student.s_count+=1
        self.g=self.grade()

    def grade(self):
        a=self.avg
        if a>=90:
            return 'O'
        elif a>=80:
            return 'A'
        elif a>=70:
            return 'B'
        elif a>=60:
            return 'C'
        elif a>=50:
            return 'D'
        else:
            return 'F'
    
    def display(self):
        print("Student ID:",self.stid)
        print("Student name:",self.sname)
        print("Total marks:",self.smarks)
        print("Average is:",self.avg)
        print("Grade is:",self.g)

Student.c_name=input("Enter the college name:")
n=int(input("Enter number of students:"))
students=[]
for i in range(n):
    stid=input(f"\nEnter student ID for student {i+1}:")
    sname=input(f"Enter name for student {i+1}:")
    marks=[]
    for j in range(3):
        mark=(int)(input(f"Enter mark {j+1}:"))
        marks.append(mark)
    students.append(Student(stid,sname,marks))

print("COLLEGE INFORMATION:-")
print("College Name:",Student.c_name)
print("Total Students:",Student.s_count)
print("STUDENT DETAILS:-")
for s in students:
    s.display()