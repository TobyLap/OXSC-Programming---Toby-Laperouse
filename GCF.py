# Finding the Greatest Common Factor of Two Numbers
import math

# Function to calculate GCF/GCD of two numbers
def find_gcf(a, b):
    return math.gcd(a, b)

# Taking input from the user with validation
while True:
    try:
        num1 = int(input("Enter the first number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

while True:
    try:
        num2 = int(input("Enter the second number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Calculating GCF
gcf = find_gcf(num1, num2)
print(f"The Greatest Common Factor of {num1} and {num2} is {gcf}.")
