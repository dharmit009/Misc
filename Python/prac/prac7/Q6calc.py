""" create a menu driven program using user defined fucntion to implement calculator that perform
basic arithmetic operation."""

def menu():
    message = """## CALCULATOR ##
    1. Add. 
    2. Subtract. 
    3. Multiply. 
    4. Divide. 
    5. Exit. 
    """; 
    print(message);
    choice = int(input("Enter number choice: "));
    return choice

def getInput():
            n1 = int(input("Enter Number1: "));
            n2 = int(input("Enter Number2: "));
            return n1 , n2; 

def calc():

    breaker = False;

    while breaker != True: 
        choice = menu();

        # FIXME: Use the math range notation instead. i.e 0 < choice < 6: 
        if choice < 6 and choice > 0:
            if choice == 5:
                breaker = True;
            elif choice == 1:
                n1 , n2 = getInput()
                out= n1 + n2;
                print("Addition: ", out)
            elif choice == 2:
                n1 , n2 = getInput()
                out= n1 - n2;
                print("Subtraction: ", out)
            elif choice == 3:
                n1 , n2 = getInput()
                out= n1 * n2;
                print("Mulitplication: ", out)
            elif choice == 4:
                n1 , n2 = getInput()
                out= n1 / n2;
                print("Division: ", out)
        else: 
            print("Error! [E] : Invalid Input");

        inn = input("Do you want to run it again? [y/n]: "); 
        if inn == 'n':
            breaker = True; 

calc()
    
