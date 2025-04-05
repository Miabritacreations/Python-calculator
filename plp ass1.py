# Simple calculator with input validation and loop

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operation():
    valid_operations = ['+', '-', '*', '/']
    while True:
        op = input("Enter the operation (+, -, *, /): ")
        if op in valid_operations:
            return op
        else:
            print("Invalid operation. Please enter one of +, -, *, /.")

while True:
    # Get user input
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    operation = get_operation()

    # Perform the operation
    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error! Division by zero is not allowed.")

    # Ask if the user wants to continue
    again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if again != 'yes':
        print("Thanks for using the calculator! Bye babe 😘")
        break
