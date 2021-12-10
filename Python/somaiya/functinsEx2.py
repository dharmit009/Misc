## create 2 functions: 
## 1. Outer Function
## 2. Inner Function
## Outer function 1 parameter return inner + 10 
## Inner Calculate sqr 

## nested function.

def outer(a): 

    def squarer():
        result = a**2;
        return result;

    result=squarer();
    result = result + 10;
    return result 
    

num = int(input("Enter the input: "));
print(outer(num));

