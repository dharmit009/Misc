# 3 8 7 5 
# Enter any number and display number in terms of words

num_word = {
    "1": "one", 
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
}

userInput = input("Enter a number: ")
userInput = list(userInput)

for x in userInput:
    print(num_word[x], sep=" ", end=" ")
print()
    

