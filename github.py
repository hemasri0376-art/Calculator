# calculator.py

from datetime import datetime

history = []

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b


def show_menu():
    print("\n===== Python Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. View History")
    print("6. Exit")


while True:
    show_menu()

    choice = input("Enter your choice (1-6): ")

    if choice == "6":
        print("\nThanks for using the calculator!")
        break

    if choice == "5":
        print("\n----- Calculation History -----")
        if history:
            for item in history:
                print(item)
        else:
            print("No calculations yet.")
        continue

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Try again.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        continue

    if choice == "1":
        result = add(num1, num2)
        operator = "+"
    elif choice == "2":
        result = subtract(num1, num2)
        operator = "-"
    elif choice == "3":
        result = multiply(num1, num2)
        operator = "*"
    else:
        result = divide(num1, num2)
        operator = "/"

    print(f"Result: {result}")

    history.append(
        f"{datetime.now().strftime('%H:%M:%S')} | {num1} {operator} {num2} = {result}"
    )
