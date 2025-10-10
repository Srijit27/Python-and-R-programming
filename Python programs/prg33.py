s1=set(map(int,input("Enter the elements of set 1:").split()))
s2=set(map(int,input("Enter the elements of set 2:").split()))
print("Press 1 for Union")
print("Press 2 for Intersection")
print("Press 3 for Difference")
print("Press 4 for Symmetric difference")
print("Press 0 to exit")
while(True):
    ch=(int)(input("Enter your choice:"))
    match ch:
        case 1:
              print("Union is:",s1|s2)
        case 2:
              print("Intersection is:",s1&s2)
        case 3:
              print("Difference is:",s1-s2)
        case 4:
              print("Symmetric difference is:",s1^s2)
        case 0:
            print("Loop exited")
            break
        case _:print("Invalid choice")
