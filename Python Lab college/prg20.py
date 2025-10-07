try:
    a,b=(eval)(input("Enter two numbers separated by commas:"))
    r=a/b
    print("Division result is:",r)
except ZeroDivisionError:
    print("Division by zero attempted..!!")
except SyntaxError:
    print("Please make the input space separated by commas")