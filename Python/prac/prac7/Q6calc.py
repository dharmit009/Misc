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

def calc():
    breaker = False;
    while breaker != True: 
        menu();
        choice = int(input("Enter number choice: "));
        if choice < 5:
            n1 = int(input("Enter Number1: "));
            n2 = int(input("Enter Number2: "));
            if choice == 1:
                out= n1 + n2;
                print("Addition: ", out)
            elif choice == 2:
                out= n1 - n2;
                print("Subtraction: ", out)
            elif choice == 3:
                out= n1 * n2;
                print("Mulitplication: ", out)
            elif choice == 4:
                out= n1 / n2;
                print("Division: ", out)
            else: 
                print("Please enter choose a valid option.");
        elif choice > 6: 
            repeat = input("Do you want to continue? [y/n]: ");
            if repeat == 'n':
                breaker = False;
        else: 
            breaker = False;




calc()
    
