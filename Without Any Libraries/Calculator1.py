def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def modulus(num1, num2):
    return num1 % num2

def power(num1, num2):
    return num1 ** num2

while True:
    try:
        num1 = input("Enter the first number: ")
        if num1.replace(".", "").replace("-", "").replace("+", "").replace("e", "").isnumeric() == False:
            raise ValueError
        num1 = float(num1)
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

while True:
    try:
        num2 = input("Enter the second number: ")
        if num2.replace(".", "").replace("-", "").replace("+", "").replace("e", "").isnumeric() == False:
            raise ValueError
        num2 = float(num2)
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("\nFirst number:", num1)
print("\nSecond number:", num2)



while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Exit")
    choice = input("\nEnter your choice: ")

    
    
    if choice == "1":
        print("\nResult: ", add(float(num1), float(num2)))

    elif choice == "2":
        print("\nResult: ", subtract(float(num1), float(num2)))

    elif choice == "3":
        print("\nResult: ", multiply(float(num1), float(num2)))

    elif choice == "4":
        print("\nResult: ", divide(float(num1), float(num2)))

    elif choice == "5":
        print("\nResult: ", modulus(float(num1), float(num2)))

    elif choice == "6":
        print("\nResult: ", power(float(num1), float(num2)))

    elif choice == "7":
        break

    else:
        print("Invalid choice. Please enter a valid number.")
        