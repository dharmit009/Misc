""" 
Q1)
Write a program (using functions!) that asks the user for
a long string containing multiple words. Print back to the
user the same string, except with the words in backwards
order. For example, say I type the string:

Input:
My name is Rupa
  
Then I would see the string:
Rupa is name My

"""

def reverser():
    user_input = input("Enter a string: ");
    print("Input String: ", user_input);
    user_input = user_input.split(" ")
    print("Output String: ", end="");
    for x in user_input[::-1]:
        print(x, end=" ")
    print("")


reverser()



    

