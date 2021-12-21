# WAP in python to accept number from user and calculate sum of first n natural numbers
#

n = int(input("Enter a number: "));
sum = 0; 

for x in range(0, n+1): 
    print(x, end="+");
    sum += x;

print("");
print(sum);
