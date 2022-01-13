
""" Create a program using user defined function named login than accepts userid and password as aparameters
1)dispaly message "account blocked" in case of three wrong attempts
2)"Login Successful" if the user enter user id as "ADMIN" and Password as "Password" or display "Login Incorrect!!
"""

global attempts;
attempts = 0; 

def login(attempted_id, attempted_passwd):
    cred_user = "ADMIN"
    cred_passwd = "Password"
    if attempted_id == cred_user and attempted_passwd == cred_passwd: 
        print("Login has been Successful !"); 
        return True;
    else: 
        print("Login Failed !");
        return False;

def passcheck(attempts):
    while attempts < 3: 
        attempted_id = input("Enter Your UserId: ");
        attempted_passwd = input("Enter Your Passwd: ");
        passchecker = login(attempted_id, attempted_passwd);
        # DEBUGGING BLOCK
        #  print("PassChecker: ", passchecker, "Attempts: ", attempts);
        if passchecker == False and attempts > 1: 
            print("Account has been blocked");
            break;
        elif passchecker == True and attempts <= 3: 
            break;
        else: 
            pass;
        attempts += 1; 


passcheck(attempts);
