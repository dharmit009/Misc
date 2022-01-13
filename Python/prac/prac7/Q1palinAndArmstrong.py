def palindrome(n):
    print("")
    temp = int(n);
    summer = 0;
    while n > 0:
        reverse = n % 10;
        summer = (summer*10) + reverse;
        n //= 10;


    if temp == summer: 
       #  print("Number:",temp,"== Palindrome:" ,summer);
        print("It is a palindrome!");
    else: 
        print("Number: {temp} is not a palindrome. ");
    print("")


def armstrong(n):
    print("")
    temp = n;
    result = 0;
    while(temp != 0):
       remainder = temp % 10;
       result += remainder * remainder * remainder;
       temp //= 10;
    
    if result == n: 
        # print("Number:", n,"== Armstrong:", result);
        print("It is a Armstrong!");
    else: 
        print("Number: {temp} is not a Armstrong. ");
    print("")

    
num = int(input("Enter a Number: "));
palindrome(num)
armstrong(num)


