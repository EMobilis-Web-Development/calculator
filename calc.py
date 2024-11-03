print('-----welcome to the calculator-----')
import math

def add(x, y):
    return x + y

def minus(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

def squareroot(x):
    return math.sqrt(x)

def cosine(x):
    return math.cos(x)

def tangent(x):
    return math.tan(x)

def cuberoot(x):
    return x ** (1 / 3)  

# User's prompt
x = int(input('Please enter the value of x: '))
operator = input('Choose the operator you may want to use (+, -, *, /, sqrt, cos, tan, cbrt): ')

one_value_operators = ['sqrt', 'cos', 'tan', 'cbrt']

if operator not in one_value_operators:
    y = int(input('Please enter the value of y: '))

if operator == '+':
    result = add(x, y)
    print(f"The result is: {result}")

elif operator == '-':
    result = minus(x, y)
    print(f"The result is: {result}")

elif operator == '*':
    result = multiplication(x, y)
    print(f"The result is: {result}")

elif operator == '/':
    result = division(x, y)
    print(f"The result is: {result}")

elif operator == 'sqrt':
    result = squareroot(x)
    print(f"The result is: {result}")

elif operator == 'cos':
    result = cosine(x)
    print(f"The result is: {result}")

elif operator == 'tan':
    result = tangent(x)
    print(f"The result is: {result}")

elif operator == 'cbrt':
    result = cuberoot(x)
    print(f"The result is: {result}")





