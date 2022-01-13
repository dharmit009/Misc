import random
from colorama import Fore

def guessch():
    guessed_ch = str(input("Enter a letter: ")).lower()
    if not guessed_ch.isalpha():
        print(Fore.RED, "[E] Error: Please input a valid character.")
        guessch()
    elif len(guessed_ch) > 1: 
        print(Fore.RED, "[E] Error: Please input a single character.")
        guessch()
    else: 
        return guessed_ch
        
def display():
    for ch in hidden_word:
        if ch in guessed_characters:
            print(ch, sep="", end=" ")
        else: 
            print("_", sep="", end=" ")
    print("")



guess_limit = 15
guessed_characters = []
wordlist = ["red", "green", "blue", "yellow", "purple", "grey", "black"]
breaker = False
rand_select = random.randint(0, len(wordlist))
hidden_word = wordlist[rand_select]
hidden_list = list(hidden_word)


while not breaker: 
    display()
    guess = guessch()
    guessed_characters.append(guess)
    guess_limit -= 1
    guessed_word = ''.join(guessed_characters)

    if guess_limit <= 0:
        breaker = True 
    else:
        breaker = False
    


