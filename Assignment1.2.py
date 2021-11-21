a = float(input("Enter number a:"))
b = float(input("Enter number b:"))
operator = (input( "Enter an operator:"))
if operator == "+":
    print("Sum is",a + b )
elif operator == "-":
    print("Difference is",a - b )
elif operator == "*":
    print("Product is",a * b )
elif operator == "/":
    print("Division is",a / b )
else:
    print("Invalid input")
