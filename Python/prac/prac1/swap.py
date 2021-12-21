a = int(input("enter a number1: "));
b = int(input("enter a number2: "));

print("Before Swap ...");
print("a: ", a);
print("b: ", b);

a = a + b; 
b = a - b; 
a = a - b;

print("After Swap ...");
print("a: ", a);
print("b: ", b);

