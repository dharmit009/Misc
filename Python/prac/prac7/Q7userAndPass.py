
""" Create a program using user defined function named login than accepts userid and password as aparameters
1)dispaly message "account blocked" in case of three wrong attempts
2)"Login Successful" if the user enter user id as "ADMIN" and Password as "Password" or display "Login Incorrect!!
"""

def getData():
    usrname = input("Enter username: ")
    passwd = input("Enter passwd: ")
    login(userid, passwd)

def login(userid, passwd):
    cred_username = "ADMIN"
    cred_password = "Password"
    



attempts = 0;
while attempts < 3:
    login(userid, passwd, attempts)
else:
    pass
