class TooHot(Exception):
    def display(self):
        print("Temperature is too Hot")
class TooCold(Exception):
    def display(self):
        print("Temperature is too Cold")
try:
    temp=(eval)(input("Enter the temperature:"))
    if(temp>40):
        raise TooHot(temp)
    elif(temp<20):
        raise TooCold(temp)
    else:
        print("Temperature is Normal")
except TooHot as t1:
    t1.display()
except TooCold as t2:
    t2.display()