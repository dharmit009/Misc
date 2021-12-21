## WAP in python to accept number from user and find divisor for number

n = int(input("Enter a number: "))

divisor = 1; 

print("Divisors: ", end=" ");
while divisor <=n:
    if (n % divisor == 0): 
        print(divisor, end=", ");
    divisor = divisor +1;
print(" ");

