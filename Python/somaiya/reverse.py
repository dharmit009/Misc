n = int(input("Enter A Number: "));
rev = 0

# Iteration1:
# 123
# 12.3 i.e rem = 3
# rev = (0*10)+3 = 3
# n = 123/10 = 12

# Iteration2:
# 12
# 1.2 i.e rem = 2
# rev =(3*10)+2 = 32
# n = 123/10 = 1

# Iteration3:
# 1
# 0.1 i.e rem = 1
# rev =(32*10)+1 = 321
# n = 1/10 = 0.1

# N reached to zero end the program 

while(n!=0):
    rem = int(n%10); 
    rev = int((rev*10)+rem);
    n   = int(n / 10); 

print(rev);

