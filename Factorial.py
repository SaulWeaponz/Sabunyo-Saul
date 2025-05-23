# Qn. Write a program to find the factorial of a number(number=5)

# number = int(input("Enter the number to find the factorial : "))
number = 5

def Factorial(n):
    fact =1 # base case value.
    if (n>1): # recursive case(decomposition)
        fact = Factorial(n-1)*n # composition
    return fact  
    
print("Factorial of a number is : ", Factorial(number))