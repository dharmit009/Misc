"""
Q2. Guess the Number game

-->generate a random correct answer, say between 1 and 100,to know what the correct answer is
-->ask the user to input a guess
-->check to see if the user’s input matches the correct answer
-->if not matches give Feedback on the user’s guess (e.g., “Correct!”; “Too High!” “Too Low!”; etc.)
-->A way to try again if the user’s guess was incorrect(only three attempt)

example
correctans-->generate from random number
guessnum-->ask user to enter

only 3 attempts are required
if-->guessnum below correctans-->than print Too Low
if-->guessnum above correctans-->than print Too High
if-->guessnum equals correctans-->than print Correct!!!

Hint -->import random


"""
import random
answerRequired = random.randint(1,100); ## The winning answer is stored in this variable. 
player_chances = 3; 
guess = None;

## Let us print the winnig answer before even guessing it .... 
print("Let us print the winnig answer before even guessing it .... ");
print("Winning Answer: " , answerRequired);

while player_chances != 0:
    print("Remaining Chances: ", player_chances);
    guess = int(input("Enter a number between [1-100]: "));
    if guess == answerRequired:
        print("You have won the game ...");
        break;
    elif guess < answerRequired:
        print("Your guess is lower than the required answer ... ");
        player_chances -=1; 
    else: 
        print("Your guess is greater than the required answer ..." );
        player_chances -=1; 
