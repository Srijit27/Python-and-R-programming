from math import *
a=(eval)(input("Enter the co-efficient of x^2:"))
b=(eval)(input("Enter the co-efficient of x:"))
c=(eval)(input("Enter the constant:"))
det=b*b-4*a*c
if(det==0):
    print("Roots are real and equal")
    print("Root 1:",(-b/2*a)," Root 2:",(-b/2*a))
elif(det>0):
    print("Roots are real and distinct")
    print("Root 1:",((-b+sqrt(det))/2*a))
    print("Root 2:",((-b-sqrt(det))/2*a))
else:
    print("Roots are complex conjugate of each other")
    det=det*(-1)
    print("Root 1:",(-b/2*a),"+",((sqrt(det)/(2*a)),"i"))
    print("Root 2:",(-b/2*a),"-",((sqrt(det)/(2*a)),"i"))