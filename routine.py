# Starting the Routine
print(80 * '=')
print("You wake up by a 2763 kg dumbbell smashing you in your balls. Feels Good.")
print(80 * '=')
def ask_yes_no_question():
    while True:
        answer = input("Is Today Sunday?: ").strip().lower()
        print(80 * '-')
        if answer in ['yes', 'y', 'yup', 'yep']:
            return True
        elif answer in ['no', 'n', 'nope', 'nuh-uh']:
            return False
        else:
            print("Invalid input. Please enter 'yes', or 'no'")
            print(80 * '-')

# Bro, is it sunday?
if ask_yes_no_question():
    print("SUNDAY FUNDAY!!! NO HOMEWORK!!!")
    print(80 * '-')
else:
    print("DO YOUR HOMEWORK!")
    print(80 * '-')


    def ask_yes_no_question():
        while True:
            answer = input("Do Your Homework?: ").strip().lower()
            print(80 * '-')
            if answer in ['yes', 'y', 'yup', 'yep']:
                return True
            elif answer in ['no', 'n', 'nope', 'nuh-uh']:
                return False
            else:
                print("Invalid input. Please enter 'yes', or 'no'")
                print(80 * '-')


    # Are you responsible for your homework?
    if ask_yes_no_question():
        print("GO PLAY NOW! HOMEWORK FINISHED!")
        print(80 * '-')
    else:
        print("You didn't do your homework.")
        print(80 * '-')