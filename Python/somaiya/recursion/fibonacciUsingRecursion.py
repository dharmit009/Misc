def fib(n): 
    if n == 0: 
        return 0; 
    elif n == 1: 
        return 1; 
    else: 
        return fib(n-1)+fib(n-2);

n = int(input("Enter a Number: "));
out = fib(n)
print(out);


## To Print the whole series do the following: 

print("Fibonacci Series: ");
for x in range(n+1): 
    out = fib(x)
    print(out, end=", ");
print("...");

