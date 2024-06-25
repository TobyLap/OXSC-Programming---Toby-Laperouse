print(80 * '-')
name = input("Enter your name: ")
print(80 * '-')

while True:
    age_input = input("Enter your age: ")
    print(80 * '-')
    try:
        age = int(age_input)
        if age < 0:
            print("Age cannot be negative. Please enter a valid age.")
            print(80 * '-')
        else:
            break
    except ValueError:
        print("Please enter a valid number for your age.")
        print(80 * '-')

if age == 1:
    print(f"My name is {name} and I am {age} year old")
    print(80 * '-')
else:
    print(f"My name is {name} and I am {age} years old")
    print(80 * '-')