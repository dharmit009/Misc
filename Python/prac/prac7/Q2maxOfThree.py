
def maxi(a,b,c):
    if a > b and a > c:
        return a; 
    elif b > a and b > c:
        return b; 
    else: 
        return c; 


a = int(input("Enter number a: "));
b = int(input("Enter number b: "));
c = int(input("Enter number c: "));
maximumNumber = maxi(a,b,c);

print("Maximum: ", maximumNumber);
