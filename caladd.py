#build scientific calculator

import math

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def asin(x):
    return math.asin(x)

def acos(x):
    return math.acos(x)

def atan(x):
    return math.atan(x)

def sqrt(x):
    return math.sqrt(x)

def log(x):
    return math.log(x)

def exp(x):
    return math.exp(x)

def pow(x, y):
    return math.pow(x, y)

def fact(x):
    return math.factorial(x)

def mod(x, y):
    return x % y

def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Sin")
    print("6. Cos")
    print("7. Tan")
    print("8. Asin")
    print("9. Acos")
    print("10. Atan")
    print("11. Square root")
    print("12. Log")
    print("13. Exponential")
    print("14. Power")
    print("15. Factorial")
    print("16. Modulus")

    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16): ")

    num1 = float(input("Enter first number: "))
    if choice != 5 and choice != 6 and choice != 7 and choice != 8 and choice != 9 and choice != 10 and choice != 11 and choice != 15:
        num2 = float(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", sub(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", mul(num1, num2))

    elif choice == '4':
        print(num1, "/", num2, "=", div(num1, num2))

    elif choice == '5':
        print("sin(", num1, ") = ", sin(num1))

    elif choice == '6':
        print("cos(", num1, ") = ", cos(num1))

    elif choice == '7':
        print("tan(", num1, ") = ", tan(num1))

    elif choice == '8':
        print("asin(", num1, ") = ", asin(num1))

    elif choice == '9':
        print("acos(", num1, ") = ", acos(num1))

    elif choice == '10':
        print("atan(", num1, ") = ", atan(num1))

    elif choice == '11':
        print("sqrt(", num1, ") = ", sqrt(num1))

    elif choice == '12':
        print("log(", num1, ") = ", log(num1))