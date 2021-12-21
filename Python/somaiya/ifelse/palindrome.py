def palindrome(String1):
    String2 = String1[::-1];
    if String1 == String2: 
        print("Yes, It is a palindrome");
    else: 
        print("No, It is not a palindrome");



print(" #### Palindrome or Not #### ");
userString = input("Enter a String: ");
palindrome(userString)


