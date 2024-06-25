import math


def get_two_numbers():
    num1 = int(input("Enter the first number: "))

    num2 = int(input("Enter the second number: "))

    return num1, num2


def find_gcd(num1, num2):
    return math.gcd(num1, num2)


if __name__ == "__main__":
    number1, number2 = get_two_numbers()

    gcd = find_gcd(number1, number2)

    print(f"The first number entered is: {number1}")
    print(f"The second number entered is: {number2}")
    print(f"The Greatest Common Demoninator  of {number1} and {number2} is: {gcd}")
