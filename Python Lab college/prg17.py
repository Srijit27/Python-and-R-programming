import math
def triangle_valid(a=8,b=9,c=3):
    if(a+b>c or b+c>a or a+c>b):
        print("Triangle is valid")
        triangle_type(a,b,c)
    else:
        print("Triangle is invalid")
def triangle_type(a=8,b=9,c=3):
    if(a==b and b==c and a==c):
        print("Equilateral triangle")
        triangle_area(a,b,c)
    elif(a==b or b==c or a==c):
        print("Isosceles triangle")
        triangle_area(a,b,c)
    else:
        print("Scalene triangle")
        triangle_area(a,b,c)
def triangle_area(a=8,b=9,c=3):
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Area is:",round(area,2))
def triangle():
    triangle_valid(8,9,3)
triangle()