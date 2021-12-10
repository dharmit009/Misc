print(" ### SUM OF SQUARE OF NUMBERS ### ")
print("How many numbers do you want to add ?")
n = int(input(">> ")); 

a[n] = {}; 
summer = 0 
i = 0
while n>=0:
    print("Enter number [", i, "]: ")
    a[i] = float(input());
    summer += (a[i]**2)
    i += 1;
    n -= 1;

print(a);
print(summer);

