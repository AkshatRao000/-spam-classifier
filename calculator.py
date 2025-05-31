def calculator():
    print("Welcome to the Simple Calculator!")
    print("Enter 'quit' to exit.")

    while True:
        operation = input("\nEnter an operation (+, -, *, /): ")
        if operation == 'quit':
            break

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero is not allowed.")
                continue
        else:
            print("Error: Invalid operation. Please enter a valid operation (+, -, *, /).")
            continue

        print(f"The result is: {result}")

calculator()