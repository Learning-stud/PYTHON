# Choice Board
print("""---------CHOICE BOARD--------------
    1. ADDITION
    2. MULTIPLICATION
    3. SUBTRACTION
    4. DIVISION
""")

# User Input
choice = int(input("Enter your choice (1/2/3/4): "))

# Input Numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif choice == 2:
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif choice == 3:
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif choice == 4:
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid choice. Please choose 1, 2, 3, or 4.")
