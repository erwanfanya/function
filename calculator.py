def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

operator = input("enter one of the operator (+,-,*,/):")

num1 = int(input("enter number 1:"))
num2 = int(input("enter number 2:"))


if operator == "+":
    print("sum :", (num1+num2))
elif operator == "-":
    print("difference", (num1-num2))
elif operator == "*":
    print("product", (num1,num2))
elif operator == "/":
    print("quotion", (num1/num2))
else:
    print("invalid operator")
