import math
x1=(int)(input("Enter x co-ordinate of 1st point:"))
y1=(int)(input("Enter y co-ordinate of 1st point:"))
x2=(int)(input("Enter x co-ordinate of 2nd point:"))
y2=(int)(input("Enter y co-ordinate of 2nd point:"))
dist=math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
print("Distance is:",round(dist,2),"units")