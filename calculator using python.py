def add(num1, num2):
    """Returns the sum of two numbers."""
    return num1 + num2

def subtract(num1, num2):
    """Returns the difference of two numbers."""
    return num1 - num2

def multiply(num1, num2):
    """Returns the product of two numbers."""
    return num1 * num2

def divide(num1, num2):
    """Returns the division of two numbers. Handles division by zero."""
    if num2 == 0:
        return "Error! Division by zero."
    return num1 / num2

def modulo(num1, num2):
    """Returns the remainder of the division of two numbers."""
    return num1 % num2

def exponent(num1, num2):
    """Returns the result of raising one number to the power of another."""
    return num1 ** num2

def display_menu():
    """Displays the menu of operations."""
    print("\nPlease select operation -")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulo")
    print("6. Exponent")
    print("7. Exit")

def get_operation_choice():
    """Gets the user's choice of operation."""
    while True:
        try:
            choice = int(input("Select operation from 1 to 7: "))
            if choice in range(1, 8):
                return choice
            else:
                print("Invalid input! Please select a valid operation.")
        except ValueError:
            print("Invalid input! Please enter a number from 1 to 7.")

def get_numbers():
    """Gets two numbers from the user."""
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input! Please enter numerical values.")

def main():
    """Main function to run the calculator."""
    while True:
        display_menu()
        choice = get_operation_choice()
        
        if choice == 7:
            print("Exiting the calculator. Goodbye!")
            break
        
        num1, num2 = get_numbers()
        
        if choice == 1:
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == 2:
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == 3:
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == 4:
            result = divide(num1, num2)
            if result == "Error! Division by zero.":
                print(result)
            else:
                print(f"{num1} / {num2} = {result}")
        elif choice == 5:
            print(f"{num1} % {num2} = {modulo(num1, num2)}")
        elif choice == 6:
            print(f"{num1} ^ {num2} = {exponent(num1, num2)}")
        
        restart = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if restart != 'yes':
            print("Exiting the calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
