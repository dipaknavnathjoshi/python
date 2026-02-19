 
def calculator():
    print("==== Simple Calculator ====")
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        print("Operations:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        
        choice = input("Choose operation (1/2/3/4): ")
        
        if choice == "1":
            print("Result:", num1 + num2)
        
        elif choice == "2":
            print("Result:", num1 - num2)
        
        elif choice == "3":
            print("Result:", num1 * num2)
        
        elif choice == "4":
            print("Result:", num1 / num2)
        
        else:
            print("Invalid choice!")

    except ValueError:
        print("Error: Please enter valid numbers.")
    
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    except Exception as e:
        print("Something went wrong:", e)


# Run in loop
while True:
    calculator()
    again = input("Do you want to continue? (yes/no): ").lower()
    if again != "yes":
        print("Thank you! Exiting program.")
        break
