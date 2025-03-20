# Program make a simple calculator

# This Function adds two number
def add(x, y):
    return x + y
# This Function subtract two number
def subtract(x, y):
    return x - y
# This Function multiplies two number
def multiply(x, y):
    return x * y
# This Function divides two number
def divide(x, y):
    return x / y

num1 = int(input("Enter a Number 1 : "))
num2 = int(input("Enter a Number 2 : "))


print("Sum :", add(num1, num2))
print("Difference :", subtract(num1, num2))
print("Product :", multiply(num1, num2))
print("Quotient:", divide(num1, num2))
