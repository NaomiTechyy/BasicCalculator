# Basic Calculator Program

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (plus, minus, multiply, divide): ").strip().lower()

# Perform the calculation
if operation == "+":
    result = num1 + num2
    symbol = "+"
elif operation == "-":
    result = num1 - num2
    symbol = "-"
elif operation == "*":
    result = num1 * num2
    symbol = "*"
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        symbol = "/"
    else:
        print("Error: Division by zero is not allowed.")
        exit()
else:
    print("Invalid operation. Please enter plus, minus, multiply, or divide.")
    exit()

# Display the result
print(f"{num1} {symbol} {num2} equals {result}")