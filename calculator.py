# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

def display_menu():
    print("\n====== Calculator Menu ======")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("=============================")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    while True:
        display_menu()
        choice = input("Choose an operation (1-5): ")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == '1':
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Invalid choice. Please select a valid operation (1-5).")

if __name__ == "__main__":
    main()
