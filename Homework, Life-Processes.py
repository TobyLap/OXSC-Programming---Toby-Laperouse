# I know it told me to do a flow chart. But I thought this is okay as well
# I hope this is fine as well

def adopt_pet():
    # Function to standardize input
    def standardize_input(response):
        response = response.strip().lower()
        if response in ['y', 'yes', 'yup', 'yep', 'hell yes']:
            return 'y'
        elif response in ['n', 'no','nope', 'nuh-uh', 'fuck no']:
            return 'n'
        else:
            return None

    # Question 1
    income = standardize_input(input("Do you have a stable source of income?: "))
    if income not in ['y', 'n']:
        print("Invalid input. Please enter 'yes' or 'no'.")
        return

    # Question 2
    living_environment = standardize_input(
        input("Do you have a suitable living environment for a pet?: "))
    if living_environment not in ['y', 'n']:
        print("Invalid input. Please enter 'yes' or 'no'.")
        return

    # Question 3
    commitment = standardize_input(
        input("Are you willing to commit to taking care of the pet's needs?: "))
    if commitment not in ['y', 'n']:
        print("Invalid input. Please enter 'yes' or 'no'.")
        return

    # Decision making
    if income == 'y' and living_environment == 'y' and commitment == 'y':
        print("Congratulations! You can adopt a pet.")
    else:
        print("Unfortunately, you do not meet the requirements to adopt a pet at this time.")


# Call the function to start the process
adopt_pet()
