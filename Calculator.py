def get_input():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Second first number: "))
        return num1, num2
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return None, None



def add(a, b):
    return a + b 

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by Zero!"
    return a / b


def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    num1, num2 = get_input()
    if num1 is None or num2 is None:
        return
    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", add(num1, num2))
    elif choice == '3':
        print("Result:", add(num1, num2))
    elif choice == '4':
        print("Result:", add(num1, num2))
    else:
        print("Invalid choice")


if __name__ == "__main__":
    calculator()