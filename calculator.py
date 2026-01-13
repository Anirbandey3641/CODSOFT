import math
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
def power(a, b):
    return math.pow(a, b)
def sqrt(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number.")
    return math.sqrt(a)
def factorial(n):
    if n < 0:
        raise ValueError("Cannot take factorial of negative number.")
    return math.factorial(n)
def logarithm(a, base=10):
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive values.")
    return math.log(a, base)
def main():
    print("welcome to the calculator")
    r=0.0
    print("enter a number:")
    n1 = float(input())
    print("enter action (+, -, *, /, ^, sqrt, log):")
    ac=input()
    if ac != 'sqrt' and ac != 'log':
        print("enter another number:")
    n2 = float(input())
    if ac == '+':
        r= add(n1,n2)
    elif ac == '-':
        r=subtract(n1,n2)
    elif ac == '*':
        r=multiply(n1,n2)
    elif ac == '/':
        r=divide(n1,n2)
    elif ac == '^':
        r=power(n1,n2)
    elif ac == 'sqrt':
        r=sqrt(n1)
    elif ac == 'log':
        r=logarithm(n1)
    else:
        r=0.0
    if r != 0.0:
        print("result is:",r)
    else:
        print("invalid operation")
if __name__ == "__main__":
    main()