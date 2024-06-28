import random

print(80 * '=')
print('\t\t         Welcome to the Slot Machine Simulator\n' " You'll start with $100. You'll be asked if you want to play. (each loss is $10)")
print(80 * '=')

INIT_money = 100
ITEMS = ["CHERRY", "ORANGE", "PLUM", "LEMON", "BELL", "BAR"]

firstWheel = None
secondWheel = None
thirdWheel = None
money = INIT_money

def play():
    global money, firstWheel, secondWheel, thirdWheel
    playQuestion = askPlayer()
    while money > 9.9 and playQuestion:
        firstWheel = spinWheel()
        secondWheel = spinWheel()
        thirdWheel = spinWheel()
        printScore()
        playQuestion = askPlayer()
    if money <= 9.9:
        playQuestion = False
        print("What money do you have to 'Play Again?'. You are a broke mf lol.")
        print (80 * '-')

def askPlayer():
    global money
    while True:
        answer = input(f"Would you like to play? You have ${money}. ").strip().lower()
        print(80 * '-')
        if answer in ["yes", "y", "yep", "yup"]:
            return True
        elif answer in ["no", "n", "nope", "nuh-uh"]:
            print(f"You walked away with ${money} in your hand.")
            print(80 * '-')
            return False
        else:
            print("Wrong Input!")

def spinWheel():
    return random.choice(ITEMS)

def printScore():
    global money, firstWheel, secondWheel, thirdWheel
    win = 0
    if firstWheel == "CHERRY" and secondWheel == "CHERRY" and thirdWheel == "CHERRY":
        win = 7
    elif firstWheel == "CHERRY" and secondWheel == "CHERRY":
        win = 5
    elif secondWheel == "CHERRY" and thirdWheel == "CHERRY":
        win = 5
    elif (firstWheel == secondWheel == thirdWheel == "BAR"):
        win = 250
    elif (firstWheel == "BAR" and secondWheel == "BAR") or (secondWheel == "BAR" and thirdWheel == "BAR") or (firstWheel == "BAR" and thirdWheel == "BAR"):
        win = 50
    elif (firstWheel == "PLUM" and secondWheel == "PLUM" and thirdWheel == "PLUM"):
        win = 25
    elif (firstWheel == "PLUM" and secondWheel == "PLUM") or (firstWheel == "PLUM" and thirdWheel == "PLUM") or (secondWheel == "PLUM" and thirdWheel == "PLUM"):
        win = 7
    elif (firstWheel == "ORANGE" and secondWheel == "ORANGE" and thirdWheel == "ORANGE") or (firstWheel == "ORANGE" and secondWheel == "ORANGE" and thirdWheel == "BAR"):
        win = 10
    elif (firstWheel == "BELL" and secondWheel == "BELL" and thirdWheel == "BELL"):
        win = 30
    elif (firstWheel == "BELL" and secondWheel == "BELL") or (secondWheel == "BELL" and thirdWheel == "BELL") or (firstWheel == "BELL" and thirdWheel == "BELL"):
        win = 15
    elif (firstWheel == "LEMON" and secondWheel == "LEMON" and thirdWheel == "LEMON"):
        win = 6
    elif (firstWheel == "LEMON" and secondWheel == "LEMON") or (firstWheel == "LEMON" and thirdWheel == "LEMON"):
        win = 3
    else:
        win = -10

    money += win
    if win > 0:
        print(f'{printEmoji(firstWheel):<10}{printEmoji(secondWheel):^10}{printEmoji(thirdWheel):^10}{"You Win $":>28}{win}')
    else:
        print(f'{printEmoji(firstWheel):<10}{printEmoji(secondWheel):^10}{printEmoji(thirdWheel):^10}{"You lose":>28}')

def printEmoji(wheel):
    emojis = {
        'BELL': '🔔',
        'CHERRY': '🍒',
        'ORANGE': '🍊',
        'PLUM': '🍎',
        'BAR': '🍫',
        'LEMON': '🍋'
    }
    return emojis.get(wheel, '')

play()
