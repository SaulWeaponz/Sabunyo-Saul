#Assignment Two:
# Write a program to handle errors, the program should ask for two number using input and then
# divides them. Use an infinite loop to keep asking until a valid input is provide.
while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
        print("The result of the division is:", result)
        break  # Exit the loop if the input and calculation are successful
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        break
    except ZeroDivisionError:
        print("Cannot divide by zero. Please enter a non-zero second number.")
