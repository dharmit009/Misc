import random

class dices: 

    def __init__(self, name): 
        self.name = name;

    def roll(self):
        randomNumber = random.randint(1,6);
        print(self.name, ": ", randomNumber);


d1 = dices("Dice1");
d2 = dices("Dice2");

while True: 
    userIn = input();
    if userIn == "exit" or userIn == "quit":
        print("Exitting ...")
        break; 

    else: 
        d1.roll()
        d2.roll()


