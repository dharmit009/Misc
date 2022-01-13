import random 

def generate_randomInt():
    random_num = random.randint(0,9)
    return random_num


def getGuess():
    guess = int(input("Enter Your Guess [0-9]: ")) 
    return guess


def checker(guess: int, randomno: int):
    if guess == randomno: 
        print("You won!!")
        return True;
    elif guess < randomno:
        print("Your guess is lower than random.")
        return False;
    elif guess > randomno:
        print("Your guess is higher than random.")
        return False;
    else: 
        print("Error [E]: Please enter a valid input ...")


def main():
    global chances
    chances = 3
    randomno = generate_randomInt()
    while chances > 0:
        chances-=1
        guess = getGuess()
        checking = checker(guess, randomno)
        if checking == True:
            chances = 0


if __name__ == '__main__':
    main()
