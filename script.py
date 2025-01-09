''' random code '''

print("Hello World")
print(2*10)
A = 19
B = 20
print(A + B)


def print_table(n):
    ''' This function prints the table of the given number '''
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

print_table(2)

def add(a, b):
    ''' This function returns the sum of two numbers '''
    return a + b

print(add(2, 3))
print(add(4, 5))

def subtract(a, b):
    ''' This function returns the difference of two numbers '''
    return a - b

print(subtract(2, 3))
print(subtract(4, 5))

def multiply(a, b):
    ''' This function returns the product of two numbers '''
    return a * b

print(multiply(2, 3))
print(multiply(4, 5))

def divide(a, b):
    ''' This function returns the division of two numbers '''
    return a / b

print(divide(2, 3))
print(divide(4, 5))

def power(a, b):
    ''' This function returns the power of a to the b '''
    return a ** b

print(power(2, 3))
print(power(4, 5))

def factorial(n):
    ''' This function returns the factorial of a number '''
    if n == 0:
        return 1
    return n * factorial(n-1)
print(factorial(5))
print(factorial(6))
