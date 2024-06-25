# Function to print the multiplication table of a given number
def print_multiplication_table(number):
    print(f"Multiplication Table for {number} up to 10")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Code stuff lol
if __name__ == "__main__":
    try:
        # number input
        number = int(input("Please Enter a Number: "))
        # Print the multiplication table
        print_multiplication_table(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
