print (80 * '-')
x = int(input("Enter a Number: "))
print (80 * '-')
y = int(input("Enter a Second Number: "))
print (80 * '-')
x1 = x
y1 = y

while True:
    if x > y:
        x = x - y
    elif y > x:
        y = y - x
    elif x == y:
        print(f"The Greatest Common Demoninator of {x1} and {y1} is {x}.")
        print(80 * '-')
        break