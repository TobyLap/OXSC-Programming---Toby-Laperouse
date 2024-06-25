import random










print(80 * '=')
print('\t\t         Welcome to the Slot Machine Simulator\n' " You'll start with $50. You'll be asked if you want to play. (each loss is $10)")
print(80 * '=')

INIT_money = 50
ITEMS = ["CHERRY", "ORANGE", "PLUM", "LEMON", "BELL", "BAR"]

firstWheel = None
secondWheel = None
thirdWheel = None
money = INIT_money


def play():
    global money, firstWheel, secondWheel, thirdWheel
    playQuestion = askPlayer()
    while(money > 9.9 and playQuestion == True):
        firstWheel = spinWheel()
        secondWheel = spinWheel()
        thirdWheel = spinWheel()
        printScore()
        playQuestion = askPlayer()
    if (money <= 9.9):
        playQuestion == False
        print("What money do you have to 'Play Again?'. You are a broke mf lol.")



def askPlayer():
    global money
    while (True):
        answer = input("Would you like to play? " + "You have $" + str(money) + ". " )
        answer = answer.lower()
        print(80 * '-')
        if(answer == "yes" or answer == "y" or answer == "yep" or answer == "yup" ):
            return True
        elif(answer == "no" or answer == "n" or answer == "nope" or answer == "nuh-uh"):
            print("You walked away with $" + str(money) + " in your hand. ")
            return False

        else:
            print("Wrong Input!")


def spinWheel():
    randomNumber = random.randint(0, 5)
    return ITEMS[randomNumber]

def printScore():
    global money, firstWheel, secondWheel, thirdWheel
    if((firstWheel == "CHERRY") and (secondWheel != "CHERRY")):
        win = 2
    elif ((firstWheel == "BAR") and (secondWheel == "BAR") and (thirdWheel == "BAR")):
        win = 250
    elif((firstWheel == "CHERRY") and (secondWheel == "CHERRY") and (thirdWheel != "CHERRY")):
        win = 5
    elif((firstWheel == "CHERRY") and (secondWheel == "CHERRY") and (thirdWheel == "CHERRY")):
        win = 7
    elif((firstWheel == "ORANGE") and (secondWheel == "ORANGE") and (thirdWheel == "ORANGE") or (thirdWheel == "BAR")):
        win = 10
    elif((firstWheel == "PLUM") and (secondWheel == "PLUM") and (thirdWheel == "PLUM") or (thirdWheel == "BAR")):
        win = 14
    elif((firstWheel == "BELL") and (secondWheel == "PLUM") and (thirdWheel == "BELL") or (thirdWheel =="BAR")):
        win = 20

    else:
        win = -10

    money += win

    if(win > 0):
        print('{:<10}{:^10}{:^10}{:>28}' .format(printEmoji(firstWheel), printEmoji(secondWheel), printEmoji(thirdWheel), ("You Win $")) + str(win))
    else:
        print('{:<10}{:^10}{:^10}{:>28}' .format(printEmoji(firstWheel), printEmoji(secondWheel), printEmoji(thirdWheel), ("You lose")))




def printEmoji(wheel):
    if wheel == 'BELL':
        return '🔔'
    if wheel == "CHERRY":
        return '🍒'
    if wheel == "ORANGE":
        return '🍊'
    if wheel == "PLUM":
        return '🍎'
    if wheel == "BAR":
        return '🍫'
    if wheel == "LEMON":
        return '🍋'

play()


