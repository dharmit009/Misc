# d. Write a function that reverses the user defined value.

def reverser(a): 
    if type(a) == str: 
        print("String Detected");
        return a[::-1]
    else: 
        print("Integer Detected");
#        rem ,rev = 0, 0
#        while a != 0:
#            rem = a % 10
#            rev = (rev*10) + rem
#            a = a //  10
        return a[::-1]


print(" ### REVERSER ### ");
choice = input("1. Reverse String\n2. Reverese Numbers.");
if choice == 1: 
    a = input("Enter String: ");
elif choice == 2: 
    a = input("Enter Number: ");
else:
    print("Error !!! Choice not found");

print(reverser(a));
